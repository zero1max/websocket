# WebSocket Chat Server

Bu loyiha **FastAPI va WebSocket** yordamida real vaqt rejimida ishlaydigan **chat serveri** hisoblanadi. U foydalanuvchilarga bir-birlari bilan xabar almashish imkonini beradi.

---

## 🚀 Loyiha imkoniyatlari
- WebSocket orqali real vaqt chat
- Xususiy (shaxsiy) va umumiy (barcha foydalanuvchilar uchun) xabarlarni yuborish
- Foydalanuvchilarning tizimga kirishi va chiqishini kuzatish

---

## 📌 Talablar
Loyihani ishga tushirishdan oldin quyidagi dasturlar kompyuteringizda o‘rnatilgan bo‘lishi kerak:
- **Python 3.8 yoki undan yuqori versiya**
- **pip** (Python kutubxona boshqaruvchisi)

---

## 📥 O'rnatish

### 1. Loyihani yuklab olish
```sh
# GitHub dan klonlash
git clone https://github.com/username/websocket-chat.git
cd websocket-chat
```

### 2. Virtual muhit yaratish va faollashtirish
```sh
# Windows
python -m venv venv
venv\Scripts\activate

# MacOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Kerakli kutubxonalarni o‘rnatish
```sh
pip install -r requirements.txt
```

Agar siz **Windows** foydalanuvchisi bo‘lsangiz, **uvloop** muammosi bo‘lishi mumkin. Uni o‘rnatish shart emas, shuning uchun quyidagi buyruq bilan davom eting:
```sh
pip install -r requirements.txt --no-deps uvloop
```

---

## 🚀 Serverni ishga tushirish
Loyihani ishga tushirish uchun quyidagi buyruqdan foydalaning:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

Agar server to‘g‘ri ishga tushgan bo‘lsa, quyidagicha chiqish paydo bo‘ladi:
```sh
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

---

## 🔌 Postman yordamida WebSocket ulanishini sinash
1. **Postman'ni oching** va "New Request" tugmasini bosing.
2. **Request turini** `WebSocket` qilib tanlang.
3. URL maydoniga quyidagini kiriting:
   ```
   ws://localhost:8000/ws/user1
   ```
   (`user1` o‘rniga o‘zingiz xohlagan foydalanuvchi ID ni yozishingiz mumkin.)
4. **Connect tugmasini bosing**.
5. Xabar yuborish uchun quyidagi JSON formatidan foydalaning:
   ```json
   { "message": "Salom hammaga!", "to_user": "" }
   ```
   Agar **bitta foydalanuvchiga xabar yuborish** kerak bo‘lsa:
   ```json
   { "message": "Salom, user2!", "to_user": "user2" }
   ```
6. **Send tugmasini bosing** va serverdan kelayotgan javoblarni kuzating.

---

## 📜 Foydalanish
Loyihada **WebSocket** ishlatilgan bo‘lib, foydalanuvchilar real vaqt rejimida xabar almashishlari mumkin:
- Agar foydalanuvchi tizimga kirsа, barcha ulanishlarga **"User X joined the chat"** degan xabar yuboriladi.
- Agar foydalanuvchi chiqib ketsa, **"User X left the chat"** deb e'lon qilinadi.
- Agar foydalanuvchi shaxsiy xabar jo‘natsa, faqat belgilangan qabul qiluvchi uni ko‘radi.

---

## 🛠 Muammo va yechimlar
### 1. `uvloop` Windows'da o‘rnatilmayapti
**Yechim:** `requirements.txt` dan `uvloop` ni olib tashlang yoki quyidagi buyruqni ishlating:
```sh
pip install -r requirements.txt --no-deps uvloop
```

### 2. `port 8000 is already in use`
**Yechim:** Avvalgi ishlayotgan serverni topish va o‘chirish kerak:
```sh
# Windows
netstat -ano | findstr :8000
# So‘ng process ID (PID) bo‘yicha o‘chirish
Taskkill /PID <PID> /F

# Linux/MacOS
lsof -i :8000
kill -9 <PID>
```

---

## 📝 Litsenziya
Bu loyiha **MIT** litsenziyasi asosida tarqatiladi.

---

✅ **Muallif:** [Your Name]  
✅ **GitHub:** [Your GitHub Link]  
✅ **Loyiha Statusi:** Ishlaydi 🚀

