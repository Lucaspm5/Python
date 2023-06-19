n = input()
vogal = "aeiou"
new_string = ""
for letra in n:
    if letra not in vogal:
        new_string += letra
print(new_string)
