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