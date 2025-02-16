def salambye(name):
    print('salam',name)
    print('bye bye',name)

salambye('jadi')
salambye('javad')


def jam(a,b):
    javab = a+b
    return javab

adade_aval = 4
adade_dovvom = 5
jam_2_adad = jam(adade_aval,adade_dovvom)

print(jam_2_adad)

def hoghoogh(hour,per_hour):
    if hour>8:
        return 'error! too much work!'
    else:
        kolle_daramad = hour * per_hour
        return kolle_daramad
print(hoghoogh(16,2))
