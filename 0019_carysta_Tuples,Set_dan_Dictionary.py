print("====== 1. TUPLE ======")

print("A.")
mahasiswa = ("Carysta", "2605060019", "Teknologi Informasi")
print(mahasiswa)

print("B.")
print("NIM:", mahasiswa[1])
print("prodi:", mahasiswa[2])

print("C.")
mahasiswa[2] = "Teknologi Informasi"
print(mahasiswa) 
#eror karena pada tuple data yang dibuat tidak bisa diubah

print("D.")
nilai_angka= {10, 4, 3, 2, 4, 10, 7, 5}
print(nilai_angka)
#angka 10 dan 4 yg ditulis 2 kali hanya disimpan satu kali karena set memiliki elemen unik atau tidak menerima duplikasi

print("====== 2. MANIPULASI DICTIONARY ======")

print("A.")
data_mahasiswa = {
    "nim": "240101",
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa)

print("B.")
#mengubah nilai prodi
data_mahasiswa["prodi"] = "Sastra Mesin"
print(data_mahasiswa)

#menambahkan key angkatan
data_mahasiswa.update({"angkatan": 2026})
print(data_mahasiswa)

print("C.")
#menghapus data nim
del data_mahasiswa["nim"]
print(data_mahasiswa)

print("====== 3. PERULANGAN PADA DICTIONARY ======")

print("A.")
keranjang = {
    "apel": 5000,
    "pisang": 3000,
    "jeruk": 7000,
    "anggur": 15000
}
print(keranjang)

print("B.")
#menampilkan barang dan harga
for buah, harga in keranjang.items():
    print(f"harga {buah}: Rp {harga}")

print("C.")
#menampilkan total belanja
total = 0

for harga in keranjang.values():
    total += harga

print("total belanja: Rp", total)