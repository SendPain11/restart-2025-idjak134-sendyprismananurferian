# Python3.6  
# Coding: utf-8  

# --- BAGIAN 1: DATA INSULIN ---
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

insulin = bInsulin + aInsulin

# --- BAGIAN 2: KAMUS pKR ---
pKR = {'y': 10.07, 'c': 8.18, 'k': 10.53, 'h': 6.00, 'r': 12.48, 'd': 3.65, 'e': 4.25}

# Menghitung SeqCount
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# --- BAGIAN 3: PERHITUNGAN (METODE 1: WHILE LOOP) ---

print("\n--- Hasil dengan WHILE LOOP ---")
pH = 0 # Inisialisasi pH awal 0

while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
        
    # Format string agar rapi (2 angka desimal)
    print('{0:.2f}'.format(pH), netCharge)

    # Naikkan pH
    pH += 1

# --- BAGIAN 4: PERHITUNGAN (METODE 2: FOR LOOP - Opsional) ---
# Jika ingin menampilkan metode for loop juga, pastikan variabel iteratornya BEDA
# atau tidak mengganggu logika while loop di atas.

print("\n--- Hasil dengan FOR LOOP ---")
# Kita pakai variabel 'i' saja agar tidak menimpa variabel 'pH' global, 
# atau biarkan saja karena variabel pH di atas sudah selesai dipakai.
for i in range(15):
    # Disini kita pakai 'i' sebagai pengganti pH
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**i)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**i))/((10**i)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
    
    print(f"pH: {i} | NettCharge: {netCharge}")