# AI Auto Reply API 🤖📩

This project is a smart email auto-responder built with FastAPI and HuggingFace's zero-shot classification model.  
It detects the intent of incoming messages (like offers, meetings, or thank-you notes), checks user availability or leave status, and generates context-aware replies.

---

## 🚀 Features

- 📨 Intent detection using transformers (XLM-RoBERTa)
- 📅 Checks user availability and leave dates
- ⏰ Suggests free time slots based on user calendar
- 🧠 Smart auto-reply logic (for thank you, meetings, offers)
- ⚡ FastAPI backend

---

## 🛠 Technologies

- FastAPI
- Hugging Face Transformers
- Python 3.10+
- Pydantic
- JSON-based mock database

---

## 🧪 Kurulum

### 1. Repo'yu klonlayın
```bash
git clone https://github.com/YOUR_USERNAME/WorkTrack-API.git
cd WorkTrack-API
```

### 2. Sanal ortam oluşturun ve bağımlılıkları yükleyin
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
# venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### 3. .env dosyasını oluşturun
```bash
DATABASE_URL=postgresql://seckinaktas@localhost:5432/db_work
```

### 4. Uygulamayı çalıştırın
```bash
uvicorn main:app --reload
```

---

## 📬 API Uç Noktaları

1️⃣ Çalışan Ekle
POST /employees/
Body (JSON):
```json
{
  "first_name": "Seçkin",
  "last_name": "Aktaş",
  "email": "seckin@example.com",
  "department": "Yazılım"
}

```

---

2️⃣ Giriş/Çıkış Kaydı Ekle
POST /attendance/
Body (JSON):
```json
{
  "employee_id": 1,
  "check_type": "IN",
  "check_time": "2026-02-18T09:00:00",
  "device_id": "samsung"
}
```

Not: check_type alanı yalnızca "IN" veya "OUT" değerlerini alabilir (veritabanında CHECK constraint ile kontrol edilir).

---

## 🧠 Author

**Seçkin Aktaş**  
Software Engineer | AI & Computer Vision Enthusiast  
[GitHub](https://github.com/sseckinaktass) • [LinkedIn](https://www.linkedin.com/in/seckinaktas/)

---

## 📜 License

MIT
