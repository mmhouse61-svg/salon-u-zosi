# Stan projektu: Gra "Salon u Róży"
Zaktualizowano: 2026-10-23 20:50

## Kierunek
Pierwsza gra na iPada 6-letniej Róży (rodzinny projekt, nauka i zabawa, nie biznes). Cel: prosta, grywalna gra o salonie fryzjerskim, którą Róża współtworzy swoimi pomysłami.

## Gdzie jesteśmy
- Gra opublikowana (jeden `index.html` + `img/`): repo github.com/mmhouse61-svg/salon-u-zosi (publiczne), link: https://mmhouse61-svg.github.io/salon-u-zosi/. Działa jako PWA (offline po 1. wejściu).
- Tła z ChatGPT na ekranach 3–5 (mycie, farbowanie, fryzura); robot-suszarka to grafika (zepsuty/naprawiony), nie emoji. SW v8.
- 6 ekranów: start, klient wchodzi (tło salonu, postacie za ladą), mycie (prysznic), farbowanie (10 kolorów), fryzura (naprawa suszarko-robota + 6 fryzur), finał (do 4 gwiazdek, fartuszek, konfetti).
- Grafiki z ChatGPT (WebP, 608 KB): 5 klientów, osobne warstwy włosów kolorowane w canvasie, Zosia, kot, fartuszek, tło + lada. Dźwięki: 6 próbek z ElevenLabs (snd/*.mp3: miau, prysznic, suszarka, nożyczki, robot, brawa) + synteza jako zapas + głos iPada po polsku.
- Aktualizacja: edytuj index.html, `git commit`, `git push` (zgoda na gh w `.claude/settings.local.json`).
- Nowe grafiki: oryginały w `grafiki/` (poza gitem), skrypt `narzedzia/przygotuj_grafiki.py` (wymaga pillow, numpy, scipy).
- Rozgrywka (SW v10): monety (2 za gwiazdkę), zapis w localStorage, sklepik (farby Złoty/Tęcza/Brokat, ozdoby kota kokardka/cylinder/korona), życzenia klientów (kolor + fryzura, +3 monety za trafienie). Użytkownik potwierdził: ekrany działają na iPadzie poziomo.
- Nowe rzeczy (sklepik, życzenia) oglądane tylko na zrzutach z przeglądarki; Róża ich jeszcze nie widziała.

## Następny krok
1. Róża gra ~15 min na iPadzie (usunąć starą ikonę, dodać grę od nowa), spisać uwagi: co by kupiła, czy rozumie etykietę życzenia, czy ozdoba siedzi na głowie kota.
2. Poprawki z jej uwag (pozycja ozdoby kota, ceny, czytelność).
3. Potem: prawdziwy Konkurs Fryzur, Koziołki z Ratusza, Zosia w większym rozmiarze.

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
- 2026-10-23 — Rozgrywka: monety + sklepik kosmetyczny + życzenia klientów, bez kar i liczników czasu — grywalność dla 6-latki.

## Parking pomysłów
- Czarodziejska farba (tęcza, brokat, gwiazdki).
- Koziołki z Ratusza jako klienci z "koziołkową fryzurą".
- Prawdziwe głosy postaci z ElevenLabs (kosztuje kredyty; efekty dźwiękowe już są).
- Rysunki Róży zamiast generowanych.

## Blokery / pytania do użytkownika
- Konkurs fryzur: osobna rozgrywka, czy zostaje napis w finale?
- Strażnik: w tej sesji dodano dwie warstwy rozgrywki (sklepik, życzenia) na polecenie użytkownika, ale Róża jeszcze ich nie widziała. Kolejne dodatki tylko po jej uwagach.
