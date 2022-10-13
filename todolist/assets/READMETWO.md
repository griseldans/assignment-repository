### Perbedaan antara asynchronous programming dengan synchronous programming.
* asynchronous multithread, sedangkan synchronous single thread
* asynchronous bisa mengirimkan beberapa request ke server tanpa harus membuat program berhenti sementara, sedangkan synchronous menyebabkan program menunggu ketika satu request dikirimkan ke server

### Jelaskan maksud dari paradigma Event-Driven Programming dan sebutkan salah satu contoh penerapannya pada tugas ini.
*Event-driven programming* merupakan paradigma yang menentukan alur program berdasarkan event yang diberikan user, seperti *mouse click*, *key press*, dsb. Contoh *event-driven programming* dari tugas ini terletak pada line 78 file `todolist.html`, yaitu `$('#save-task-btn').click(function(){..}` pada bagian click yang menunjukkan event akan terjadi jika *user* mengklik button Save Changes.

### Jelaskan penerapan asynchronous programming pada AJAX.
Website tidak perlu di-*refresh* secara keseluruhan untuk menampilkan perubahan terbaru. Pada tugas ini, digunakan AJAX GET untuk mengambil data dan AJAX POST untuk mengirimkan data ke server. Pengguna tetap berada di halaman website yang sama ketika proses transaksi data terjadi.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Memberikan script AJAX jQuery di `<head>` base.html
2. Membuat fungsi `show_json` pada `views.py` dan menambahkan pathnya untuk memberikan data JSON ke AJAX
3. Membuat `<script>` di bawah syntax HTML berisi implementasi jQuery untuk AJAX
4. Membuat fungsi get_json() di dalam `<script>` untuk memberikan akses data JSON ke AJAX dengan AJAX GET
5. Membuat modal menggunakan syntax yang disediakan Bootstrap
6. Membuat fungsi add_task() di dalam `<script>` untuk mengambil isi input user dan menampilkannya sebagai card baru. Di dalamnya terdapat event mouse click untuk mengobjek input user sebagai data baru JSON