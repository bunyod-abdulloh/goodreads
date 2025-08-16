📚 Goodreads Clone

Goodreads saytining soddalashtirilgan kloni (Django asosida).
Loyiha kitoblarni boshqarish, foydalanuvchilarni ro‘yxatdan o‘tkazish, login qilish va o‘zaro fikr almashish imkonini beradi.

✨ Texnologiyalar

Backend: Django 5, Python 3.12

Frontend: HTML5, CSS3, Bootstrap 5, JavaScript

Database: PostgreSQL

Template engine: Django Templates

Version Control: Git + GitHub

⚙️ O‘rnatish
1. Repository’ni clone qilish
git clone https://github.com/bunyod-abdulloh/goodreads.git
cd goodreads

2. Virtual environment yaratish
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows (PowerShell)

3. Kerakli paketlarni o‘rnatish
pip install -r requirements.txt

4. .env fayl yaratish
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=goodreads
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

5. Ma’lumotlar bazasini sozlash
python manage.py makemigrations
python manage.py migrate

6. Admin foydalanuvchi yaratish
python manage.py createsuperuser

7. Serverni ishga tushirish
python manage.py runserver

📖 Asosiy funksiyalar

Foydalanuvchilarni ro‘yxatdan o‘tkazish va login qilish

Kitob qo‘shish, tahrirlash va o‘chirish

Kitoblar ro‘yxati va tafsilot sahifasi

Bootstrap yordamida zamonaviy UI

Django ORM orqali PostgreSQL bilan ishlash

📂 Loyihaning tuzilishi
goodreads/
├── goodreads/         # Asosiy konfiguratsiya
├── users/             # Foydalanuvchi autentifikatsiyasi (login/register)
├── books/             # Kitoblarni boshqarish
├── templates/         # HTML shablonlari
├── static/            # CSS, JS, Bootstrap, images
├── manage.py
└── requirements.txt

🚀 Kelajak rejalar

📌 Kitoblarga izoh qoldirish

📌 Reyting tizimi (⭐️⭐️⭐️⭐️⭐️)

📌 API (Django REST Framework orqali)

📌 Docker qo‘llab-quvvatlash

🤝 Hissa qo‘shish

Pull request’lar va yangi g‘oyalar mamnuniyat bilan qabul qilinadi!

📜 Litsenziya

MIT License — erkin foydalanishingiz mumkin.
