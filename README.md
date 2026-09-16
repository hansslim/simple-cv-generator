# Simple CV Generator

Jednoduchý open-source webový editor strukturovaného životopisu navržený pro přímý export a tisk do formátu A4. Funguje čistě na straně klienta – bez backendu, registrace a odesílání dat na vzdálené servery.

## Přehled funkcí

- **Lokální zpracování**: Všechna data zůstávají v prohlížeči. Aplikace neposílá žádné požadavky na externí servery.
- **Tisk na A4**: Pevně definované rozvržení pro jedno i dvoustránkový životopis. Možnost určit přesné místo rozdělení stránek.
- **Dva způsoby úprav**: Data lze zadávat přes formulář v levém panelu nebo přímým kliknutím a vepsáním do pravého náhledu.
- **Práce se soubory (JSON)**: Možnost exportu a importu rozpracovaného stavu pro pozdější úpravy.
- **Uspořádání obsahu**: Pořadí sekcí, kontaktů i jednotlivých položek praxe a vzdělání lze měnit tažením myši nebo tlačítky.
- **Vykreslování**: Nevyplněné údaje, prázdné položky ani nepoužité sekce se do výsledného dokumentu nepromítnou.
- **Vzhled a proporce**: Nastavení hlavní barvy, měřítka písma, šířky levého sloupce i odsazení záhlaví.

## Spuštění

Aplikace nevyžaduje instalaci balíčků ani buildovací nástroje.

1. Naklonujte repozitář:
   ```bash
   git clone https://github.com/hansslim/simple-cv-generator.git
   ```
2. Otevřete `index.html` v prohlížeči (Chrome, Firefox, Edge, Safari apod.).

## Doporučený postup při tvorbě CV

1. **Vyplnění dat**: Vyplňte základní údaje a rozbalte sekce, které chcete v životopisu mít.
2. **Přizpůsobení délky**: Pokud se obsah nevejde přesně na jednu stranu, můžete v horní liště upravit měřítko dokumentu (např. 110–125 %) nebo kliknutím na symbol nůžek určit, kde přesně má začínat druhá strana.
3. **Záloha**: Před zavřením prohlížeče si stav uložte tlačítkem **Export JSON**.
4. **Export do PDF**:
   - Klikněte na **Tisk do PDF** (nebo použijte zkratku `Ctrl+P` / `Cmd+P`).
   - Cíl tisku nastavte na **Uložit jako PDF**.
   - Formát papíru zvolte **A4**.
   - Okraje nastavte na **Výchozí** nebo **Žádné**.
   - Zapněte volbu **Grafika na pozadí**.

## Technologie

- Vue.js 3 (Composition API načítané přes CDN)
- HTML5, standardní CSS3 (CSS Variables, Flexbox, Grid, Media query `@media print`)

## Licence

MIT (vibecoded by Gemini 3.7 Flash)
