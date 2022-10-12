# Tugas 6: Javascript dan AJAX

Nama            : Reza Taufiq Yahya

Kelas           : PBP C

NPM             : 2106654183

Heroku App Link : https://rezataufiq56.herokuapp.com/todolist/

## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.

Asynchronous adalah proses jalannya program bisa dilakukan secara bersamaan tanpa harus menunggu proses antrian. Synchronous merupakan bagian dari Asynchronous (1 antrian) dimana proses akan dieksekusi secara bersamaan dan untuk hasil tergantung lama proses suatu fungsi synchronous .

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

Event-driven adalah suatu paradigma pemrograman yang alur programnya ditentukan oleh suatu event / peristiwa yang merupakan keluaran atau tindakan pengguna, atau bisa berupa pesan dari program lainnya. Misal, ketika tombol A diklik maka nilai X akan ditambah dengan 3. Ketika tombol B diklik maka nilai X akan dikurangi dengan 2. Tombol yang diklik ini disebut sebagai event.

Penerapan paradigma dalam tugas ini adalah penerapan tombol submit formulir untuk menambahkan task. Ketika tombol ini ditekan, acara pengiriman formulir akan ditampilkan. Acara ini ditangkap oleh AJAX, yang menangani pengiriman data formulir ke server. AJAX kemudian secara asinkron memperbarui data todolist dari server.
## 3. Jelaskan penerapan asynchronous programming pada AJAX.

Yang berarti bahwa browser tidak perlu memuat ulang seluruh halaman ketika hanya sedikit data pada halaman yang berubah. AJAX hanya meneruskan informasi yang diperbarui ke dan dari server.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

### AJAX GET
Untuk membuat AJAX, hanya perlu menyisipkan script pada bagian <head> atau <body> (pada tugas ini akan disisipkan pada <head>) dengan menggunakan tag <script>. Untuk AJAX GET, pertama-tama ikuti spesifikasi masalah dan buat routing dan fungsi seperti pada tugas sebelumnya untuk membantu pembuatan data.

Pada `views.py`

`...`
`@login_required(login_url='/todolist/login/')`
`def show_json(request):`
    `orang = request.user`
    `dataTask = Task.objects.all().filter(user = orang)`
    `return HttpResponse(serializers.serialize("json", dataTask), content_type="application/json")`
`...`

Pada `urls.py` saya menambahkan pattern untuk show_json
`path('json/', show_json, name='show_json'),`

Kemudian tambahkan saja script ke file todolist.html Anda. Script berjalan ketika web selesai memuat, mengambil data dari path /todolist/json, mengulangi setiap item, dan menyortir antara yang selesai dan yang belum selesai. Kemudian elemen div baru yang cocok dibuat.

### AJAX POST
Untuk AJAX POST, pertama buat rute dan fungsi seperti pada tugas sebelumnya, mengikuti spesifikasi pertanyaan untuk membantu menghasilkan data.
pada `views.py`

`@login_required(login_url='/todolist/login/')`
`def add_task(request):`
    `if request.method == 'POST':`
        `task = Task()`
        `task.user = request.user`
        `task.title = request.POST.get('title')`
        `task.description = request.POST.get('description')`
        `task.save()`
        `return redirect('todolist:show_todolist')`

Pada `urls.py` saya menambahkan pattern untuk add_tesk
`path('add/', add_task, name='add_task'),`

Jangan lupa untuk membuat modal juga. Modal dapat diambil dari dokumentasi Bootstrap dan dimodifikasi sesuai kebutuhan. Kemudian tambahkan saja skrip berikut ke file todolist.html, Ketika formulir diklik dengan id=addTask , skrip diaktifkan dan data yang dikonversi ke format yang sesuai dikirim ke jalur yang disebutkan dalam kode di bawah ini. Setelah mengirimkan data, modal dihapus dan formulir diatur ulang.

`$("#addTask").submit(function (e) {`
      `e.preventDefault();`
      `var serializedData = $(this).serialize();`
      `$.ajax({`
          `url: "{% url 'todolist:add_task' %}",`
          `type: "POST",`
          `data: serializedData,`
          `dataType: 'text',`
          `success: function (data) {`
              `$("#exampleModal").modal('hide');`
              `$('#addTask').each(function () {`
                  `this.reset();`
              `});`
          `}`
     `});`
`});`