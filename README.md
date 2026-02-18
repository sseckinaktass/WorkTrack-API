WorkTrack-API 🤖📋

WorkTrack API, çalışanların giriş ve çıkış kayıtlarını takip etmek için geliştirilmiş, FastAPI ve PostgreSQL tabanlı bir mikroservis API’sidir. Çalışan ekleme, giriş/çıkış kaydı ve basit raporlama işlevleri sunar.

🛠 Teknolojiler

Python 3.10+

FastAPI

SQLAlchemy

Pydantic

PostgreSQL

🧪 Kurulum
1. Repo'yu klonlayın
git clone https://github.com/YOUR_USERNAME/WorkTrack-API.git
cd WorkTrack-API

2. Sanal ortam oluşturun ve bağımlılıkları yükleyin
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
pip install -r requirements.txt

3. .env dosyasını oluşturun
DATABASE_URL=postgresql://seckinaktas@localhost:5432/db_work

4. Uygulamayı çalıştırın
uvicorn main:app --reload

📬 API Uç Noktaları
Çalışan Ekle

POST /employees/
Body (JSON):

{
  "first_name": "Seçkin",
  "last_name": "Aktaş",
  "email": "seckin@example.com",
  "department": "Yazılım"
}

Giriş/Çıkış Kaydı Ekle

POST /attendance/
Body (JSON):

{
  "employee_id": 1,
  "check_type": "IN",
  "check_time": "2026-02-18T09:00:00",
  "device_id": "samsung"
}

👀 Veritabanı Yapısı

employees → Çalışan bilgileri

attendance_logs → Giriş/Çıkış kayıtları

NOT: check_type alanı IN veya OUT olmalıdır (PostgreSQL CHECK constraint ile kontrol edilir).

🧠 Author

Seçkin Aktaş
Software Engineer | AI & Computer Vision Enthusiast
GitHub
 • LinkedIn

📜 License

MIT
