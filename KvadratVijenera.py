'''
Лаб. работы №1 - Шифр Виженера
Выполнила: Камскова Алина
Гр. Пи - 41(э)
алфавит написан заглавными так что слово и ключ тоже нужно вводить заглавными
'''

        #   0  1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  28  30  31  32  33
alfavit = ['','А','Б','В','Г','Д','Е','Ё','Ж','З','И','Й','К','Л','М','Н','О','П','Р','С','Т','У','Ф','Х','Ц','Ч','Ш','Щ','Ъ','Ы','Ь','Э','Ю','Я']

word = input("cлово: ")
key = input("ключ: ")

key *= len(word)//len(key) + 1   #Определяем длину ключа под длину сообщения

NumWord = []    #нумерация букв по алфавиту у шифруемого слова
NumKey = []     #нумерация букв по алфавиту у ключа
Sum = []        #сумма нумераций
Shifr = []      #полученный шифр
DeSum = []      #cписок индексов для дешифровки
DeShifr = []    #cписок с исходным расшифрованным словом

''' ШИВРОВАНИЕ '''

for j in range(len(word)):                  # получаем индексы шифруемого слова
    for i in range(len(alfavit)):
        if word[j] == alfavit[i]:
            NumWord.append(i)
print(NumWord)

for j in range(len(key)):                   # получаем индексы ключа
    for i in range(len(alfavit)):
        if key[j] == alfavit[i]:
            NumKey.append(i)
print(NumKey)

while len(NumWord) < len(NumKey):           # делаем списки равной длины
    NumKey.pop(len(NumKey) - 1)
print(NumKey)

for i in range(0, len(NumWord)):            # Определяем индексы букв шифра
    S = NumKey[i] + NumWord[i]
    if S > (len(alfavit) - 1):
        S = S - (len(alfavit) - 1)
        Sum.append(S)
    else:
        Sum.append(NumKey[i] + NumWord[i])
print(Sum)

for j in range(len(Sum)):                   # Сопоставляем индексы с буквами в исходном алфавите
    for i in range(len(alfavit)):
        if i == Sum[j]:
            Shifr.append(alfavit[i])
print(Shifr)
print()
print("Полученный шифр", " ".join(map(str, Shifr)))
print()

'''ДЕШИФРОВАНИЕ'''

# NumKey Sum
for i in range(len(Sum)):                    # Получаем индексы шифруемого слова
    if Sum[i] < NumKey[i]:
        D = Sum[i] + (len(alfavit) - 1) - NumKey[i]
        DeSum.append(D)
    else:
        DeSum.append(Sum[i] - NumKey[i])
print(DeSum)

for j in range(len(Sum)):                   # Сопоставляем индексы с буквами в исходном алфавите
    for i in range(len(alfavit)):
        if i == DeSum[j]:
            DeShifr.append(alfavit[i])
print(DeShifr)
print()
print("Расшифрованное слово", " ".join(map(str, DeShifr)))











    









