# 📚 Goodreads Clone

Goodreads saytining soddalashtirilgan kloni (Django asosida).  
Loyiha kitoblarni boshqarish, foydalanuvchilarni ro‘yxatdan o‘tkazish, login qilish va o‘zaro fikr almashish imkonini beradi.  

---

## ✨ Texnologiyalar
- **Backend:** Django 5, Python 3.12
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript
- **Database:** PostgreSQL
- **Template engine:** Django Templates
- **Version Control:** Git + GitHub

---

## ⚙️ O‘rnatish

### 1. Repository’ni clone qilish
```bash
git clone https://github.com/bunyod-abdulloh/goodreads.git
cd goodreads

### 2. Virtual environment yaratish
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows (PowerShell)

### 3. Kerakli paketlarni o‘rnatish
```bash
pip install -r requirements.txt

### 4. .env fayl yaratish
```bash
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_NAME=goodreads
DATABASE_USER=postgres
DATABASE_PASSWORD=your_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

### 5. Ma’lumotlar bazasini sozlash
```bash
python manage.py makemigrations
python manage.py migrate

### 6. Admin foydalanuvchi yaratish
```bash
python manage.py createsuperuser

### 7. Serverni ishga tushirish
```bash
python manage.py runserver
