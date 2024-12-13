# Online Store

Bu Django asosida ishlab chiqilgan online do'kon loyihasi bo'lib, foydalanuvchilar uchun mahsulotlarni ko'rish, xarid qilish, va buyurtmalarni boshqarish imkoniyatini beradi.

## Loyihaning asosiy funksiyalari
- Mahsulotlarni katalog shaklida ko'rish.
- Foydalanuvchilar uchun ro'yxatdan o'tish va tizimga kirish.
- Mahsulotlarni savatchaga qo'shish.
- Buyurtma qilish va buyurtma tarixi bilan tanishish.

## Texnologiyalar
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)
- **Ma'lumotlar bazasi:** SQLite (standart), boshqa DB-lar uchun sozlash mumkin
- **API:** Django REST Framework (agar ishlatilgan bo'lsa)

## O'rnatish bo'yicha yo'riqnoma
1. Repository’ni klonlash:
   ```bash
   git clone https://github.com/AbdusattarovOtabek/Online-shopping.git
   ```
2. Virtual muhitni yaratish va faollashtirish:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows uchun: env\Scripts\activate
   ```
3. Kerakli kutubxonalarni o'rnatish:
   ```bash
   pip install -r requirements.txt
   ```
4. Ma'lumotlar bazasini yaratish:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Super foydalanuvchi yaratish:
   ```bash
   python manage.py createsuperuser
   ```
6. Serverni ishga tushirish:
   ```bash
   python manage.py runserver
   ```

## Foydalanish
- Loyihani lokal serverda ishga tushirgandan so'ng, brauzer orqali [http://127.0.0.1:8000](http://127.0.0.1:8000) manziliga o'ting.
- Admin panelga kirish uchun [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) manzilidan foydalaning.

## Qo'shimcha imkoniyatlar
- **Responsive dizayn:** Har qanday qurilmaga moslashgan foydalanuvchi interfeysi.
- **Modulli arxitektura:** Keyingi funksiyalarni qo'shish va yangilash oson.

## Hissa qo'shish
- Pull requestlar ochiq.
- Har qanday xato yoki taklif haqida [Issues](https://github.com/AbdusattarovOtabek/Django-App/issues) bo'limida xabar qoldiring.

## Litsenziya
Bu loyiha [MIT litsenziyasi](LICENSE) asosida tarqatiladi. Tafsilotlar uchun LICENSE faylini ko'ring.

## Muallif
- **Otabek Abdusattarov**
