import datetime as date

# Input pengguna
nama = input("Masukkan nama anda: ")
nim = input("Masukkan nim anda: ")
tempat_lahir = input("Masukkan tempat lahir: ")
tanggal_lahir = int(input("Masukkan tanggal lahir (1-31): "))
bulan_lahir = int(input("Masukkan bulan lahir (1-12): "))
tahun_lahir = int(input("Masukkan tahun lahir: "))

# Tanggal lahir
dob = date.datetime(tahun_lahir, bulan_lahir, tanggal_lahir)

# Tanggal sekarang
current_date = date.datetime.now()

# Menghitung umur
age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

# Hasil dari print
print("\nData Pribadi:")
print("Nama:", nama)
print("NIM:", nim)
print("Tempat Lahir:", tempat_lahir)
print("Tanggal Lahir:", tanggal_lahir)
print("Bulan Lahir:", bulan_lahir)
print("Tahun Lahir:", tahun_lahir)
print("Umur:", age, "tahun")
