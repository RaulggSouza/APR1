#Uma determinada loja está fazendo promoções de vendas. 
#Qualquer compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. 
#Se a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto será de 10%. 
#Se for superior ou igual a R$ 200,00, o desconto será de 20%.
#Faça um programa que leia o quanto o cliente gastou e escreva o valor da conta já com os descontos
compra = float(input("Digite o valor total da compra: "))
if compra <= 100.00:
    preco_final = compra - compra*0.05
elif compra > 100.00 and compra < 200.00:
    preco_final = compra - compra*0.1
else:
    preco_final = compra - compra*0.2
print(f'O preço final da compra, com descontos aplicados, é de {preco_final}')