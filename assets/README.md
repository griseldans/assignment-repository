### Perbedaan Inline, Internal, dan External CSS
#### Inline CSS
##### Struktur
1. digunakan untuk *styling* elemen HTML secara spesifik spesifik
2. jenis *styling* diletakkan di dalam tag milik elemen HTML yang dituju
#### Kelebihan
1. Bisa mudah dan cepat dalam melakukan *styling* sehingga cocok digunakan untuk melakukan *preview* pada elemen HTML
2. Efektif digunakan jika hanya ingin melakukan *styling* pada *single* elemen saja
3. Tidak perlu membuat dokumen lain sebagai *external style*
#### Kekurangan
1. Memakan waktu yang lama jika elemen yang di-*styling* banyak
2. Bisa mempengaruhi *download time* jika terlalu banyak *styling* pada element (misal repitisi *styling*

#### Internal CSS
##### Struktur
1. melakukan *styling* di dalam file HTML, tapi bisa di*styling* berdasarkan *selectors*
2. menambahkan `<style>` pada bagian `<head>` HTML
#### Kelebihan
1. Tidak perlu membuat file eksternal CSS
2. Efektif untuk digunakan pada website *single page*
#### Kekurangan
1. Bisa mempengaruhi *download time* jika terlalu banyak *styling* pada element (misal repitisi *styling*

#### Eksternal CSS
##### Struktur
1. melakukan *styling*  dengan membuat file external CSS
#### Kelebihan
1. Satu file CSS bisa digunakan untuk *styling* lebih dari satu *page* website
2. Dokumen HTML lebih rapi karena terlihat struktur elemennya
#### Kekurangan
1. Halaman *page* pada website tidak bisa terrender sesuai file jika file CSS tidak ter-*load* dengan benar
2. *Linking* beberapa file CSS menambah waktu *download time*


### Tag pada HTML5
#### <html></html>
Bertugas sebagai root, yaitu tag yang menaungi isi tagnya sebagai elemen file HTML
#### <head></head>
Bagian tag yang memberikan informasi atau detail mengenai dokumen HTML. Disini kita bisa menambahkan judul dokumen, rujukan *styling*, dsb.
#### <title></title>
Salah satu bagian yang diletakkan di dalam <head> untuk memberikan judul *website page*
#### <body></body>
Bagian setelah <head> yang menjadi tempat dari isi elemen HTML yang akan ditampilkan di *web browser*
#### <p></p>
Tag yang terletak pada <body> untuk membuat sebuah paragraf
#### <!-- komentar-->
Memberikan komentar pada file HTML


### Tipe-tipe selector
1. Element Selector
*Selector* ini memodifikasi *styling* berdasarkan jenis elemen HTML, misalnya elemen h1, p, button, dll.
2. ID Selector
ID yang unik ditambahkan pada di dalam opening tag elemen HTML dengan syntax `id="(nama id)`. Selector ini diidentifikasi dengan tanda pagar (#) pada pendefinisian selector CSS
3. Class Selector
Class bekerja seperti ID, tapi class tidak bersifat unik sehingga class yang sama bisa diberikan kepada lebih dari satu elemen HTML. Pendefinisian selector CSS ini dilakukan dengan simbol titik (.).


### Styling website todolist
1. Membuat external file CSS pada static todolist dan me-*load* file tersebut di file html untuk login, register, dan todolist
2. Memasukkan elemen ke dalam <div class="container"> supaya responsive terhadap ukuran web browsers
3. Untuk mengimplementasikan webpage login, saya mengambil referensi dari https://codepen.io/FlorinPop17/pen/vPKWjd?editors=1000. Webpage register ada yang otomatis terset sesuai css yang direferensikan dari referensi tersebut karena diberikan nama class yang sama
4. Untuk mengimplementasikan webpage todolist, saya mengambil referensi dari https://getbootstrap.com/docs/4.0/components/card/ bagian Title, Text, and Link