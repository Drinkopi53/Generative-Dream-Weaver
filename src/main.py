# -*- coding: utf-8 -*-

"""
File utama untuk aplikasi Generative Dream Weaver.

File ini mengatur alur kerja aplikasi:
1. Mensimulasikan data gelombang otak.
2. Memproses data yang disimulasikan.
3. Menghasilkan narasi mimpi berdasarkan data yang diproses.
4. Menampilkan narasi yang dihasilkan kepada pengguna.
"""

def main():
    """
    Fungsi utama untuk menjalankan aplikasi Generative Dream Weaver.
    """
    print("Selamat datang di Generative Dream Weaver!")
    # Inisialisasi dan jalankan alur kerja aplikasi
    initialize()

# Impor modul-modul yang diperlukan
from neuro_simulator import simulate_brainwave_data
from data_processor import process_data
from dream_generator import generate_dream_narrative
from user_interface import display_narrative

def initialize():
    """
    Menginisialisasi dan menjalankan komponen-komponen aplikasi.
    """
    # 1. Mensimulasikan data gelombang otak
    raw_data = simulate_brainwave_data()

    # 2. Memproses data yang disimulasikan
    processed_data = process_data(raw_data)

    # 3. Menghasilkan narasi mimpi
    narrative = generate_dream_narrative(processed_data)

    # 4. Menampilkan narasi yang dihasilkan
    display_narrative(narrative)

    print("Aplikasi selesai.")

if __name__ == "__main__":
    main()
