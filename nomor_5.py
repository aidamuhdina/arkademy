def sequence(x,y):
    deret = [y]
    i = 0
    xkecil = "parameter x HARUS lebih besar daripada y!!"
    bukan_angka = "Parameter HARUS angka!!"
    if isinstance(x,int) and isinstance(y,int):
        if x>y:
            while (deret[-1]>1):
                deret.append((deret[i]**2)%(x+i))
                i+= 1
            return deret
        else:
            return xkecil
    else:
        return bukan_angka
