## Link Heroku
* https://assignment-griseldaneysasadiya.herokuapp.com/mywatchlist/
* https://assignment-griseldaneysasadiya.herokuapp.com/mywatchlist/json/
* https://assignment-griseldaneysasadiya.herokuapp.com/mywatchlist/html/
* https://assignment-griseldaneysasadiya.herokuapp.com/mywatchlist/xml/


## Perbedaan JSON, XML, HTML
### JSON
Singkatan dari JavaScript Object Nation merupakan bahasa *independent* yang digunakan untuk merepresentasikan data. Syntax JSON berbasis JavaScript. JSON biasanya dimanfaatkan untuk melakukan transmisi data. Formatnya berbentuk seperti dictionary sehingga tiap data memiliki *key* dan *value*. JSON hanya mendukung encoding UTF-8. JSON bersifat *self-describing*

### XML
Singkatan dari Extensible Markup Language yang digunakan untuk menyimpan dan mengirimkan data. XML bukan sebuah bahasa pemrograman dan hanya menyimpan data di dalam *tag* sehingga diperlukan program lain untuk mengakses data dalam file tersebut. XML bersifat *self-descriptive*

### HTML
Singkatan dari HyperText Markup Language yang digunakan untuk membuat *base* dari isi sebuah web. Struktur data HTML terbungkus dalam *tag* dan terbagi menjadi bagian *head* dan *body*. Kemudian dari masing-masing bagian akan terbagi lagi sesuai struktur HTML yang diinginkan. HTML bisa digunakan untuk menampilkan data yang didapatkan dari JSON atau XML di bagian web yang diinginkan. 


## Kebutuhan data delivery dalam implementasi sebuah platform
Sebuah biasanya dikembangkan untuk bisa diakses oleh sebuah kelompok atau bahkan seluruh pengguna Internet. Agar pengguna bisa mengakses sebuah platform, data-data untuk membangun/menjalankan platform di komputer pengguna dikirimkan. Data tersebut bisa berupa HTML, CSS, JPG, dan sebagainya yang nantikan akan dieksekusi komputer sehingga menampilkan platform yang sama di setiap tampilang pengguna. Dengan begitu, data delivery berperan besar pada pemberian akses platform kepada pengguna.

## Cara mengimplementasikan checklist
### Membuat aplikasi `mywatchlist`
Menjalankan `python manage.py startapp mywatchlist` pada virtual environment `assignment repository`dan menambahkan `mywatchlist` pada `INSTALLED_APPS` di `settings.py` milik `project_django`

### Menambahkan *path* `mywatchlist`
Menambahkan  
    >path('mywatchlist/', include('mywatchlist.urls')),
    pada `urls.py` milik `project_django`

### Membuat model pada `models.py` milik folder `mywatchlist`
Membuat class `WatchList` yang berisi atribut yang dibutuhkan. Kemudian, model tersebut di-*migrate* supaya Django App bisa menerapkan skema model

### Menambahkan minimal 10 data
Membuat `initial_watchlist_data.json` dan `initial_watchlist_data.xml` sebagai tempat menampung data mengenai film yang akan/sudah ditonton. Kemudian, data cd di-*load* sebagai database lokal Django App

### Mengimplementasikan sebuah fitur untuk menyajikan data JSON, XML, HTML
Menambahkan fungsi `show_json` dan `show_xml`di `views.py` milik folder `mywatchlist`

### Membuat routing untuk ketiga data tersebut
Menambahkan path yang merujuk ke 3 fungsi baru yang ditambahkan di `views.py` milik folder `mywatchlist`


## Postman
![Alt Text](assets/ss-html.png)
![Alt Text](assets/ss-json.png)
![Alt Text](assets/ss-xml.png)