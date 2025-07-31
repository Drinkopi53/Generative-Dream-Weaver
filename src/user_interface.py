# -*- coding: utf-8 -*-

"""
Modul untuk antarmuka pengguna.

Menangani presentasi output kepada pengguna. Untuk MVP, ini akan
menjadi output konsol sederhana.
"""

def display_narrative(narrative):
    """
    Menampilkan narasi mimpi yang dihasilkan kepada pengguna.

    Args:
        narrative (str): Narasi mimpi yang akan ditampilkan.
    """
    print("\n--- Rekonstruksi Mimpi Anda ---")
    print(narrative)
    print("---------------------------------\n")
