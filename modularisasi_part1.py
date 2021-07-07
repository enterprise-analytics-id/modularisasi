"""
program menghitung luas segitiga
luas segitiga = alas * tinggi / 2
"""

print('menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}\n')

print('menghitung luas segitiga 2 dengan copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}\n')

print('membuat fungsi hitung luas segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(5, 10)}')
print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(6, 15)}')
print(f'menghitung luas segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(3, 5)}')