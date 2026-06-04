# 🏦 UZCARD Academy — Python kursi

Bu repository **UZCARD Academy** Python kursi bo'yicha dars materiallari, uy vazifalari va yechimlarini o'z ichiga oladi.

---

## 📚 Kurs haqida

**UZCARD Academy** — to'lov tizimi sohasida ishlash uchun mo'ljallangan amaliy Python kursi.
Kurs 2 blokdan iborat, har bir blok 13 darsni o'z ichiga oladi.

📄 To'liq kurs dasturi: [`UZCARD Academy.pdf`](./UZCARD%20Academy.pdf)

---

## 📁 Fayl tuzilishi

```
Uzcard-academy/
├── main.py                              # Blok 1 — dars yechimlari va quiz javoblari
├── week01_python_basics.ipynb           # Uy vazifasi 1: Tranzaksiya analitikasi
├── week02_uzcard_currency_service.ipynb # Uy vazifasi 2: Valyuta kurs servisi
├── UZCARD Academy.pdf                   # Kurs dasturi va materiallari
└── .gitignore
```

---

## 🗂️ Blok 1 — Python asoslari (13 dars)

### `main.py` — Dars yechimlari

| # | Dars mavzusi | Tur |
|---|-------------|-----|
| 4 | Loops & Tuples — approved tranzaksiyalar summasi | Quiz + Kod |
| 5 | Strings — karta raqamini maskalash | Quiz + Kod |
| 6 | Lists — eng katta 3 ta tranzaksiya | Quiz + Kod |
| 7 | dict, tuple, set — noyob valyutalar | Quiz + Kod |
| 8 | Funksiyalar — komissiya hisoblash | Quiz + Kod |
| 9 | \*args, \*\*kwargs, lambda — balans bo'yicha saralash | Quiz + Kod |
| 10 | Modullar, venv, pip | Quiz |
| 11 | Fayllar bilan ishlash — approved summa | Quiz + Kod |
| 12 | JSON — eng katta summali mijoz | Quiz + Kod |
| 13 | Xatoliklar va istisnolar — xavfsiz bo'lish | Quiz + Kod |

---

### 📓 Uy vazifalari

#### Vazifa 1: `week01_python_basics.ipynb` — Tranzaksiya analitikasi

25 ta tranzaksiya bo'yicha 6 ta funksiya yozish:

| Funksiya | Vazifa |
|----------|--------|
| `successful(txs)` | Faqat muvaffaqiyatli tranzaksiyalarni qaytaradi |
| `total_volume(txs)` | Umumiy aylanma summasi |
| `top_gateway_by_volume(txs)` | Eng ko'p pul o'tkazgan to'lov shlyuzi |
| `unique_merchants(txs)` | Noyob merchantlar soni |
| `top_merchant_by_count(txs)` | Eng faol merchant |
| `avg_amount_in_age_range(txs, lo, hi)` | Yosh oralig'i bo'yicha o'rtacha summa |

#### Vazifa 2: `week02_uzcard_currency_service.ipynb` — Valyuta kurs servisi

`api.frankfurter.dev` API orqali real valyuta kurslari bilan ishlash:

| Klass / Funksiya | Vazifa |
|-----------------|--------|
| `fetch_rates(url)` | API dan kurslarni yuklash |
| `Currency` | Bitta valyuta modeli (`__str__`, `__eq__`, `__hash__`) |
| `RateBook` | Valyutalar to'plami (dict-like interfeys) |
| `Converter` | To'g'ridan va kross-kurs hisoblash |
| `CachedRateBook` | Murojaat logi bilan RateBook |
| `TurboBook` | Diamond MRO — C3-linearizatsiya |

---

## 🚀 Ishga tushirish

```bash
# Virtual muhit yaratish
python3 -m venv .venv
source .venv/bin/activate

# Kutubxonalarni o'rnatish
pip install requests

# main.py ni ishga tushirish
python3 main.py

# Jupyter notebook ni ishga tushirish
jupyter notebook
```

---

## 🛠️ Texnologiyalar

- **Python 3.11**
- **requests** — HTTP so'rovlar uchun
- **json** — JSON bilan ishlash
- **Jupyter Notebook** — interaktiv darslar

---

## 👤 Muallif

**Ibroximjon**
- GitHub: [@Ibroximjon631](https://github.com/Ibroximjon631)
