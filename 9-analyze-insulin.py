import os

# --- PERSIAPAN FOLDER ---
os.makedirs("result", exist_ok=True)

# --- MEMBACA & MEMBERSIHKAN DATA ---
try:
    # Membaca file input
    with open("preproinsulin-seq.txt", "r") as file:
        raw_data = file.read()
    
    # Membersihkan data (menghapus spasi, baris baru, dll)
    clean_seq = raw_data.replace(" ", "").replace("\n", "").replace("\r", "").replace("ORIGIN", "").replace("//", "")
    # Menghapus angka jika ada (agar benar-benar bersih 110 karakter)
    clean_seq = ''.join([i for i in clean_seq if not i.isdigit()])

    # Verifikasi panjang karakter
    if len(clean_seq) != 110:
        print(f"PERINGATAN: Panjang karakter bersih adalah {len(clean_seq)}. Seharusnya 110.")
    else:
        # Simpan file master bersih ke folder result
        with open("result/preproinsulin-seq-clean.txt", "w") as f:
            f.write(clean_seq)

        # --- MENAMPILKAN PREPROINSULIN UTAMA (Clean) ---
        # Bagian ini ditambahkan kembali agar tampil di layar sesuai permintaan Anda
        print("=============PREPROINSULIN (Clean) : simpan karakter 1-110=============")
        print(clean_seq)
        print(f"Berhasil disimpan dan panjang karakter : {len(clean_seq)}")
        print("") # Baris kosong pemisah

        # --- DEFINISI TUGAS ---
        # Format: (Nama Task, Start Index, End Index, Nama File)
        tasks = [
            ("TASK 4.1", 0, 24, "lsinsulin-seq-clean.txt"),
            ("TASK 4.2", 24, 54, "binsulin-seq-clean.txt"),
            ("TASK 4.3", 54, 89, "cinsulin-seq-clean.txt"),
            ("TASK 4.4", 89, 110, "ainsulin-seq-clean.txt")
        ]

        # --- LOOPING UTAMA ---
        for name, start, end, filename in tasks:
            # 1. Ambil potongan karakter (Slicing)
            seq_slice = clean_seq[start:end]

            # 2. Tampilkan Header
            print(f"============={name} : simpan karakter {start+1}-{end}=============")
            
            # 3. Tampilkan Isi Sequence
            print(seq_slice)

            # 4. Simpan ke File
            filepath = os.path.join("result", filename)
            with open(filepath, "w") as file:
                file.write(seq_slice)

            # 5. Tampilkan Konfirmasi
            print(f"Berhasil disimpan dan panjang karakter : {len(seq_slice)}")
            print("") # Baris kosong untuk pemisah

except FileNotFoundError:
    print("Error: File preproinsulin-seq.txt tidak ditemukan.")