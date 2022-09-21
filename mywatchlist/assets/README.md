## Link Heroku


## Perbedaan JSON, XML, HTML


## Kebutuhan data delivery dalam implementasi sebuah platform


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
Membuat `initial_watchlist_data.json` dan `initial_watchlist_data.xml` sebagai tempat menampung data mengenai film yang akan/sudah ditonton. Kemudian, data di-*load* sebagai database lokal Django App

### Mengimplementasikan sebuah fitur untuk menyajikan data JSON, XML, HTML
Menambahkan fungsi `show_json` dan `show_xml`di `views.py` milik folder `mywatchlist`

### Membuat routing untuk ketiga data tersebut
Menambahkan path yang merujuk ke 3 fungsi baru yang ditambahkan di `views.py` milik folder `mywatchlist`