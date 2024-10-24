def hitung_nilai_mahasiswa():
    
    jumlah_mahasiswa = int(input("Masukkan jumlah data: "))

    data_mahasiswa = []

   
    for i in range(jumlah_mahasiswa):
        nama = input(f"Nama Mahasiswa {i+1}: ")
        nilai = int(input(f"Nilai Mahasiswa {i+1}: "))
        data_mahasiswa.append((nama, nilai))

  
    print("\nDAFTAR NILAI MAHASISWA")
    print("No\tNama\tNilai\tStatus")

   
    total_nilai = sum(nilai for _, nilai in data_mahasiswa)
    jumlah_lulus = sum(1 for _, nilai in data_mahasiswa if nilai >= 60)

   
    for i, (nama, nilai) in enumerate(data_mahasiswa, start=1):
        status = "Lulus" if nilai >= 60 else "Tidak Lulus"
        print(f"{i}\t{nama}\t{nilai}\t{status}")


    rata_rata = total_nilai / jumlah_mahasiswa
    print(f"\nJumlah: {total_nilai}")
    print(f"Nilai Rata-rata: {rata_rata:.2f}")

if __name__ == "__main__":
    hitung_nilai_mahasiswa()
