# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

with open('text.txt', 'w') as data:
    data.write('12абв абв +1 kljhабвds hi 5jxdабв1 ljgdebz')

with open('text.txt', 'r') as data:
    words = data.readline()
print(words)

new_words = list(filter(lambda x: 'абв' not in x, words.split()))
print(new_words)

    