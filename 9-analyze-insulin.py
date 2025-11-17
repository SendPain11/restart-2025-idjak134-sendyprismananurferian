# This is code task for analyze insulin in ncbi with python

# --- BAGIAN 1: MEMBACA & MEMBERSIHKAN DATA ---
try:
    with open("preproinsulin-seq.txt", "r") as file:
        raw_data = file.read()
    
    # PENTING: File Anda di screenshot memiliki spasi. 
    # Kita harus menghapus spasi (" ") dan baris baru ("\n") agar hitungannya pas 110.
    clean_seq = raw_data.replace(" ", "").replace("\n", "").replace("\r", "")
    
    # Verifikasi panjang karakter (Harus 110)
    if len(clean_seq) != 110:
        print(f"PERINGATAN: Panjang karakter adalah {len(clean_seq)}. Seharusnya 110.")
        print("Pastikan tidak ada angka atau teks 'ORIGIN' di dalam file txt.")
    else:
        print("Data valid! Panjang karakter pas 110.")
        
        # Simpan versi bersih utama (opsional, diminta lab)
        with open("preproinsulin-seq-clean.txt", "w") as f:
            f.write(clean_seq)

        # --- BAGIAN 2: MEMECAH (SLICING) ---
        # lsinulin: indeks 0 sampai 24
        lsinsulin = clean_seq[0:24]
        
        # binsulin: indeks 24 sampai 54
        binsulin = clean_seq[24:54]
        
        # cinsulin: indeks 54 sampai 89
        cinsulin = clean_seq[54:89]
        
        # ainsulin: indeks 89 sampai 110
        ainsulin = clean_seq[89:110]

        # --- BAGIAN 3: MENYIMPAN KE FILE ---
        with open("lsinsulin-seq-clean.txt", "w") as f:
            f.write(lsinsulin)
            
        with open("binsulin-seq-clean.txt", "w") as f:
            f.write(binsulin)
            
        with open("cinsulin-seq-clean.txt", "w") as f:
            f.write(cinsulin)
            
        with open("ainsulin-seq-clean.txt", "w") as f:
            f.write(ainsulin)

        print("Sukses! 4 file sequence telah dibuat.")

except FileNotFoundError:
    print("Error: File preproinsulin-seq.txt tidak ditemukan.")
    
    
print("\n--- VERIFIKASI ISI FILE HASIL ---")

# Daftar nama file yang ingin dicek
file_list = [
    "lsinsulin-seq-clean.txt",
    "binsulin-seq-clean.txt",
    "cinsulin-seq-clean.txt",
    "ainsulin-seq-clean.txt"
]

for nama_file in file_list:
    try:
        with open(nama_file, "r") as f:
            isi = f.read()
            # Menampilkan nama file, jumlah karakter, dan isinya
            print(f"File: {nama_file}")
            print(f"Panjang: {len(isi)} karakter") 
            print(f"Isi: {isi}")
            print("-" * 30)
    except FileNotFoundError:
        print(f"Error: {nama_file} belum dibuat.")