### Link Heroku
http://assignment-griseldaneysasadiya.herokuapp.com/todolist/login/?next=/todolist/

### Akun dummy
1. username: percobaan1; password: susuindomilk
2. username: percobaan2; password: susugreenfield


### Fungsi {% csrf_token %}
{% csrf_token %} adalah sebuah *template* tag yang men-*generate* sebuah token guna menjaga keamanan data pengguna. Token yang dihasilkan melindungi pengguna dari *cross-site request forgery* dengan memastikan bahwa HTTP Request benar berasal dari pengguna aplikasi yang terotentifikasi. Tiap akses form diberikan token baru yang bersifat unik untuk setiap sessionnya meskipun diakses oleh pengguna yang sama. Jika tidak menggunakan {% csrf_token %}, pengguna bisa di-*hack* karena aplikasi tidak bisa mengenali pengguna asli sehingga *hacker* bisa mengambil alih akses pengguna di aplikasi.


### Buat <form> secara manual
Elemen `form` bisa dibuat tanpa generator seperti {{ form.as_table }}. Pada file HTML, dapat digunakan tag elemen <label> untuk memberikan jenis identitas kolum pada kolom input dan <input> untuk membuat kolom input tersebut. Struktur umumnya:
```
<form>
    <label for=(sesuai atribut model)>title</label>
    <input type=(disesuaikan jenis input yang diterima)>
</form>
```
Isi dari elemen <form> lah yang bisa kita identifikasi menjadi sebuah *table*, *div*, dsb.


### Proses alur submisi dan penampilan data yang diambil dari form
1. Ketika pengguna menekan tombol `submit`, 
sebuah request terbentuk. Masukan yang ada dari kolom input disimpan sesuai jenis atribut yang tertera pada tag elemen <label>nya.
2. Request tersebut dijadikan parameter dari fungsi yang memuat `file.html` yang memiliki form tersebut pada *context*-nya di `views.py`.
3. Request tersebut menjadi parameter instance `Form`. Pada class `Form`, request bisa diidentifikasi jika semua jumlah dan jenis atributnya sama dengan atribut yang dikenali `Form`.
4. Instance `Form` disimpan menggunakan .save() sehingga data tersimpan pada database sesuai atributnya.
5. Data yang sudah tersimpan berarti sudah memenuhi syarat skema model, maka untuk menampilkan data tersebut pada template HTML hanya perlu melakukan tahap yang biasanya dilakukan, yaitu melakukan objektifikasi pada model dan memasukkan objek tersebut ke `context`.


### Implementasi Checklist
- [x] Membuat aplikasi `todolist`
Pada cmd, membuat folder aplikasi dengan perintah `startapp`. Kemudian menambahkan aplikasi di `INSTALLED_APPS` di `settings.py` 

- [x] Menambahkan *path* `todolist`
Menambahkan `path('todolist/', include('todolist.urls'))` pada `project_django\views.py`

- [x] Membuat model task
Membuat variable yang diminta dengan tipe field yang cocok pada `todolist.models/py`. Kemudian, model di-*migrate*

- [x] Mengimplementasi form registrasi, login, logout
* Melakukann import yang tertera pada line 3 hingga line 15 pada `todolist\views.py`
* Membuat fungsi register, login, logout yang isi fungsinya yang disediakan di Tutorial 3 dengan disesuaikan nama aplikasinya. Class form yang digunakan pada register adalah Class bawaan Django, yaitu UserCreationForm().
* Menambahkan syntax *login required* pada fungsi `show_task` dan `get_task`
* Membuat `register.html` dan `login.html` sebagai *template* tampilan form.
* Manambahkan `button` untuk logout pada `todolist.html`

- [x] Membuat halaman form untuk pembuatan task
* Membuat file `forms.py`dan membuat Class TaskFrom() menggunakan Model.Form
* Memuat pada Meta di TaskForm() model berupa ToDoList dan field untuk title dan description saja untuk menerima input dari user
* Menambahkan fungsi `get_task` pada `todolist\views.py` untuk pemroses request task
* Membuat `task.html` sebagai template halaman penampil form pembuat task

- [x] Membuat routing
Pada `todolist\urls.py`dibuat:
```
path('', show_todolist, name='show_todolist'),
path('register/', register, name='register'),
path('login/', login_user, name='login'),
path('logout/', logout_user, name='logout'),
path('create-task/', get_task, name='create-task')
```

- [x] Melakukan *deployment*
Program di *add*, *commit*, *push*. Karena di repository sudah ada `secrets` untuk aplikasi heroku dan API key, maka perubahan pada program otomatis ter-*deploy* dengan tanda *workflow* pada Action berhasil

- [x] Membuat dummy
Pada tiap akun dilakukan:
* Membuat akun dengan registrasi akun
* Membuat tiga task dengan menekan tombol `Tambah Task Baru` dan mengisi data yang dibutuhkan
* Logout dan lakukan hal yang sama untuk akun lainnya