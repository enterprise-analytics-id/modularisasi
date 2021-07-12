# import geometri.triangle as gt
# print(f'Hitung luas segitiga = {gt.hitung_luas_segitiga(3, 6)}')


from geometri.square import hitung_luas_persegi_panjang, info as info_square
from geometri.triangle import hitung_luas_segitiga, info as info_triangle

print(info_triangle())
print(f"Hitung luas segitiga = {hitung_luas_segitiga(3, 6)}")

print(info_square())
print(f"Hitung luas persegi panjang = {hitung_luas_persegi_panjang(3, 6)}")
