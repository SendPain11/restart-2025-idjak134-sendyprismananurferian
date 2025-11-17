# Python3.6  
# Coding: utf-8  

# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  

# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  

# Menggabungkan rantai B dan A menjadi insulin
insulin = bInsulin + aInsulin

# Membuat Dictionary pKR sesuai instruksi
pKR = {
    'y': 10.07,
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
}

# Menghitung jumlah asam amino menggunakan List Comprehension
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})

# Inisialisasi variabel pH
pH = 0

# While Loop untuk menghitung net charge dari pH 0 sampai 14
while (pH <= 14):
    netCharge = (
        +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
        for x in ['k','h','r']}.values()))
        -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
        for x in ['y','c','d','e']}.values())))
        
    print('{0:.2f}'.format(pH), netCharge)
    
    # Increment pH agar loop berjalan maju
    pH += 1