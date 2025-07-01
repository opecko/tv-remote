# Remote-xdotool

Vzdálené ovládání počítače přes webové rozhraní (HTML stránku). Funguje na Linuxu s X11 (nefunguje na Waylandu), využívá `xdotool` pro simulaci stisků kláves.

## Autor
Vytvořil: @opecko (YouTube)

## Závislosti
- Python 3
- Flask (`pip install flask` nebo systémový balíček `python3-flask`)
- xdotool (`sudo apt install xdotool`)

## Instalace a spuštění
1. Ujistěte se, že máte nainstalované závislosti.
2. Spusťte server:
   ```bash
   python3 tv_remote.py
   ```
3. Otevřete webový prohlížeč a přejděte na adresu `http://<IP_adresa>:5000` (např. `http://localhost:5000`).

## Funkce
- Ovládání šipek, Enter, mezerník, Escape, zpět, hlasitost (nahoru/dolů)
- Zadávání textu přes webové rozhraní

## Bezpečnostní upozornění
- Skript umožňuje ovládat klávesnici počítače přes síť. Používejte pouze v důvěryhodné síti!
- Nedoporučuje se vystavovat server do veřejného internetu.

## Poznámky
- Funguje pouze na X11 (ne na Waylandu).
- Port lze změnit v souboru `tv_remote.py`.

---

Projekt je určen pro osobní použití a demonstraci.