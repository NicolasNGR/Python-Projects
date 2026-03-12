# limite da mochila
limite = 23

# lista para guardar os itens
itens = []

# peso total
peso_total = 0

# nome do mochileiro
nome = input("Digite o nome do mochileiro: ")

while True:
    
    item = input("\nDigite o nome do item (ou 'fim' para encerrar): ")
    
    if item.lower() == "fim":
        break
    
    peso = float(input("Digite o peso do item em kg: "))
    
    # verificar se ainda cabe na mochila
    if peso_total + peso <= limite:
        itens.append((item, peso))
        peso_total += peso
        print("Item adicionado com sucesso!")
    else:
        print("Não há espaço suficiente na mochila!")

# cálculo do espaço restante
espaco_restante = limite - peso_total

# resultado final
print("\n----- RESUMO DA MOCHILA -----")
print("Mochileiro:", nome)
print("Peso total:", peso_total, "kg")
print("Espaço restante:", espaco_restante, "kg")

print("\nItens na mochila:")
for item, peso in itens:
    print("-", item, "-", peso, "kg")