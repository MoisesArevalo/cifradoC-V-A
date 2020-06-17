from math import ceil, gcd
abc=[chr(i).upper() for i in range(97,123)]
def inv(a,n):
    i=0
    if gcd(n,a) ==1:
        while(i<n and (a*i % n)!=1):
            i+=1
    else:
        return 'No existe inv'
    return i

def cifraCesar(texto):
    cifrado = ''
    for t in texto:
        cifrado += '|' if t==' ' else  abc[(abc.index(t)+3)%len(abc)]
    return cifrado.lower()

def cifraAfin(texto,a=3,b=5):
    cifrado = ''
    for t in texto:
        cifrado += '|' if t==' ' else  abc[(a*abc.index(t)+b)%len(abc)]
    return cifrado.lower()
def cifraVigenere(texto,clave='IDEA'):
    cifrado = ''
    clave = clave *ceil(len(texto)/len(clave))
    for (t,c) in zip(texto,clave):
        cifrado += '|' if t==' ' else  abc[(abc.index(t)+ abc.index(c))%len(abc)]
    return cifrado.lower()
###### METODOS PARA DECIFRAR
def decifrarCesar(texto):
    decifrado =''
    for t in texto:
        decifrado += ' ' if t=='|' else  abc[(abc.index(t)-3)%len(abc)]
    return decifrado.lower()

def decifrarAfin(texto,a=3,b=5):
    decifrado = ''
    for t in texto:
        
        decifrado += ' ' if t=='|' else  abc[((abc.index(t)-b)*inv(a,len(abc)))%len(abc)]
    return decifrado.lower()

def decifrarVigenere(texto,clave='IDEA'):
    decifrado = ''
    clave = clave *ceil(len(texto)/len(clave))
    for (t,c) in zip(texto,clave):
        decifrado += ' ' if t=='|' else  abc[(abc.index(t)- abc.index(c))%len(abc)]
    return decifrado.lower()
print()