// Service worker: najpierw sieć (świeże wersje gry), a offline bierze z pamięci podręcznej.
const WERSJA = 'salon-u-zosi-v12';
const PLIKI = ['./', 'index.html', 'manifest.json', 'icon-192.png', 'icon-512.png', 'apple-touch-icon.png',
  'img/fartuszek.webp',
  'img/gumki-kok.webp',
  'img/gumki-kucyki.webp',
  'img/klient-ewa.webp',
  'img/klient-franek.webp',
  'img/klient-karol.webp',
  'img/klient-ola.webp',
  'img/klient-stefan.webp',
  'img/kot.webp',
  'img/lada.webp',
  'img/tlo-salonu.webp', 'img/tlo-mycie.webp', 'img/tlo-fryzura.webp', 'img/robot-zepsuty.webp', 'img/robot-dziala.webp', 'img/tlo-farbowanie.webp',
  'img/wlosy-dlugie.webp',
  'img/wlosy-irokez.webp',
  'img/wlosy-kok.webp',
  'img/wlosy-krotkie.webp',
  'img/wlosy-kucyki.webp',
  'img/wlosy-warkocze.webp',
  'img/zosia.webp',
  'snd/miau.mp3', 'snd/prysznic.mp3', 'snd/suszarka.mp3', 'snd/nozyczki.mp3', 'snd/robot.mp3', 'snd/brawa.mp3'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(WERSJA).then(c => c.addAll(PLIKI)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys()
    .then(k => Promise.all(k.filter(n => n !== WERSJA).map(n => caches.delete(n))))
    .then(() => self.clients.claim()));
});
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(
    fetch(e.request)
      .then(r => { const kopia = r.clone(); caches.open(WERSJA).then(c => c.put(e.request, kopia)); return r; })
      .catch(() => caches.match(e.request).then(r => r || caches.match('index.html')))
  );
});
