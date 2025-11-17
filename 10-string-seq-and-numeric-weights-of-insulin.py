import sys

# --- FUNGSI PEMBANTU (HELPER FUNCTION) ---
def baca_file_dengan_status(nama_file):
    """
    Mencoba membaca file. 
    Jika ada: print SUKSES dan kembalikan isinya.
    Jika tidak ada: print GAGAL dan kembalikan None.
    """
    try:
        with open(nama_file, "r") as f:
            isi = f.read().strip()
            # INI YANG ANDA MINTA: Konfirmasi visual
            print(f"[BERHASIL] File '{nama_file}' ditemukan & dimuat.")
            return isi
    except FileNotFoundError:
        print(f"[GAGAL] ❌ File '{nama_file}' TIDAK ditemukan!")
        return None

# --- BAGIAN 1: MEMUAT VARIABEL ---
print("--- MEMULAI PROSES LOAD DATA ---")

preproInsulin = baca_file_dengan_status("preproinsulin-seq-clean.txt")
lsInsulin = baca_file_dengan_status("lsinsulin-seq-clean.txt")
bInsulin = baca_file_dengan_status("binsulin-seq-clean.txt")
aInsulin = baca_file_dengan_status("ainsulin-seq-clean.txt")
cInsulin = baca_file_dengan_status("cinsulin-seq-clean.txt")

print("--------------------------------\n")

# Pengecekan Keamanan: Jika ada satu saja file yang gagal, program berhenti.
# Agar tidak error saat perhitungan matematika di bawah.
if None in [preproInsulin, lsInsulin, bInsulin, aInsulin, cInsulin]:
    print("CRITICAL ERROR: Data tidak lengkap. Periksa file .txt Anda.")
    sys.exit() # Menghentikan program

# --- BAGIAN 2: LOGIKA PROGRAM (LAB ORIGIN) ---

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