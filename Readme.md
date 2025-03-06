# Cara Menjalankan Streamlit Secara Lokal

Dokumen ini berisi langkah-langkah untuk menjalankan dashboard berbasis **Streamlit** secara lokal berdasarkan struktur direktori yang diberikan.

## **1. Persiapan Lingkungan**
Sebelum menjalankan Streamlit, pastikan Anda memiliki Python dan pip terinstal di sistem Anda.

Jika belum menginstal Streamlit, jalankan perintah berikut:

```bash
pip install streamlit
```

## **2. Masuk ke Direktori Dashboard**
Arahkan terminal atau command prompt ke dalam direktori tempat file `dashboard.py` berada:

```bash
cd submission/dashboard
```

## **3. Jalankan Streamlit**
Jalankan Streamlit dengan perintah berikut:

```bash
streamlit run dashboard.py
```

## **4. Akses Dashboard di Browser**
Setelah menjalankan perintah di atas, terminal akan menampilkan output seperti berikut:

```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Buka browser dan akses URL **http://localhost:8501** untuk melihat dashboard.

## **5. Troubleshooting (Opsional)**
Jika mengalami kendala:
- Pastikan semua dependensi telah diinstal dengan:
  ```bash
  pip install -r ../requirements.txt
  ```
- Jika ada perubahan pada kode, restart Streamlit dengan menekan **Ctrl + C** lalu menjalankan kembali perintah **streamlit run dashboard.py**.

---
Sekarang dashboard Anda siap dijalankan secara lokal! 🚀


