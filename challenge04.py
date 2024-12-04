#challenge04
nodos = [[1,2],[2,3],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16],[17,18],[19,20],[21,22],[23,24],[25,26],[27,28],[31,32],[33,34],[35,36],[37,38],[39,40],[41,42],[43,44],[45,46],[47,48],[49,50],[71,72],[73,74],[75,76],[77,78],[79,80],[81,82],[83,84],[85,86],[87,88],[155,156],[157,158],[175,176],[177,178],[179,180],[181,182],[183,184],[195,196],[197,198],[198, 199],[199,200],[2,4],[4,6],[6,8],[8,10],[10,12]]
posicion_nodos=[False for i in range(len(nodos)-1)]
nodos_nvos=[]
print(nodos)
print(f'Cantidad de nodos {len(nodos)}')
for i in range(len(nodos)-1):
    if nodos[i][1] in nodos[i+1]:
        posicion_nodos[i]=False
    elif nodos[i][0] in nodos[i-1]:
        posicion_nodos[i]=False
    else:
        posicion_nodos[i]=True
    #print(f'posicion {i},')

if nodos[-1][0] in nodos[-2]:
    posicion_nodos.append(False)

for i in range(len(posicion_nodos)):
    if  posicion_nodos[i]:
        nodos_nvos.append(nodos[i][0])
        nodos_nvos.append(nodos[i][1])

print(f'Nodos {posicion_nodos}, cantidad de nodos {len(posicion_nodos)}')
print(f'nodos_nvos {nodos_nvos} y cantidad {len(nodos_nvos)}')
