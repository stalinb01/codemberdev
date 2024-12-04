#desafio 5, determinar si un numero es primo y la suma de sus digitos som primos. 
#esta lista de nodos viene del desafio 4 (challenge04)
nodos=[13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,155,156,157,158,175,176,177,178,179,180,181,182,183,184,195,196]
tercero=0
todos=0
lista_prime=[]
def is_prime(n):
    cont=0
    for i in range(2,n-1):
        if n%i == 0:
          cont+=1
    if cont==0:
        return True
    else:
        return False
for i in range(len(nodos)):
    suma=0
    if is_prime(nodos[i]):
        if len(str(nodos[i])) > 1:
            for j in range(len(str(nodos[i]))):
                suma += int(str(nodos[i])[j])
        else:
            suma+=nodos[i]
        if is_prime(suma):
            lista_prime.append(nodos[i])
        #    print(f'Numero primo y la suma de los digitos este numero es primo: {nodos[i]}')
        #else:
        #    print(f'Numero primo, pero la suma de los digitos este numero no es primo: {nodos[i]}')
print(f'La lista de numeros es: {lista_prime}, \nel tercer numero es {lista_prime[2]} y la cantidad  de elementos es: {len(lista_prime)}.\nenviar "submit {lista_prime[2]}-{len(lista_prime)}"')
