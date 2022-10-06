# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Nama            : Reza Taufiq Yahya

Kelas           : PBP C

NPM             : 2106654183

Heroku App Link : https://rezataufiq56.herokuapp.com/todolist/

### 1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
Kegunaannya adalah untuk menghindari serangan berbahaya,  Ini menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk kembali. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Jika tidak terdapat potongan `% csrf_token %` terdapat serangan yang menuju aplikasi web yang kita buat.

### 2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual!

Kita dapat membuat form secara manual. Secara garis besarnya kita membuat formnya sesuai apa yang sudah kita definisikan pada `models.py`

### 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.

Ketika user menambahkan task baru pada form dibuat, task tersebut akan tersimpan pada database sebagai objek dari model `task` untuk ditampilkan pada HTML . Kita perlu mengambil objek dari `task` yang difilter berdasarkan user yang sedang login dan direturn dalam bentuk dictionary sehingga dapat diakses dalam HTML.

### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
1. Membuat app todolist dengan perintah `python manage.py startapp todolist`
2. Menambahkan path todolist ke dalam `urls.py` project django seperti `path ('todolist/',include ('todolist.urls')),`
3. Membuat `class todolist` pada `models.py` yang memiliki atribut user, date, title, dan description
4. Pada `views.py` terdapat berbagai macam fungsi
- `register`
- `login_user`
- `show_todolist`
- `logout_user`
- `create_task`
5. Untuk mengimplementasikan form register kita mengimport
`from django.shortcuts import redirect`
`from django.contrib.auth.forms import UserCreationForm`
`from django.contrib import messages`

kemudian kita masukkan kode pada fungsi register

`def register(request):`
    
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('wishlist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

kemudian kita membuat file `register.html` pada folder *templates*

untuk mmengimplementasikan form login kita mengimport
`from django.contrib.auth import authenticate, login`

kemudian kita memasukkan kode pada fungsi login

`def login_user(request):`
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wishlist:show_wishlist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

kemudian kita membuat file `login.html` pada folder *templates*

untuk mengimplementasikan form logout kita mengimport 
`from django.contrib.auth import logout`

kemudian kita memasukkan kode pada fungsi logout

`def logout_user(request):`

    logout(request)
    return redirect('todolist:login')

6. Selanjutnya kita membuat `todolist.html` yang isinya memuat username pengguna, tombol Tambah Task Baru, tombol logout, serta tabel berisi tanggal pembuatan task, judul task, dan deskripsi task.

7. Kita membuat dua akun pengguna dan tiga dummy data menggunakan model Task pada akun masing-masing di situs web Heroku.




# Tugas 5: Web Design Using HTML, CSS, and CSS Framework

Nama            : Reza Taufiq Yahya

Kelas           : PBP C

NPM             : 2106654183

Heroku App Link : https://rezataufiq56.herokuapp.com/todolist/


### 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

1. Internal CSS adalah kode CSS yang ditulis di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Cara ini akan sangat cocok dipakai untuk menciptakan halaman web dengan tampilan yang berbeda. Dengan kata lain, Internal CSS ini bisa dipakai untuk menciptakan tampilan yang unik, pada setiap halaman website.

2. Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman.

Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin kita atur tampilannya. 

3. Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style, di situ lah inline CSS ditulis.

Cara ini kurang efisien karena setiap tag HTML yang diberikan harus memiliki style masing-masing. kita  akan lebih sulit dalam mengatur website jika hanya menggunakan inline style CSS. Sebab, Inline CSS digunakan hanya untuk mengubah satu elemen saja.

Kelebihan Internal CSS : 
- Perubahan hanya terjadi pada 1 halaman
- Class dan ID bisa digunakan oleh internal stylesheet
- Tidak perlu meng-upload beberapa file karena HTML dan CSS bisa digunakan di file yang sama.

Kekurangan Internal CSS :
- Meningkatkan waktu akses website
- Perubahan hanya terjadi pada 1 halaman – tidak efisien bila Anda ingin menggunakan CSS yang sama pada beberapa file.

Kelebihan Eksternal CSS :
- Ukuran file HTML menjadi lebih kecil dan strukturnya lebih rapi
- Kecepatan loading menjadi lebih cepat
- File CSS yang sama bisa digunakan di banyak halaman.

Kekurangan Eksternal CSS :
- Halaman belum tampil secara sempurna hingga file CSS selesai dipanggil.

Kelebihan Inline CSS :
- Sangat membantu ketika kita hanya ingin menguji dan melihat perubahan pada satu elemen.
- Berguna untuk memperbaiki kode dengan cepat.
- Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

Kekurangan Inline CSS :
- Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.
### 2. Jelaskan tag HTML5 yang kamu ketahui.
HTML5 adalah perbaikan dari HTML. Versi ini diciptakan sebagai solusi untuk kebutuhan saat ini — salah satunya adalah dukungan untuk membuat website yang bersifat mobile-friendly.

HTML5 mampu menangani error secara lebih baik dibanding HTML. Selain itu, HTML5 juga menggunakan syntax yang lebih sederhana dibanding HTML, sehingga developer bisa membuat struktur halaman website yang kompleks secara lebih mudah.

Kelebihan HTML5 :
- Penanganan Error yang Lebih Baik
- Kemudahan untuk Membuat Aplikasi Web
- Syntax yang Lebih Sederhana
- Dukungan untuk Pembuatan Website Responsive
- Support untuk Konten Video dan Audio
- Dukungan untuk Grafik Vektor
- Kompatibel dengan lebih Banyak Browser
- Penyimpanan Informasi secara Lokal
- Fokus Otomatis pada Kolom Form
- Menjalankan JavaScript di Web Browser
### 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selector Tag
Selector Tag disbut juga Type Selector. Selector ini akan memilih elemen berdasarkan nama tag.

2. Selector Class
Selector class adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selector class dibuat dengan tanda titik di depannya.

3. Selector ID
Selector ID hampir sama dengan class. Bedanya, ID bersifat unik. Hanya boleh digunakan oleh satu elemen saja. Selector ID 
ditandai dengan tanda pagar (#) di depannya.

4. Selector Atribut
Selector atribut adalah selector yang memiliki elemen berdasarkan atribut. Selector ini hampir sama seperti selector Tag.

5. Selector Universal
Selector universal adalah selector yang digunakan untuk menyeleksi semua elemen pada jangkaua (scope) tertentu.

6. Pseudo Selector
Pseudo selektor adalah selektor untuk memilih elemen semu seperti state pada elemen, elemen before dan after, elemen ganjil, dan sebagainya.
Ada dua macam pseudo selektor:
- pseudo-class selektor untuk state elemen;
- pseudo-element selektor untuk elemen semu di HTML.
### 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Pada file `login.html` saya membuat tag `body` untuk menghias background website saya dengan menambahkan `style = "background-color :blanchedalmond"` di dalam tag body. Kemudian pada tag `div` saya menambahkan syntax `container-fluid` agar pada class `login` terlihat rapih. Kemudian pada tag `table` menambahkan syntax `text-primary fw-bold` agar warna text menjadi biru dan tebal. Kemudian menambahkan syntax `btn btn-outline-primary` untuk merubah warna button login

2. Pada file `register.html`saya membuat tag `body` untuk menghias background website saya dengan menambahkan `style = "background-color :blanchedalmond"` di dalam tag body. Kemudian pada tag `div` saya menambahkan syntax `container-fluid` agar pada class `register` terlihat rapih. Kemudian pada tag h1 untuk judul saya menambahkan `class="text-success">Formulir Registrasi` untuk memberi warna pada tulisan `Formulir Registrasi`. Untuk `table formulir registrasi` saya menambahkan `class="text-bg-success"` untuk memberikan warna pada background table. Kemudian menambahkan `class="btn btn-dark"` pada button daftar agar menjadi warna hitam

3. Pada file `create_task.html` saya membuat tag `body` untuk menghias background website saya dengan menambahkan `style = "background-color :blanchedalmond"` di dalam tag body. Kemudian pada tag h2 untuk judul saya menambahkan `class="text-success container-fluid">Tambah Task` untuk memberi warna pada tulisan `Formulir Registrasi` dan merapihkan margin pada tulisan `Tambah Task`. Lalu saya menggunakan `Cards` pada bootstrap dengan syntax 
`<div class="card text-bg-success mb-3" style="width: 25rem;">`
      `<form class="text-center fw-bold" action="{% url 'todolist:create_task' %}" method="post">`
      `<div class="card-body">`
        `<h5 class="card-title">Tambah Task</h5>`
        `<p class="card-text">{% csrf_token %} {{form.as_p}}</p>`
        `<input class="btn btn-outline-dark"type="submit" value="Submit" />`
      `</div>`
      `</form>`
    `</div>`
4. Pada file `todolist.html` saya membuat tag `body` untuk menghias background website saya dengan menambahkan `style = "background-color :blanchedalmond"` di dalam tag body. Kemudian pada tag h1 untuk judul saya menambahkan `class="text-center text-primary fw-bold"` untuk memberi warna pada tulisan, tebal, serta center align `Tugas 4 Assignment PBP/PBD To Do List`. Kemudian pada tag `h4` saya menambahkan `class="fw-bold container-fluid"` untuk string nama dan NPM agar tulisan tebal dan rapih. Lalu saya menggunakan Cards bootstrap untuk tampilan task agar lebih rapih dan bagus 
`<button class="btn btn-outline-warning"><a href="{% url 'todolist:create_task' %}">Tambah Task Baru</a></button>`
  `{% for item in todolist %}`
  `<div class="card text-bg-dark mb-3" style="width: 25rem;">`
    `<div class="card-body">`
      `<h5 class="card-title">{{item.title}}</h5>`
      `<h6 class="card-subtitle mb-2 text-muted">{{item.date}}</h6>`
      `<p class="card-text">{{item.description}}</p>`
      `{% if item.is_finished %}`
      `<p class="card-text">Selesai</p>`
      `<button class="btn btn-outline-warning"><a href="{% url 'todolist:set_task' item.pk %}">Mark Undone</a></button>`
      `{% else %}`
      `<p class="card-text">Belum Selesai</p>`
      `<button class="btn btn-outline-warning"><a href="{% url 'todolist:set_task' item.pk %}">Mark Done</a></button>`
      `{% endif %}`
      `<button class="btn btn-outline-warning"><a href="{% url 'todolist:delete' item.pk %}">Hapus Task</a></button>`
      `{% endfor %}`
    `</div>`
  `</div>`
  `<div>`
    `<button class="btn btn-outline-warning text-center" ><a href="{% url 'todolist:logout' %}">Logout</a></button>`
  `</div>`
`</body>`