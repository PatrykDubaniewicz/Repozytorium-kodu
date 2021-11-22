#wprowadzanie danych
poprawne_dane = False
while(poprawne_dane == False):
    wzor_funkcji = input('Podaj wzór funkcji: ')
    #cyfry
    cyfry = ['0','1','2','3','4','5','6','7','8','9','.']
    znaki_dozwolone = ['0','1','2','3','4','5','6','7','8','9','x','.','+','-','^',' ',',','*']
    poprawne_dane = True
    for i in range(0,len(wzor_funkcji)):
        if(wzor_funkcji[i] not in znaki_dozwolone):
            poprawne_dane = False
    if(poprawne_dane == False):
        print('Wystąpił błąd. Wprowadź ponownie wzór funkcji')

#eliminacja spacji, znaków mnożenia, przecinków
i=0
for letter in range(0,len(wzor_funkcji)):
    if(wzor_funkcji[letter-i]==' '):
        wzor_funkcji = wzor_funkcji[:letter-i] + wzor_funkcji[(letter+1-i):]
        i+=1
    if (wzor_funkcji[letter - i] == '*'):
        wzor_funkcji = wzor_funkcji[:letter - i] + wzor_funkcji[(letter + 1 - i):]
        i += 1
    if (wzor_funkcji[letter - i] == ','):
        wzor_funkcji = wzor_funkcji[:letter - i] + '.' + wzor_funkcji[(letter + 1 - i):]
        i += 1

#dodawanie jedynek
wzor_funkcji += " "
length = len(wzor_funkcji)
pozycje_x = []
for i in range(0,len(wzor_funkcji)):
    if(wzor_funkcji[i]=="x"):
        pozycje_x.append(i)

for element in pozycje_x:
    if(wzor_funkcji[element-1] == '+' or wzor_funkcji[element-1] == '-' or element == 0):
        wzor_funkcji = wzor_funkcji[:(element)] + '1' + wzor_funkcji[(element):]
        for i in range(pozycje_x.index(element),len(pozycje_x)):
            pozycje_x[i]+=1
            i+=1

dictionary = {
    'liczby': [],
    'wykladniki': [],
}
c_wykladnik = ''
c_liczba = ''
#zczytywanie wykładników
for element in pozycje_x:
    if(wzor_funkcji[element+1]=='^'):
        k=2
        while(wzor_funkcji[element+k] != '+' and wzor_funkcji[element+k] != '-' and element+k != len(wzor_funkcji)-1):
            c_wykladnik += wzor_funkcji[element+k]
            k+=1
        dictionary['wykladniki'].append(c_wykladnik)
        c_wykladnik = ''
    else:
        dictionary['wykladniki'].append('1')
        c_wykladnik = ''
#zczytywanie liczb
for element in pozycje_x:
    l=1
    while(wzor_funkcji[element-l] != '+' and wzor_funkcji[element-l] != '-' and l!=0):
        if(element-l == 0):
            c_liczba = wzor_funkcji[element-l] + c_liczba
            l+=1
            break
        c_liczba = wzor_funkcji[element - l] + c_liczba
        l += 1
    if(wzor_funkcji[element-l] =='-'):
        dictionary['liczby'].append('-' + c_liczba)
        c_liczba = ''
    elif(wzor_funkcji[element-l] =='+'):
        dictionary['liczby'].append(c_liczba)
        c_liczba = ''
    else:
        dictionary['liczby'].append(c_liczba)
        c_liczba = ''
#obliczanie pochodnej
pochodna = ''
wartosc = 0
wspolczynnik_liczbowy = 0
for i in range(0,len(dictionary['liczby'])):
    if(dictionary['wykladniki'][i] == '1'):
        wspolczynnik_liczbowy += int(dictionary['liczby'][i])
    else:
        wartosc = int(dictionary['liczby'][i]) * int(dictionary['wykladniki'][i])
        if(i==0):
            pochodna += str(wartosc) + 'x'
        else:
            if(wartosc<0):
                pochodna += str(wartosc) + 'x'
            else:
                pochodna += '+' + str(wartosc) + 'x'
        if(dictionary['wykladniki'][i]>'2'):
            pochodna += '^' + str(int(dictionary['wykladniki'][i]) - 1)
if(wspolczynnik_liczbowy>0):
    pochodna += '+' + str(wspolczynnik_liczbowy)
elif(wspolczynnik_liczbowy<0):
    pochodna += str(wspolczynnik_liczbowy)

if(pochodna[0]=='+'):
    pochodna = pochodna[1:]

if(len(pochodna)==0):
    print('Wartość pochodnej wynosi: 0')
else:
    print('Wartość pochodnej wynosi: ' + pochodna)
