def cetak_gambar(angka):
    bukan_angka = "Parameter Harus Angka!!"
    genap = "Parameter Harus Ganjil!!"
    if isinstance(angka, int):
        if angka%2!=0:
            for i in range(0, angka):
                for j in range(0, angka):
                    if j==0 or i==(angka/2)-0.5:
                        print("* ",end="")
                    else:
                        print("= ",end="")
                print("* ")
        else:
            return genap
    else:
        return bukan_angka
