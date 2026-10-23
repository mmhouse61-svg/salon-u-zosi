# Stan projektu: Gra "Salon u Róży"
Zaktualizowano: 2026-10-23 20:40

## Kierunek
Pierwsza gra na iPada 6-letniej Róży (rodzinny projekt, nauka i zabawa, nie biznes). Cel: prosta, grywalna gra o salonie fryzjerskim, którą Róża współtworzy swoimi pomysłami.

## Gdzie jesteśmy
- Gra opublikowana (jeden `index.html` + `img/`): repo github.com/mmhouse61-svg/salon-u-zosi (publiczne), link: https://mmhouse61-svg.github.io/salon-u-zosi/. Działa jako PWA (offline po 1. wejściu).
- Tła z ChatGPT na ekranach 3–5 (mycie, farbowanie, fryzura); robot-suszarka to grafika (zepsuty/naprawiony), nie emoji. SW v8.
- 6 ekranów: start, klient wchodzi (tło salonu, postacie za ladą), mycie (prysznic), farbowanie (10 kolorów), fryzura (naprawa suszarko-robota + 6 fryzur), finał (do 4 gwiazdek, fartuszek, konfetti).
- Grafiki z ChatGPT (WebP, 608 KB): 5 klientów, osobne warstwy włosów kolorowane w canvasie, Zosia, kot, fartuszek, tło + lada. Dźwięki: 6 próbek z ElevenLabs (snd/*.mp3: miau, prysznic, suszarka, nożyczki, robot, brawa) + synteza jako zapas + głos iPada po polsku.
- Aktualizacja: edytuj index.html, `git commit`, `git push` (zgoda na gh w `.claude/settings.local.json`).
- Nowe grafiki: oryginały w `grafiki/` (poza gitem), skrypt `narzedzia/przygotuj_grafiki.py` (wymaga pillow, numpy, scipy).
- Nic nie było klikane na żywo, tylko zrzuty z przeglądarki.

## Następny krok
1. Zagrać z Różą na iPadzie (usunąć starą ikonę, dodać grę od nowa z Safari), spisać jej uwagi.
2. Poprawki z jej uwag.
3. Potem: Zosia w większym rozmiarze, ewentualnie prawdziwy konkurs fryzur, prawdziwe głosy postaci.

## Decyzje
- 2026-10-23 — Bohaterka: Zosia, salon w Poznaniu — wybór Róży.
- 2026-10-23 — Mechaniki: mycie, farbowanie, fryzury — wybór Róży.
- 2026-10-23 — Atrakcje: zwierzak, konkurs fryzur, zepsuty suszarko-robot — wybór Róży.
- 2026-10-23 — Zakończenie: nowy fartuszek — wybór Róży.
- 2026-10-23 — Technologia: HTML w przeglądarce (PWA) — iPad bez App Store.
- 2026-10-23 — Publikacja: repo publiczne + GitHub Pages — darmowy link.
- 2026-10-23 — Grafiki: generowane w ChatGPT; włosy jako osobne szare warstwy — farbowanie i fryzury działają na każdym kliencie.
- 2026-10-23 — Nazwa gry: „Salon u Róży” (wybór użytkownika); bohaterka nadal Zosia.
- 2026-10-23 — Ikona PWA: róża.

- 2026-10-23 — Dźwięki: próbki ElevenLabs w repo (snd/), ok. 100 kredytów — żywszy salon dla Róży.

## Parking pomysłów
- Czarodziejska farba (tęcza, brokat, gwiazdki).
- Koziołki z Ratusza jako klienci z "koziołkową fryzurą".
- Prawdziwe głosy postaci z ElevenLabs (kosztuje kredyty; efekty dźwiękowe już są).
- Rysunki Róży zamiast generowanych.
- Zapis postępów.

## Blokery / pytania do użytkownika
- Konkurs fryzur: osobna rozgrywka, czy zostaje napis w finale?
- Strażnik: sesja była bardzo długa i rozrosła się (poprawki SVG, potem zmiana na grafiki ChatGPT); gra wciąż nie przeszła testu z Różą na iPadzie, więc dalsze ozdoby warto robić dopiero po jej uwagach.
