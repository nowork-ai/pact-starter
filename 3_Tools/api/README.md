# API klice — nastaveni

> Aby tvoje PACT nastroje fungovaly, potrebujes API klice. Tady je navod jak je ziskat.

---

## 1. OpenRouter (doporuceny start)

**Co to je:** Jedna brana ke stovkam AI modelu. Jeden API klic = pristup ke Claude, GPT, Gemini, Llama, Mistral a dalsim 300+ modelum. Nemusis mit ucet u kazdeho poskytovatele zvlast.

**Proc OpenRouter:**
- Jeden klic, vsechny modely
- Free tier: 25+ modelu zdarma (50 requestu/den)
- Pay-as-you-go: platís jen za to, co pouzíjes (5.5% poplatek, zadny mesicni pausal)
- Muzes vyzkouset ruzne modely a vybrat si ten nejlepsi pro tvuj use case

### Jak ziskat klic

1. Jdi na [openrouter.ai](https://openrouter.ai)
2. Klikni **Sign Up** (staci Google ucet)
3. Po prihlaseni jdi do **Keys** (leva strana)
4. Klikni **Create Key**
5. Pojmenuj ho (napr. "PACT")
6. Zkopiruj klic (zacina na `sk-or-...`)

### Kam ho ulozit

Vytvor soubor `3_Tools/api/openrouter-api.txt` a vloz do nej klic:

```
sk-or-tvuj-klic-tady
```

> **Dulezite:** Tento soubor NIKDY nedavej do Gitu ani nesdilej. Je to tvuj osobni pristupovy klic.

### Jak to otestovat

V Cursoru otevri terminal a spust:

```bash
curl https://openrouter.ai/api/v1/models \
  -H "Authorization: Bearer $(cat 3_Tools/api/openrouter-api.txt)" \
  | python3 -m json.tool | head -20
```

Pokud vidis JSON se seznamem modelu, funguje to.

### Doporucene modely pro zacatek

| Use case | Model | Poznamka |
|----------|-------|----------|
| Univerzalni | `anthropic/claude-sonnet-4` | Nejlepsi pomer cena/vykon |
| Rychle ukoly | `google/gemini-2.5-flash` | Rychly, levny |
| Slozite analyzy | `anthropic/claude-sonnet-4` | Nejlepsi reasoning |
| Coding | `anthropic/claude-sonnet-4` | Nejlepsi pro kod |
| Kreativni psani | `openai/gpt-4.1` | Dobry pro text |
| **Zdarma** | `openrouter/free` | Nahodny free model, 0 Kc |

> Modely se rychle meni. Aktualni seznam: [openrouter.ai/models](https://openrouter.ai/models)

---

## 2. OpenAI API (volitelne)

**Kdy potrebujes:** Pokud chces prepisovat audio/video (transkripce). Model `gpt-4o-transcribe` je nejlepsi na prepis reci a je dostupny jen pres OpenAI API, ne pres OpenRouter.

### Jak ziskat klic

1. Jdi na [platform.openai.com](https://platform.openai.com)
2. Prihlás se nebo vytvor ucet
3. Jdi do **API Keys**
4. Klikni **Create new secret key**
5. Zkopiruj klic (zacina na `sk-...`)

### Kam ho ulozit

```
3_Tools/api/openai-api.txt
```

### Cena

- Audio prepis: cca $0.006 / minuta (6 centů za minutu)
- 1 hodina podcastu = cca $0.36 (9 Kc)

---

## 3. Apify (volitelne)

**Co to je:** Platforma pro web scraping a automatizaci. Muzes stahnout obsah jakekoli webove stranky, extrahovat LinkedIn profily, monitorovat zmeny na webech, a dalsi.

**Proc Apify:**
- Free tier: 5 USD kredit mesicne (staci na stovky scrape)
- Hotove "Actors" — predpripravene scripty na bezne ukoly
- Zadny vlastni server — vsechno bezi v cloudu

### Jak ziskat klic

1. Jdi na [apify.com](https://apify.com)
2. Klikni **Sign Up** (staci Google ucet)
3. Po prihlaseni jdi do **Settings** → **Integrations**
4. Zkopiruj **Personal API token**

### Kam ho ulozit

```
3_Tools/api/apify-api.txt
```

---

## Prehled

| Sluzba | Co dava | Free tier | Klic ulozit do |
|--------|---------|-----------|----------------|
| **OpenRouter** | 300+ AI modelu (text, analyza, kod) | 25+ modelu, 50 req/den | `openrouter-api.txt` |
| **OpenAI** | Audio prepis (transkripce) | — (pay-as-you-go) | `openai-api.txt` |
| **Apify** | Web scraping, automatizace | 5 USD/mesic kredit | `apify-api.txt` |

---

## Bezpecnost

- API klice jsou jako hesla — **nesdilej je**
- Soubory s klici (`*-api.txt`) pridej do `.gitignore`
- Pokud klic unikne, okamzite ho zrus a vytvor novy
- Pro sdileni projektu pouzij `.env.example` bez skutecnych klicu
