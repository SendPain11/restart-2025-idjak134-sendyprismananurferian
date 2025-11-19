import sys
import os

# --- KONFIGURASI FOLDER ---
folder_sumber = "result"

# --- FUNGSI PEMBANTU (VERSI IF/ELSE) ---
def baca_file_dari_result(nama_file):
    """
    Mencoba membaca file dari folder 'result' menggunakan pengecekan IF.
    """
    # Menggabungkan nama folder dan nama file
    path_lengkap = os.path.join(folder_sumber, nama_file)
    
    # [UBAHAN UTAMA] Menggunakan IF os.path.exists daripada Try-Except
    if os.path.exists(path_lengkap):
        # Jika file ADA, maka buka dan baca
        with open(path_lengkap, "r") as f:
            isi = f.read().strip()
            print(f"[BERHASIL] File '{path_lengkap}' ditemukan & dimuat.")
            return isi
    else:
        # Jika file TIDAK ADA (Else), cetak pesan gagal
        print(f"[GAGAL] ❌ File '{path_lengkap}' TIDAK ditemukan! Cek apakah file sudah dibuat.")
        return None

# --- BAGIAN 1: MEMUAT VARIABEL ---
print(f"--- MEMULAI PROSES LOAD DATA DARI FOLDER '{folder_sumber}' ---")

preproInsulin = baca_file_dari_result("preproinsulin-seq-clean.txt")
lsInsulin = baca_file_dari_result("lsinsulin-seq-clean.txt")
bInsulin = baca_file_dari_result("binsulin-seq-clean.txt")
aInsulin = baca_file_dari_result("ainsulin-seq-clean.txt")
cInsulin = baca_file_dari_result("cinsulin-seq-clean.txt")

print("--------------------------------\n")

# Pengecekan Keamanan: Jika ada satu saja file yang gagal, program berhenti.
if None in [preproInsulin, lsInsulin, bInsulin, aInsulin, cInsulin]:
    print("CRITICAL ERROR: Data tidak lengkap. Periksa folder 'result' Anda.")
    sys.exit() # Menghentikan program

# --- BAGIAN 2: LOGIKA PROGRAM (SAMA SEPERTI SEBELUMNYA) ---

# Menggabungkan rantai B dan A
insulin = bInsulin + aInsulin

# Printing ke layar
print("The sequence of human preproinsulin:")
print(preproInsulin)

# Menggunakan variabel aInsulin yang diambil dari file
print("The sequence of human insulin, chain a: " + aInsulin)

# --- BAGIAN 3: PERHITUNGAN BERAT MOLEKUL ---

# Daftar berat asam amino
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}  

# Menghitung jumlah setiap asam amino
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']})  

# Mengalikan jumlah dengan beratnya
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in
['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
'S', 'T', 'V', 'W', 'Y']}.values())  

print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))

# Menghitung persentase error
molecularWeightInsulinActual = 5807.63
print("Error percentage: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))