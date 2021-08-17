def mostatil(width,height,vahed='Metre'):
    if vahed=='Metre':
        masahat=(width*height)
        return masahat
    elif vahed=='centimetre':
        width1=width/100
        height1=height/100
        masahat=(width1*height1)
        return masahat
m=mostatil(3,3,'Metre')
print(m)
