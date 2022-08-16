# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def new_symbs(symbol, count: int):
    return symbol * count

with open('text1.txt', 'w') as data:
    data.write('gwwwwjjjvvvvvvvvvkddddommmmsa')

with open('text1.txt', 'r') as data:
    text = data.readline()
print(text)

count = 1
result = ''
for i in range (len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        result = result + str(count) + text[i]
        count = 1
if count > 1 or text[- 2] != text[- 1]:
    result = result + str(count) + text[-1]
print(result)


result2 = ''
for i in range (1, len(result)):
    try:
        a = int(result[i-1])
        result2 = result2 + new_symbs(result[i], a)
    except:
        result2 = result2


print(result2)
