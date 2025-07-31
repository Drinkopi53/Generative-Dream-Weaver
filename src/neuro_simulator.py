# -*- coding: utf-8 -*-

"""
Modul untuk mensimulasikan data gelombang otak.

Untuk MVP, ini akan menghasilkan data sampel yang telah ditentukan sebelumnya
atau data yang dibuat secara acak yang meniru pola dasar gelombang otak.
"""

def simulate_brainwave_data():
    """
    Mensimulasikan penangkapan data gelombang otak dari antarmuka neuro.

    Mengembalikan:
        list: Daftar nilai numerik yang mewakili data gelombang otak yang disimulasikan.
    """
    print("Mensimulasikan data gelombang otak...")
    # Untuk MVP, kita akan mengembalikan daftar nilai statis untuk memastikan
    # output yang dapat diprediksi untuk pengujian.
    # Nilai-nilai ini dapat mewakili amplitudo sinyal EEG dari waktu ke waktu.
    simulated_data = [0.5, 0.6, 0.7, 0.9, 1.2, 1.5, 1.1, 0.8, 0.6, 0.4]
    print("Simulasi data berhasil.")
    return simulated_data
