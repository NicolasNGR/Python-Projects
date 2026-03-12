def eh_primo(numero):
    
    if numero < 2:
        return False
    
    divisor = 2
    
    while divisor <= numero // 2:
        if numero % divisor == 0:
            return False
        divisor += 1
        
    return True


inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

contador = 0
menor_primo = None
maior_primo = None

numero = inicio

while numero <= fim:
    
    if eh_primo(numero):
        contador += 1
        
        if menor_primo is None:
            menor_primo = numero
            
        maior_primo = numero
        
    numero += 1


print("\nResultado:")
print("Quantidade de primos:", contador)

if contador > 0:
    print("Menor primo:", menor_primo)
    print("Maior primo:", maior_primo)
else:
    print("Nenhum número primo encontrado no intervalo.")