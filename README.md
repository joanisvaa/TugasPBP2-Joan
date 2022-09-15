# Tugas 2 PBP 
Link app: https://tugas2pbp-joan.herokuapp.com/katalog/

Joan Isva Shanti Andrea
2106707712
PBP E

1. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
<img width="718" alt="Screen Shot 2022-09-15 at 09 35 21" src="https://user-images.githubusercontent.com/101711787/190300191-0918f1cc-564e-4787-a78f-62589b9840fe.png">

Model berperan sebagai penyedia interface untuk menyimpan dan mengatur data pada database. Views berperan sebagai penerima input user yang dibuat oleh Template. Melalui Models, Views menerima data dari database dan mengirimkan data tersebut kepada user. Template berperan sebagai user interface bagi user. User akan meminta sebuah URL request untuk mengambil data melalui template pada Django. Kemudian, Django akan mencari URL request tersebut. URL akan memanggil Views dan Views akan berinteraksi dengan Model dan mengambil data dari database. Views akan mengcompile response yang dibuat oleh Model kembali ke Template. Siklus request-respons akan dimulai.

2. Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment berfungsi untuk mengisolasi package serta dependencies dari aplikasi. Virtual environment berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Setiap proyek Django sebaiknya memiliki virtualenv-nya sendiri. Virtual environment pada sebuah projek Django bukanlah suatu keharusan namun hal ini lebih baik dilakukan, terutama apabila terdapat beberapa proyek. 


3. Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

Saya mengerjakan Tugas 2 PBP sesuai dengan cara yang sudah dipelajari pada Lab 1 yang lalu. 
Untuk langkah pertama, saya membuat sebuah fungsi dengan parameter request pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML. 

def show_katalog(request):
    return render(request, "katalog.html")
    
Kemudian saya membuat sebuah folder bernama templates di dalam folder aplikasi katalog dan membuat file bernama katalog.html. 
 
Untuk langkah kedua, saya membuat file HTML yang nantinya akan ditampilkan di browser dengan membuat file bernama urls.py yang melakukan routing terhadap fungsi views yang sudah dibuat pada langkah-langkah sebelumnya. Berikut 

from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]

Langkah ketiga adalah untuk menghubungkan models dengan views dan template atau mapping. Cara untuk menghubungkan models dengan views adalah untuk mengimport models yang sudah dibuat sebelumnya di dalam file views.py. Kemudian, saya melakukan mapping pada data yang telah ikut di-render pada fungsi views untuk memunculkan di halaman HTML. Untuk menampilkan daftar barang ke dalam tabel, saya melakukan iterasi variabel list_barang yang telah di-render ke dalam HTML.
Kemudian saya melakukan git add, commit, dan push. 

Langkah keempat adalah untuk melakukan deployment. Saya membuat aplikasi baru di akun heroku saya sesuai dengan nama aplikasi yang saya inginkan (tugas2pbp-joan). Kemudian, saya menambahkan file Tugas2PBP_HEROKU.txt di github yang berisikan API key dan app name dari aplikasi saya. Setelah itu, saya membuat 2 secret baru, yaitu API key dan app name secara terpisah. Terakhir, saya melakukan re-run all failed jobs di github dan melakukan deployment. 

# Template Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselengga
rakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

*Read this in other languages: [Indonesian](README.md), [English](README.en.md)*

## Pendahuluan

Repositori ini merupakan sebuah template yang dirancang untuk membantu mahasiswa yang sedang mengambil mata kuliah Pemrograman Berbasis Platform (CSGE602022) mengetahui struktur sebuah proyek aplikasi Django serta file dan konfigurasi yang penting dalam berjalannya aplikasi. Kamu dapat dengan bebas menyalin isi dari repositori ini atau memanfaatkan repositori ini sebagai pembelajaran sekaligus awalan dalam membuat sebuah proyek Django.

## Cara Menggunakan

Apabila kamu ingin menggunakan repositori ini sebagai repositori awalan yang nantinya akan kamu modifikasi:

1. Buka laman GitHub repositori templat kode, lalu klik tombol "**Use this template**"
   untuk membuat salinan repositori ke dalam akun GitHub milikmu.
2. Buka laman GitHub repositori yang dibuat dari templat, lalu gunakan perintah
   `git clone` untuk menyalin repositorinya ke suatu lokasi di dalam sistem
   berkas (_filesystem_) komputermu:

   ```shell
   git clone <URL ke repositori di GitHub> <path ke suatu lokasi di filesystem>
   ```
3. Masuk ke dalam repositori yang sudah di-_clone_ dan jalankan perintah berikut
   untuk menyalakan _virtual environment_:

   ```shell
   python -m venv env
   ```
4. Nyalakan environment dengan perintah berikut:

   ```shell
   # Windows
   .\env\Scripts\activate
   # Linux/Unix, e.g. Ubuntu, MacOS
   source env/bin/activate
   ```
5. Install dependencies yang dibutuhkan untuk menjalankan aplikasi dengan perintah berikut:

   ```shell
   pip install -r requirements.txt
   ```

6. Jalankan aplikasi Django menggunakan server pengembangan yang berjalan secara
   lokal:

   ```shell
   python manage.py runserver
   ```
7. Bukalah `http://localhost:8000` pada browser favoritmu untuk melihat apakah aplikasi sudah berjalan dengan benar.

## Contoh Deployment 

Pada template ini, deployment dilakukan dengan memanfaatkan GitHub Actions sebagai _runner_ dan Heroku sebagai platform Hosting aplikasi. 

Untuk melakukan deployment, kamu dapat melihat instruksi yang ada pada [Tutorial 0](https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-0).

Untuk contoh aplikasi Django yang sudah di deploy, dapat kamu akses di [https://django-pbp-template.herokuapp.com/](https://django-pbp-template.herokuapp.com/)

## Credits

Template ini dibuat berdasarkan [PBP Ganjil 2021](https://gitlab.com/PBP-2021/pbp-lab) yang ditulis oleh Tim Pengajar Pemrograman Berbasis Platform 2021 ([@prakashdivyy](https://gitlab.com/prakashdivyy)) dan [django-template-heroku](https://github.com/laymonage/django-template-heroku) yang ditulis oleh [@laymonage, et al.](https://github.com/laymonage). Template ini dirancang sedemikian rupa sehingga mahasiswa dapat menjadikan template ini sebagai awalan serta acuan dalam mengerjakan tugas maupun dalam berkarya.

Sumber: https://techvidvan.com/tutorials/djangos-mvt-architecture/
