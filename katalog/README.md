# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Nama            : Reza Taufiq Yahya

Kelas           : PBP C

NPM             : 2106654183

Heroku App Link : https://rezataufiq56.herokuapp.com/katalog/

## 1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;


<img src= katalog/image/Tugas2PBP.png width = "720" height = "720">

## 2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?


Saat kita menginstal modul/library menggunakan `pip` , modulnya akan terinstal secara global di `/user/lib/python3.9/site-packages`. Alasan memakai virtual environment, misal pada hari ini kita membuat proyek aplikasi menggunakan `django 1.1`.Aplikasi berjalan dengan sempurna menggunakan modul versi 1.1. Lalu beberapa waktu kemudian, django rilis versi baru. Anggaplah `versi 4.0`. Kita kemudian melakukan upgrade modul. Akan tetapi, aplikasi yang sudah kita buat tidak bisa berjalan dengan modul versi baru ini, karena banyak perubahan fungsi dan lain-lain. Sementara itu, ada proyek aplikasi lain yang diharuskan menggunakan modul versi itu. Karena itu… kita membutuhkan `virtualenv`, agar masing-masing aplikasi memiliki modulnya sendiri.

Bisa, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan *virtual environment*.

## 3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.


Poin 1 : Pada poin 1 saya membuat fungsi yang bernama   `show_katalog` dengan parameter request. terdapat variable context yang merupakan dict. Dan mereturn parameter request, variable context berupa dict, dan templates `katalog.html`


Poin 2 : Cara saya membuat routing untuk memetakan fungsi yang telah dibuat pada `views.py` adalah dengan cara menggunakan fungsi `path` lalu mengonfigurasi `urls.py` dari App Django dengan menyertakan `include()` dan jangan lupa mengimpornya dari `django.urls`. Terakhir saya menambahkan fungsi tampilan untuk menanggapi permintaan HTTP yang masuk dari router.


Poin 3 : Ketika kita melakukan migration, hasilnya bakal disimpan ke *database*. Pas user membuat *request* memanggil fungsi yang ada di `views.py`. Ketika itu juga si fungsi `views.py` mengambil data dari *database* juga. Data yang udh diambil dari *database* akan dipetakan ke dalam HTML.

Poin 4 : Sebelum melakukan `deployment` kita membuat file `procfile` dan membuat `dpl.yml` pada folder `github\workflows` terlebih dahulu. Untuk `deployment` caranya adalah mengatur Heroku_app_name dan Heroku_API_key di dalam *secrets* repository github. Setelah itu pergi ke action dan melakukan `deployment` ulang.