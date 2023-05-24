frase = 'Lucas emanuel Lucas'
# Retorna true or false
auxiliary = 'uct' in frase

if auxiliary:
    print(f'uc existe em {frase}')
else:
    print('Não existe')

# Transforma em maiusculo
print(frase.upper())
# Transforma em minusculo
print(frase.lower())
# Ver quantas palavras especificadas existem
print(frase.count('a'))
# Verifica aonda ouve a primeira ocorrencia do 'a'
print(frase.find('a'))
# Exclui os primeiros e ultimos espaços vazios
print(frase.strip())
# Divide a frase em varias listas, aonde tiver ' ' <- espaços
print(frase.split())
# Estou ajuntando novamente as frases
print(''.join(frase))
# Escrevo do indice 1 ao final da string saltando de 2 em 2
print(frase[1::2])
# Substituo a frase Lucas por emanuel
print(frase.replace('Lucas','emanuel'))