def input_nilai():
    jumlah = int(input("Masukkan jumlah mahasiswa: "))
    nama_mahasiswa = []
    nilai_mahasiswa = []

    for i in range(jumlah):
        print("\nMahasiswa ke-", i + 1)
        nama = input("Nama mahasiswa: ")
        nilai = float(input("Nilai mahasiswa (0-100): "))

        while nilai < 0 or nilai > 100:
            print("Nilai harus antara 0 sampai 100.")
            nilai = float(input("Masukkan nilai lagi: "))

        nama_mahasiswa.append(nama)
        nilai_mahasiswa.append(nilai)

    return nama_mahasiswa, nilai_mahasiswa


def tentukan_status(nilai):
    if nilai >= 75:
        return "Lulus"
    else:
        return "Tidak Lulus"


def hitung_rata_rata(nilai_mahasiswa):
    total = 0
    for nilai in nilai_mahasiswa:
        total += nilai

    return total / len(nilai_mahasiswa)


def tampilkan_hasil(nama_mahasiswa, nilai_mahasiswa):
    print("\n=== HASIL NILAI MAHASISWA ===")
    for i in range(len(nama_mahasiswa)):
        status = tentukan_status(nilai_mahasiswa[i])
        print(nama_mahasiswa[i], "-", nilai_mahasiswa[i], "-", status)

    rata_rata = hitung_rata_rata(nilai_mahasiswa)
    print("Rata-rata kelas:", round(rata_rata, 2))


def main():
    nama_mahasiswa, nilai_mahasiswa = input_nilai()
    tampilkan_hasil(nama_mahasiswa, nilai_mahasiswa)


if __name__ == "__main__":
    main()
