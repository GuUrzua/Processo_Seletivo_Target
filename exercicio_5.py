# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

text = input("Insira o texto: \n")
text_array = []

for i in text:
    text_array.append(i)
    
def reverse_array():
    i = len(text_array) - 1
    inverted_array = []
    while i >= 0:
        inverted_array.append(text_array[i])
        i -= 1
    return inverted_array

def reverse_text():
    inverted_array = reverse_array()
    inverted_text = ''
    for i in inverted_array:
        inverted_text += i
    return inverted_text

print("Texto invertido: ", reverse_text())