## Link Heroku
https://assignment-griseldaneysasadiya.herokuapp.com/katalog/

## Bagan
![alt text](./assets/bagan.jpeg)
**urls.py**: menerima request client, lalu memetakan path request-an client ke **views.py**.
**views.py**: menjadi jembatan antara **models.py** dan **html**, mengisi file **html** dengan context yang bisa diambil dari **models.py**.
**html**: menyediakan template untuk ditampilkan di layar user dengan mengirimkannya ke **views.py** untuk diproses
**models.py**: mengobjektifikasi dan mengirimkan data dari **database** untuk digunakan oleh **views.py**

## Penggunaan Virtual Envinronment
Virtual envinronment digunakan pada saat proses pengembangan program supaya program dibangun di lingkungan yang terisolasi sehingga perubahan yang ada tidak mempengaruhi jalan kerja komputer host. Sebenarnya, tanpa virtual envinronment pun aplikasi Django tetap bisa jalan, namun resikonya komputer host ikut mengalami perubahan dalam proses pengembangan aplikasi Django tersebut.

## Implementasi poin 1 - 4:
    1. Fungsi yang sudah disediakan, yaitu showkatalog(), bagian isinya ditambahkan dengan inisiasi varibale **data_barang_katalog** dengan value objek dari class **CatalogItem**. Kemudian dibuat dictionary **context** untuk menyimpan data yang dibutuhkan untuk diakses nanti
    2. Mengkonfigurasikan path dengan syntax
     ```
     urlpatterns = [
    path('', show_katalog, name='show_katalog'),
    ]
     ```
    3. Pada struktur kalimat yang ingin disisipkan data di file **html**, diberikan syntax **{{data}}**. Kemudian khususnya pada tabel, dilakukan looping untuk memunculkan data dengan syntax 
    ```
    {% for barang in list_barang %}
    ...
    {% endfor %} 
    ```
    4. Meregister **repository secret** baru, yaitu ***HEROKU_APP_NAME*** dan ***HEROKU_API_KEY*** supaya workflow berhasil berjalan dan deployment berhasil dilakukan