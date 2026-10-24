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

## 2026-10-23 20:50 — Monety, zapis, sklepik, życzenia klientów
- Zrobione: monety (2 za gwiazdkę), zapis w localStorage (monety, zakupy, fartuszek), sklepik (farby: Złoty 8, Tęcza 12, Brokat 16; ozdoby kota: kokardka 6, cylinder 10, korona 12), życzenia klientów (kolor + fryzura, +3 monety za każde trafione). Wypchnięte na GitHub Pages.
- Zmienione pliki: index.html, sw.js (v10), cukier/STAN.md, cukier/LOG.md.
- Decyzje: nagrody kosmetyczne bez kar i liczników czasu (6-latka); zakupy bez nowych grafik (emoji + kod); użytkownik potwierdził, że ekrany działają na iPadzie poziomo.
- Niedokończone / ryzyka: tylko zrzuty z przeglądarki, nie przeklikane na żywo; pozycja ozdoby na kocie ustawiona na oko; Róża nie widziała jeszcze sklepiku ani życzeń.
- Następny krok: Róża gra ~15 min, spisać jej uwagi (co by kupiła, czy rozumie etykietę życzenia), poprawki.

## 2026-10-24 19:01 — Animacje, nowe towary sklepiku, reset postępów
- Zrobione: ożywienie gry (oddychające postacie, krok wejścia, podskok po dotknięciu, iskry, bańki w myciu, fala koloru, nożyczki + dmuchanie suszarki, taniec robota i klienta w finale, ptaki/chmury w oknie, blask lamp, sekundnik); sklepik +3 farby (Srebrny 6, Zachód 14, Galaktyka 18) i +3 ozdoby kota (Kwiatek 5, Czapka 9, Różek 15); reset postępów w sklepiku z pytaniem „Na pewno?”. Wszystko wypchnięte na GitHub Pages.
- Zmienione pliki: index.html, sw.js (v13), cukier/STAN.md, cukier/LOG.md.
- Decyzje: animacje na prośbę Róży („nudne”), czysty kod bez nowych grafik; farby z przejściem kolorów w słowniku GRADIENTY; reset schowany jako mały napis + potwierdzenie (ochrona przed 6-latką).
- Niedokończone / ryzyka: nic nie klikane na żywo (tylko składnia JS); animacje mogą być za mocne/za słabe na iPadzie; położenie okna/lamp/zegara liczone z obrazka tła; „blokery” zrozumiane jako „bajery”.
- Następny krok: Róża gra ~15 min, spisać uwagi, poprawić tempo/siłę efektów.
