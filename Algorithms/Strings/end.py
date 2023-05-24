frase = 'Lucas Emanuel'
# Pego o tamanho da frase
print(len(frase))
# Conta quantas vezes um determinado carater apareceu
print(frase.count('u'))
# Conta a ocorrencia do 2 do indice zero ao indice 10-1
print(frase.count('u',0,10))
# Verifico aonde de iniciou essa ocorrencia
print(frase.find('Ema'))
# Aqui verifico se existe algum zezinho, como n existe, retorna -1
print(frase.find('zezinho'))
# Aqui estou verificando se existe '13' na sequencia, se tive return true e entra na condição do if
a = str(input())

if '13' in a:
    print(f'{a} es de Mala Suerte')
else:
    print(f'{a} No es de Mala Suerte')
