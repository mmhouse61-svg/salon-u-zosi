"""Przygotowanie grafik do gry: klienci (bez tła), warstwy włosów (do farbowania), gumki, Zosia, kot, fartuszek."""
import os, glob, re, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

ROOT = '/Users/marcinmirecki/OS/Róża gra'
SRC = ROOT + '/grafiki/wyciete'
OUT = ROOT + '/img'
os.makedirs(OUT, exist_ok=True)
W, H = 1100, 1430
PAD = 260           # zapas u góry na kok, irokez i kucyki
PADX = 100          # zapas po bokach na kucyki
H2 = H + PAD
W2 = W + 2 * PADX
OW, OH = W2 // 2, H2 // 2   # rozmiar w grze (proporcja zachowana)

def numerowane():
    d = {}
    for f in glob.glob(SRC + '/*-*.png'):
        m = re.search(r'-(\d+)\.png$', f)
        if m:
            d[int(m.group(1))] = f
    return d

def usun_tlo(rgb):
    """Białe tło połączone z krawędzią -> przezroczyste (białe kołnierze/oczy zostają)."""
    biale = rgb.min(axis=2) > 236
    lab, _ = ndi.label(biale)
    brzeg = set(np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))) - {0}
    tlo = np.isin(lab, list(brzeg))
    tlo = ndi.binary_dilation(tlo, iterations=1)
    alfa = ndi.gaussian_filter(np.where(tlo, 0, 255).astype(float), 1.0)
    return alfa.astype(np.uint8)

def hsv(a):
    mx, mn = a.max(2), a.min(2)
    s = np.where(mx > 0, (mx - mn) / np.maximum(mx, 1e-6), 0)
    return s, mx

def zapisz(arr_rgba, nazwa, rozmiar=(OW, OH)):
    im = Image.fromarray(arr_rgba.astype(np.uint8))
    if rozmiar:
        im = im.resize(rozmiar, Image.LANCZOS)
    im.save(f'{OUT}/{nazwa}.webp', quality=88, method=6)
    print(nazwa, im.size, os.path.getsize(f'{OUT}/{nazwa}.webp') // 1024, 'KB')

def wytnij_wlosy(rgb):
    a = rgb.astype(float) / 255
    s, v = hsv(a)
    yy, xx = np.mgrid[0:H, 0:W]
    # u góry głowy włosy mają jasne refleksy (do 0.97); niżej biel to oczy/kołnierz, więc limit niższy
    vmax = np.where(yy < 430, 0.975, 0.88)
    szare = (s < 0.17) & (v > 0.40) & (v < vmax)
    szare = ndi.binary_opening(szare, iterations=1)
    # kołnierzyk i okolice szyi: tam włosów nie ma
    szare &= ~((xx > 330) & (xx < 770) & (yy > 820))
    lab, n = ndi.label(szare, structure=np.ones((3, 3)))
    if n:
        pola = ndi.sum(np.ones_like(lab), lab, range(1, n + 1))
        szare = np.isin(lab, [i + 1 for i, p in enumerate(pola) if p >= 0.01 * pola.max() and p > 400])
    ciemne = v < 0.50
    obrys = ciemne & ndi.binary_dilation(szare, iterations=5) & ~((xx > 330) & (xx < 770) & (yy > 820))
    maska = ndi.binary_closing(szare | obrys, iterations=3)
    # zamknięcie małych dziur w górnej części (refleksy)
    gora = ndi.binary_fill_holes(maska) & (yy < 430)
    maska = maska | (gora & ~ndi.binary_dilation(~gora, iterations=0) & ((s < 0.2) | (v < 0.5)))
    # gumki: różowe piksele tuż obok włosów
    rozowe = (a[..., 0] - a[..., 1] > 0.22) & (a[..., 2] > a[..., 1]) & (s > 0.28) & (v > 0.6)
    gumki = rozowe & ndi.binary_dilation(maska, iterations=14) & (yy < 1000)
    gumki = ndi.binary_closing(gumki, iterations=2)
    gumki = ndi.binary_dilation(gumki, iterations=2)
    lab, n = ndi.label(gumki)
    if n:
        pola = ndi.sum(np.ones_like(lab), lab, range(1, n + 1))
        gumki = np.isin(lab, [i + 1 for i, p in enumerate(pola) if p > 150])
    maska = maska & ~gumki
    # warstwa włosów: jasność znormalizowana, żeby mnożenie kolorem dawało żywy kolor
    jas = np.clip(v / 0.74, 0, 1)
    rgb_w = np.dstack([jas, jas, jas]) * 255
    alfa_w = ndi.gaussian_filter(maska.astype(float), 1.0) * 255
    alfa_g = ndi.gaussian_filter(gumki.astype(float), 1.0) * 255
    return (np.dstack([rgb_w, alfa_w]), np.dstack([a * 255, alfa_g]), gumki.any())


def miary(rgb):
    """Szerokość głowy (od ucha do ucha) i środek oczu: do dopasowania warstw włosów do głowy bazowej."""
    a = rgb.astype(float) / 255
    s, v = hsv(a)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    skora = (r > g) & (g > b) & (s > 0.15) & (s < 0.7) & (v > 0.55)
    ys, xs = np.nonzero(skora[450:760])
    szer = np.percentile(xs, 99.5) - np.percentile(xs, 0.5)
    xx, yy = np.arange(W)[None, :], np.arange(H)[:, None]
    ciemne = (v < 0.28) & (xx > 250) & (xx < 850) & (yy > 380) & (yy < 760)
    return szer, np.nonzero(ciemne)[1].mean(), np.nonzero(ciemne)[0].mean()

def dopasuj(rgba, m, wzor):
    """Przeskaluj i przesuń warstwę tak, by oczy i szerokość głowy pokrywały się ze wzorcem."""
    sk = wzor[0] / m[0]
    ox, oy = wzor[1], wzor[2]
    hx, hy = m[1], m[2]
    im = Image.fromarray(rgba.astype(np.uint8))
    im = im.transform((W2, H2), Image.AFFINE,
                      (1 / sk, 0, hx - (ox + PADX) / sk, 0, 1 / sk, hy - (oy + PAD) / sk), resample=Image.BICUBIC)
    return np.array(im).astype(float), sk

if __name__ == '__main__':
    N = numerowane()
    klienci = {1: 'ola', 2: 'karol', 3: 'ewa', 4: 'franek', 5: 'stefan'}
    style = {6: 'krotkie', 7: 'dlugie', 8: 'kucyki', 9: 'kok', 10: 'warkocze', 11: 'irokez'}
    for k, nazwa in klienci.items():
        rgb = np.array(Image.open(N[k]).convert('RGB'))
        assert rgb.shape[:2] == (H, W), rgb.shape
        zapisz(np.pad(np.dstack([rgb, usun_tlo(rgb)]), ((PAD, 0), (PADX, PADX), (0, 0))), 'klient-' + nazwa)
    wzor = miary(np.array(Image.open(N[1]).convert('RGB')))
    for k, nazwa in style.items():
        rgb = np.array(Image.open(N[k]).convert('RGB'))
        wl, gu, jest = wytnij_wlosy(rgb)
        m = miary(rgb)
        wl, sk = dopasuj(wl, m, wzor)
        gu, _ = dopasuj(gu, m, wzor)
        print(nazwa, 'skala', round(sk, 3))
        zapisz(wl, 'wlosy-' + nazwa)
        if jest:
            zapisz(gu, 'gumki-' + nazwa)
    # Zosia, kot, fartuszek z arkusza (już wycięte)
    for n in ['zosia', 'kot', 'fartuszek']:
        im = Image.open(f'{SRC}/{n}.png').convert('RGBA')
        zapisz(np.array(im), n, rozmiar=None)
