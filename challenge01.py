#Desafío 2: Detectando acceso no deseado
f = open("c:\\path to the file\\log.txt","r")
lineas = f.readlines()
flag_alpha=False
arreglo=[]
salida=[]
cont_valid=0
cont_invalid=0
tipo=''
for line in lineas:
    
    strin=line.strip()
    if strin.isnumeric():
        salida= [True if strin[i]<=strin[i+1]  else False for i in range(len(strin)-1)]
        tipo="numerico"
        salida.append('num')
    elif strin.isalpha():
        salida= [True if strin[i]<=strin[i+1] and strin[i].lower() else False for i in range(len(strin)-1)]
        tipo="alfabetico"
        salida.append('alf')
    else: #casos de caracteres con numeros
        salida=[]
        tipo="numerico y alfabetico"
        salida.append('mix')
        flag_alpha=False
        for i in range(len(strin)-1):
            if i==0 and strin[i].isalpha():
                flag_alpha=True
  
            if strin[i+1].isalpha(): 
                if strin[i+1].islower():
                    if strin[i]<=strin[i+1]:
                        salida.append(True) #el siguiente caracter es mayor
                    else: 
                        salida.append(False) 
                else:
                    salida.append(False)
            elif strin[i+1].isnumeric():
                if flag_alpha and (not strin[i].isalpha()):
                    salida.append(False)
                elif strin[i]<=strin[i+1] and not strin[i].isalpha(): 
                    salida.append(True)
                else:
                    salida.append(False)
    
    if all(salida):
       cont_valid+=1
       print(f'--> El string es {tipo} y es valido--> {line}')
    else:
       cont_invalid+=1
       print(f'--> El string es {tipo} y es "\033[0;31m" invalido--> {line} "\033[0;37m"')
#imprimir lista
print(f'\nCantidad de intentos validos {cont_valid} \n Cantidad de intentos invalidos{cont_invalid}')


