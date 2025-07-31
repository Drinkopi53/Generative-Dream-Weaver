# Dokumen Persyaratan Produk (PRD) - MVP Generative Dream Weaver

## 1. Ikhtisar Proyek

Generative Dream Weaver adalah sebuah program inovatif yang dirancang untuk menangkap data gelombang otak saat tidur melalui antarmuka neuro (seperti EEG canggih). Dengan memanfaatkan model generatif canggih (seperti GANs atau Diffusion), program ini bertujuan untuk merekonstruksi visual dan narasi mimpi pengguna ke dalam format video atau teks yang dapat diakses. MVP ini akan berfokus pada demonstrasi fungsionalitas inti dari penangkapan data dan rekonstruksi mimpi sederhana.

## 2. Tujuan MVP

*   Memvalidasi kelayakan teknis penangkapan data gelombang otak yang relevan selama tidur.
*   Mendemonstrasikan kemampuan model generatif untuk memproses data gelombang otak dan menghasilkan representasi mimpi (misalnya, narasi teks sederhana).
*   Menyediakan dasar untuk pengembangan fitur rekonstruksi visual di iterasi mendatang.

## 3. Fitur MVP

*   **Penangkapan Data Gelombang Otak:** Kemampuan untuk menerima atau mensimulasikan input data gelombang otak dari antarmuka neuro.
*   **Pemrosesan Data:** Algoritma dasar untuk memproses data gelombang otak yang masuk.
*   **Rekonstruksi Narasi Mimpi (Teks):** Model generatif yang menghasilkan deskripsi naratif singkat dari mimpi berdasarkan data yang diproses.
*   **Output Hasil:** Menampilkan narasi mimpi yang dihasilkan kepada pengguna.

## 4. Kisah Pengguna (User Stories)

*   **Sebagai** pengguna dengan antarmuka neuro,
    **Saya ingin** menghubungkan perangkat saya ke aplikasi Generative Dream Weaver,
    **Sehingga** data gelombang otak saya dapat ditangkap selama tidur.
    *(Catatan MVP: Untuk MVP, input data gelombang otak akan disimulasikan.)*

*   **Sebagai** sistem Generative Dream Weaver,
    **Saya ingin** memproses data gelombang otak yang masuk,
    **Sehingga** data tersebut dapat digunakan untuk merekonstruksi elemen mimpi.

*   **Sebagai** pengguna yang telah tidur dengan perangkat terhubung,
    **Saya ingin** melihat narasi tekstual dari mimpi saya,
    **Sehingga** saya dapat memahami isi pengalaman bawah sadar saya.

*   **Sebagai** pengguna,
    **Saya ingin** melihat narasi mimpi yang dihasilkan dengan jelas,
    **Sehingga** saya dapat dengan mudah membaca dan menafsirkannya.

## 5. Kriteria Penerimaan (Acceptance Criteria)

*   **Untuk Kisah Pengguna 1 (Penangkapan/Simulasi Data):**
    *   Sistem dapat menerima input data gelombang otak yang disimulasikan.
    *   Format data simulasi didefinisikan dengan jelas dan dapat diurai.
    *   Sistem mengindikasikan penerimaan data yang berhasil.

*   **Untuk Kisah Pengguna 2 (Pemrosesan Data):**
    *   Sistem berhasil memproses data gelombang otak yang disimulasikan tanpa kesalahan.
    *   Data yang diproses berada dalam format yang sesuai untuk model generatif.

*   **Untuk Kisah Pengguna 3 (Rekonstruksi Narasi Mimpi - Teks):**
    *   Model generatif menghasilkan deskripsi naratif tekstual yang koheren (meskipun sederhana) berdasarkan data gelombang otak yang diproses.
    *   Teks yang dihasilkan relevan dengan tema mimpi umum atau pola yang dapat diidentifikasi dari data.
    *   Teks keluaran tidak bersifat nonsens atau berulang secara tidak berarti.

*   **Untuk Kisah Pengguna 4 (Tampilan Hasil):**
    *   Narasi mimpi tekstual yang dihasilkan ditampilkan di antarmuka pengguna.
    *   Teks dapat dibaca dan diformat agar mudah dibaca.
