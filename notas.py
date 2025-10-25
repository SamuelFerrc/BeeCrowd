dinheiro = int(input())
inicial = dinheiro
cem = int(dinheiro/100)
dinheiro = dinheiro % 100
ciquenta = int(dinheiro/50)
dinheiro = dinheiro%50
vinte = int(dinheiro/20)
dinheiro = dinheiro % 20
dez = int(dinheiro/10)
dinheiro = dinheiro%10
cinco  = int(dinheiro/5)
dinheiro = dinheiro%5
dois = int(dinheiro/2)
dinheiro = dinheiro%2
um = dinheiro

print(inicial)
print(f"{cem} nota(s) de R$ 100,00")
print(f"{ciquenta} nota(s) de R$ 50,00")
print(f"{vinte} nota(s) de R$ 20,00")
print(f"{dez} nota(s) de R$ 10,00")
print(f"{cinco} nota(s) de R$ 5,00")
print(f"{dois} nota(s) de R$ 2,00")
print(f"{um} nota(s) de R$ 1,00")
