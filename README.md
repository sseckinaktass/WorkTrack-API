# WorkTrack-API 🤖📋

WorkTrack API, çalışanların giriş ve çıkış kayıtlarını takip etmek için geliştirilmiş bir FastAPI + PostgreSQL mikroservisidir.

---

## 🛠 Teknolojiler

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
