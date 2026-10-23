## 2026-10-23 18:51 — Pomysł i fabuła gry "Salon fryzjerski u Zosi"
- Zrobione: Róża (6 lat) chce zrobić pierwszą grę na iPada. Odpowiedziała na 6 pytań o fabułę. Ułożona fabuła i prosta mapa 6 ekranów.
- Zmienione pliki: cukier/STAN.md, cukier/LOG.md (nowe).
- Decyzje: bohaterka Zosia, salon w centrum Poznania; mycie, farbowanie, fryzury; atrakcje: zwierzak w salonie, konkurs fryzur w Poznaniu, zepsuty suszarko-robot; nagroda: nowy fartuszek.
- Niedokończone / ryzyka: nie wybrano jeszcze narzędzia do zrobienia gry; brak grafik.
- Następny krok: wybrać technologię (rekomendacja: wersja w przeglądarce, działa na iPadzie) i zrobić pierwszy ekran (start + klient wchodzi).

## 2026-10-23 19:13 — Zbudowanie całej gry i publikacja
- Zrobione: wszystkie 6 ekranów (start, klient wchodzi, mycie, farbowanie, fryzura+suszarko-robot, finał z gwiazdkami i fartuszkiem), kot w salonie, dźwięki (Web Audio) + głos iPada (pl-PL). Publikacja na GitHub Pages, użytkownik potwierdził, że działa.
- Zmienione pliki: index.html (nowy, cała gra), cukier/STAN.md, cukier/LOG.md.
- Decyzje: technologia = HTML w przeglądarce; grafiki = SVG-zaślepki; repo publiczne + Pages (link na iPada).
- Niedokończone / ryzyka: gra nieprzetestowana z Różą na iPadzie; konkurs fryzur to tylko napis w finale; brak zapisu postępów; grafiki to zaślepki.
- Następny krok: zagrać z Różą na iPadzie, zebrać jej uwagi i poprawić.

## 2026-10-23 20:13 — Grafiki z ChatGPT, tło z ladą, nazwa i ikona
- Zrobione: poprawa postaci SVG, PWA (manifest, service worker, offline), guzik Graj wyżej; potem podmiana na grafiki z ChatGPT (5 klientów łysych + 6 warstw włosów kolorowanych w canvasie, Zosia, kot, fartuszek), tło salonu + lada jako przód (postacie stoją za ladą), nazwa „Salon u Róży”, ikona PWA = róża. Wszystko wysłane na GitHub Pages.
- Zmienione pliki: index.html, sw.js (v5), manifest.json, ikony, img/ (18 plików WebP, 608 KB), narzedzia/przygotuj_grafiki.py, .gitignore (grafiki/ poza gitem).
- Decyzje: grafiki generowane w ChatGPT (włosy jako osobne szare warstwy, dopasowane skalą do głowy bazowej); gra nazywa się „Salon u Róży” (bohaterka nadal Zosia); ikona = róża rysowana kodem.
- Niedokończone / ryzyka: Zosia tylko ~270 px (miękka na retinie); ekrany 3–5 mają gradienty zamiast tła, robot to emoji; nic nie było klikane na żywo (tylko zrzuty); na iPadzie trzeba usunąć starą ikonę i dodać grę od nowa; konkurs fryzur to tylko napis.
- Następny krok: zagrać z Różą na iPadzie, spisać jej uwagi i poprawić.
