file = open("path to file txt",'r')
lines = file.readlines()
sumaPasos=0
for l in lines:
    linea= l.strip()
    print(f'{linea}  ')
    line=linea.split(' ')
    elements = len(line) 
    flagExit=False
    i=0 #indice
    pasos=0
    while i < elements and not flagExit:
        if i == 0 and int(line[i]) < 0:
                line[i]=int(line[i]) + 1
                pasos +=1
                break
        else:
            if i >=0 and i <= elements :
                if int(line[i])==0:
                    line[i]=int(line[i]) + 1
                    pasos+=1
                elif int(line[i]) > 0:
                    pasos+=1
                    aux = int(line[i]) 
                    line[i] = int(line[i])+1
                    i+=aux
                    if i < 0 or i > elements :
                        flagExit = True
                elif int(line[i]) < 0:
                    pasos+=1
                    aux = int(line[i]) 
                    line[i] = int(line[i])+1
                    i+=aux
                    if i < 0 or i > elements :
                        flagExit = True
            else:
                flagExit = True
    print(f"{line} --> Omega salio en {pasos} pasos")
    sumaPasos+=pasos
print(f'solucion: submit {sumaPasos}-{pasos}')
