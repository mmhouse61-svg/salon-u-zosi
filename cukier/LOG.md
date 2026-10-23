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

## 2026-10-23 20:40 — Dźwięki ElevenLabs, tła ekranów 3–5, grafika robota
- Zrobione: 6 dźwięków z ElevenLabs (miau, prysznic w pętli, suszarka, nożyczki, robot, brawa) wpięte w Dzwiek z zapasem syntezowanym; tła mycia, farbowania i fryzury z ChatGPT; robot w 2 stanach (zepsuty/naprawiony) wycięty z grafiki, zamiast emoji. Wszystko wypchnięte na GitHub Pages.
- Zmienione pliki: index.html, sw.js (v8), snd/*.mp3 (6), img/tlo-mycie|farbowanie|fryzura.webp, img/robot-zepsuty|dziala.webp.
- Decyzje: próbki ładowane przez Web Audio (pętla prysznica, suszarka 2 s po wyborze fryzury); tła jako CSS cover przy dole.
- Niedokończone / ryzyka: nic nie klikane na żywo (tylko parsowanie JS); suszarka to 1 s zapętlona, może mieć szew; robot może zasłaniać się z wózkiem z tła; na iPadzie trzeba usunąć starą ikonę i dodać grę od nowa.
- Następny krok: zagrać z Różą na iPadzie, spisać uwagi, poprawić.
