import random

print('-='*10, 'GERADOR DE SENHAS', '-='*10)
print()

#listas e variáveis
abcMin = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abcMax = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nums = ['0','1','2','3','4','5','6','7','8','9']
randomMin = ''
randomMax = ''
randomNum = ''
senhaL = []
senhaS = ''

#input do usuário
abcMinNum = int(input("Número de letras minúsculas: "))
abcMaxNum = int(input("Número de letras maiúsculas: "))
numNum = int(input('Número de números: '))

#loops para formar senha em uma lista
for mn in range(abcMinNum):
	randomMin = random.choice(abcMin)
	senhaL.append(randomMin)

for mx in range(abcMaxNum):
	randomMax = random.choice(abcMax)
	senhaL.append(randomMax)

for n in range(numNum):
	randomNum = random.choice(nums)
	senhaL.append(randomNum)

#formatar e mostrar senha pronta
random.shuffle(senhaL)
print('-'*59)
print(f'Senha gerada: {senhaS.join(senhaL)}')