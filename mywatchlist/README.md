# Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Nama            : Reza Taufiq Yahya

Kelas           : PBP C

NPM             : 2106654183

Heroku App Link : https://rezataufiq56.herokuapp.com/mywatchlist/

## 1. Jelaskan perbedaan antara JSON, XML, dan HTML!

1. JSON menyimpan elemennya secara efisien akan tetapi tidak rapi untuk dilihat. Sedangkan XML menyimpan elemen-elemen nya dengan cara yang terstruktur, mudah dibaca oleh manusia dan mesin, akan tetapi kurang efisien.
2. Nama dari file JSON akan diakhiri dengan ekstensi .json. Sementara file XML akan diakhiri dengan ekstensi .xml.
3. Untuk penerapannya, JSON digunakan untuk mengirimkan data dengan cara data diuraikan dan dikirimkan melalui internet. Sedangkan XML memiliki data yang lebih terstruktur dan pengguna dapat menggunakannya untuk menambahkan catatan.
4. HTML berfungsi sebagai `interface` utama dan terdepan dalam sebuah website. Segala teks yang kita lihat dari sebuah laman website merupakan HTML. Dalam kata lain, HTML menampilkan segala sesuatu yang berhubungan dengan text pada sebuah laman web.
5. HTML adalah sebagai penanda struktur susunan yang ditampilkan seperti apa

## 2. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Karena agar data bisa disajikan dalam bentuk apapun, maka diperlukan data delivery

## 3. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!

Pertama saya membuat app baru pada folde tugas 2 pekan kemarin dengan perintah `python manage.py startapp mywatchlist`. Kemudian saya menambahkan path *mywatchlist* di `urls.py`agar pengguna dapat mengakses di `http://localhost:8000/mywatchlist`. Selanjutnya saya membuat sebuah model `MyWatchlist` pada *models.py* yang memiliki atribut `watched` untuk mendeskripsikan film tersebut sudah ditonton atau belum, `title` untuk mendeskripsikan judul film, `rating` untuk mendeskripsikan rating film dalam rentang 1 sampai dengan 5, `release_date` untuk mendeskripsikan kapan film dirilis, `review` untuk mendeskripsikan review untuk film tersebut. Lalu saya membuat file `initial_mywatchlist_data.json` yang isinya 10 data untuk objek `MyWatchList`. untuk menyajikan data dalam bentuk `HTML`, `XML`, dan `JSON` saya menambahkan `urlspatterns` di `urls.py` dengan cara 
1. `path('html', show_MyWatchList name='show_MyWatchlist'),`
2. `path('xml/', show_xml, name='show_xml'),`
3. `path('json/', show_json, name='show_json'),`

Saya juga membuat fungsi pada file `views.py` 
1. `def show_xml(request):`
    `data = MyWatchList.objects.all()`
    `return HttpResponse(serializers.serialize("xml" data), content_type="application/xml")`

2. `def show_json (request):`
    `data = MyWatchList.objects.all()`
    `return HttpResponse(serializers.serialize("json",` `data), content_type="application/json")`

3. `def show_json_by_id (request,id):`
    `data = MyWatchList.objects.filter(pk=id)`
    `return HttpResponse(serializers.serialize("json",` `data), content_type="application/json")`

4. `def show_xml_by_id (request,id):`
    `data = MyWatchList.objects.filter(pk=id)`
    `return HttpResponse(serializers.serialize("xml",` `data), content_type="application/xml")`

untuk membuat routing saya menambahkan path pada `urls.py` agar data dapat diakses berupa `HTML`, `XML`, dan `JSON`. Untuk `deployment` sudah otomatis terdeploy ke `herokuapp` karena memakai repo github yang sama yang sudah terdeploy juga. 

Pada `tests.py` saya membuat 3 fungsi yang isi parameternya `self` dan variabel response isinya `client().get` dengan paramaternya masing - masing jenis data.

