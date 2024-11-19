#Desafío 1: ¡Consigue acceso a la terminal!
code = [5,2,8,9,3,4,7,1,2,8,3,4]
mover = 'URDURUDRUDLLLLUUDDUDUDUDLLRRRR'

print("Current code: "code)
posicion=0
for m in mover:
    if m=='U':
        if code[posicion]==9:
            code[posicion]=0
        else:
            code[posicion]+=1
    elif m=='D':
        if code[posicion]==0:
            code[posicion]=9
        else:
            code[posicion]-=1
    elif m=='R':
        if posicion < len(code):
            posicion+=1
        else:
            posicion=0
    elif m=='L':
        if posicion > 0:
            posicion-=1
        else:
            posicion=len(code)-1
print("New code: "code)
