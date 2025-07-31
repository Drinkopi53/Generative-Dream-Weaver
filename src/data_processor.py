# -*- coding: utf-8 -*-

"""
Modul untuk memproses data gelombang otak.

Modul ini mengambil data mentah yang disimulasikan dan mengubahnya menjadi
format yang dapat digunakan oleh dream_generator.
"""

def process_data(raw_data):
    """
    Memproses data gelombang otak mentah untuk mengekstrak fitur-fitur yang bermakna.

    Args:
        raw_data (list): Daftar nilai numerik dari neuro_simulator.

    Mengembalikan:
        dict: Kamus yang berisi fitur-fitur yang diekstrak dari data,
              misalnya, intensitas rata-rata.
    """
    print("Memproses data gelombang otak...")
    if not raw_data:
        print("Peringatan: Data mentah kosong. Tidak ada yang bisa diproses.")
        return {"average_intensity": 0}

    # Untuk MVP, pemrosesan akan menjadi perhitungan sederhana,
    # seperti menghitung intensitas rata-rata dari sinyal.
    average_intensity = sum(raw_data) / len(raw_data)

    processed_features = {
        "average_intensity": average_intensity
    }

    print(f"Pemrosesan data berhasil. Intensitas rata-rata: {average_intensity:.2f}")
    return processed_features
