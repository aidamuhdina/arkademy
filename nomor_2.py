def usernameValidity(name):
    import re
    if isinstance(name, str):
        if len(name)>4 and len(name)<13:
            pertama = re.search("\A[a-z|_]",name)
            cek_simbol = re.findall("\W",name)
            if (pertama) and len(cek_simbol)==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def passValidity(password):
    import re
    huruf = []
    if isinstance(password, str):
        if len(password)==7:
            angka = re.findall("\d",password)
            simbol = re.findall("\W",password)
            underscore = re.findall("[_]",password)
            huruf = re.findall("[A-Z]",password)
            if len(angka)==1 and (len(simbol)==1 or len(underscore)==1) and len(huruf)==5:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
