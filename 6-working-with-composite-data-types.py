# mport modul yang diperlukan
import csv
import copy

# Definisikan kerangka (schema) untuk kendaraan. 
# Ini adalah Dictionary kosong sebagai template.
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Loop ini hanya untuk menunjukkan isi awal dictionary (kosong)
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))

# Buat List kosong untuk menampung semua data mobil nantinya
myInventoryList = []

# Membaca file CSV dan memasukkannya ke dalam memory
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  
    lineCount = 0  
    
    for row in csvReader:
        if lineCount == 0:
            # Baris pertama adalah Header (judul kolom)
            print(f'Column names are: {", ".join(row)}')  
            lineCount += 1  
        else:  
            # Baris selanjutnya adalah data mobil
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            
            # PENTING: Membuat salinan mendalam (Deep Copy) dari template myVehicle
            # Agar setiap mobil punya "kotak penyimpanan" sendiri di memori.
            currentVehicle = copy.deepcopy(myVehicle)  #pakai deepcopy untuk nested object tapi disini pakai copy.copy disini sudah aman sebenarnya
            # currentVehicle = copy.copy(myVehicle) # ini bisa dipakai disini tapi lab memberikan default ke deepcopy
            
            # Mengisi data ke dalam dictionary sementara
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            
            # Menambahkan dictionary yang sudah terisi ke dalam List utama
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
            
    print(f'Processed {lineCount} lines.')
    
print(myInventoryList)

# Mencetak hasil akhir dari List Inventory
print("-----------------")
print("Printing Inventory:")
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key,value))
    print("-----")
    
    
    
##### Penjelasan #####
# copy (copy biasa) dengan library copy= digunakan untuk int, string, bool, float

# Copy.deepcopy (copy istimewa) dengan library copy = digunakan untuk kasus variable dengan tipe : list, tuple, dictionary yang bersifat nested/complex (composite di dalam composite)
