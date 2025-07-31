# -*- coding: utf-8 -*-

"""
Modul untuk menghasilkan narasi mimpi.

Menggunakan data yang diproses untuk membuat deskripsi tekstual sederhana
dari sebuah mimpi.
"""

def generate_dream_narrative(processed_data):
    """
    Menghasilkan narasi mimpi berdasarkan fitur data yang diproses.

    Args:
        processed_data (dict): Kamus berisi fitur-fitur yang diproses
                               dari data_processor.

    Mengembalikan:
        str: String yang berisi narasi mimpi yang dihasilkan.
    """
    print("Menghasilkan narasi mimpi...")

    intensity = processed_data.get("average_intensity", 0)

    # Untuk MVP, kita akan menggunakan logika berbasis aturan sederhana untuk menghasilkan narasi.
    # Ini memenuhi persyaratan untuk narasi yang koheren tetapi sederhana.
    if intensity > 1.0:
        narrative = "Mimpi itu intens dan penuh aksi. Mungkin Anda sedang terbang atau berlari cepat."
    elif intensity > 0.7:
        narrative = "Anda mengalami mimpi yang hidup dan menarik, penuh dengan detail yang jelas."
    elif intensity > 0.4:
        narrative = "Mimpi Anda tenang dan damai, seperti berjalan-jalan santai di taman."
    else:
        narrative = "Mimpi itu kabur dan samar, sulit untuk diingat detailnya."

    print("Narasi mimpi berhasil dihasilkan.")
    return narrative
