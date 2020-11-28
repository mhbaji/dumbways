jumlahKalori = int(input("Jumlah Kalori: "))

def tentukanOlahraga(jumKalori):

    jenisOlahraga=""
    if jumlahKalori > 750:
        jenisOlahraga = "Lari"
    elif jumlahKalori > 500:
        jenisOlahraga = "Badminton"
    else :
        jenisOlahraga = "Renang"

    waktuOlahraga = int(jumlahKalori*2/20)

    print("Jenis Olahraga: ", jenisOlahraga)
    print("Waktu Olahraga: ", waktuOlahraga, " Menit")

tentukanOlahraga(jumlahKalori)