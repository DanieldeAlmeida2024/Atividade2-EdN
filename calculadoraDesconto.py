
nome_produto = "Camiseta"
preco_original = 50.00 
porcentagem_desconto = 20 

valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto Aplicado: {porcentagem_desconto}%")
print(f"Valor do Desconto: R$ {valor_desconto:.2f}")
print(f"Preço Final: R$ {preco_final:.2f}")