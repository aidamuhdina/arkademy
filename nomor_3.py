def cek_kata(kataIn):
    import re
    bukanKata = "Parameter harus string!"
    if isinstance(kataIn,str):
        kata_kata = re.split("\s",kataIn)
        for i in range(len(kata_kata)-1):
            cari_simbol = re.findall("\W",kata_kata[i])
            cari_angka = re.findall("\d", kata_kata[i])
            kata_baru = kata_kata.copy()
            if len(cari_angka)==0 and len(cari_simbol)==0:
                continue
            else:
                kata_baru.pop(i)
        total=len(kata_kata)
        total_kata=len(kata_baru)
        slash = "{}/{}"
        disp = slash.format(total_kata,total)
        return disp
    else:
        return bukanKata
