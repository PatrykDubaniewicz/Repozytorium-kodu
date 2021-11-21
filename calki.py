#wprowadzanie danych
poprawne_dane = False
while(poprawne_dane == False):
    wzor_funkcji = input('Podaj wzór funkcji: ')
    zakres_a = input('Podaj dolną granicę: ')
    zakres_b = input('Podaj górną granicę: ')
    #cyfry
    cyfry = ['0','1','2','3','4','5','6','7','8','9','.']
    znaki_dozwolone = ['0','1','2','3','4','5','6','7','8','9','x','.','+','-','^',' ',',','*']
    poprawne_dane = True
    for i in range(0,len(wzor_funkcji)):
        if(wzor_funkcji[i] not in znaki_dozwolone):
            poprawne_dane = False
    for i in range(0,len(zakres_a)):
        if(zakres_a[i] not in znaki_dozwolone):
            poprawne_dane = False
    for i in range(0,len(zakres_b)):
        if(zakres_b[i] not in znaki_dozwolone):
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
    'wolne_liczby': []
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
#zczytywanie wolnych liczb
pozycje_cyfr = []
for i in range(0,len(wzor_funkcji)):
    if(wzor_funkcji[i] in cyfry):
        if(wzor_funkcji[i-1]!='^'):
            pozycje_cyfr.append(i)

c_liczba_wolna = ''
for cyfra in pozycje_cyfr:
    if(wzor_funkcji[cyfra+1]=='+' or wzor_funkcji[cyfra+1]=='-' or wzor_funkcji[cyfra+1]==' '):
        c_liczba_wolna += wzor_funkcji[cyfra]
        m = 1
        while (wzor_funkcji[cyfra-m] != '+' and wzor_funkcji[cyfra-m] != '-' and cyfra-m != -1):
            c_liczba_wolna = wzor_funkcji[cyfra-m] + c_liczba_wolna
            m+=1

        if (wzor_funkcji[cyfra-m] == '-'):
            dictionary['wolne_liczby'].append('-' + c_liczba_wolna)
            c_liczba_wolna = ''
        elif (wzor_funkcji[cyfra-m] == '+'):
            dictionary['wolne_liczby'].append(c_liczba_wolna)
            c_liczba_wolna = ''
        else:
            dictionary['wolne_liczby'].append(c_liczba_wolna)
            c_liczba_wolna = ''

#obliczanie całki oznaczonej
wspolczynnik_liczbowy = 0
for n in range(0,len(dictionary['wolne_liczby'])):
    wspolczynnik_liczbowy += float(dictionary['wolne_liczby'][n])

liczba_prostokatow = 20000
x = float(zakres_a)
calka = 0
h_prostokata = 0
a_prostokata = abs(float(zakres_b)-float(zakres_a))/liczba_prostokatow
while(x<=float(zakres_b)):
    for p in range(0,len(dictionary['liczby'])):
        h_prostokata += float(dictionary['liczby'][p]) * (x ** float(dictionary['wykladniki'][p]))
    h_prostokata += wspolczynnik_liczbowy
    calka += h_prostokata * a_prostokata
    h_prostokata = 0
    x += a_prostokata

if(len(pozycje_x)==0):
    calka = abs(float(zakres_b)-float(zakres_a))*wspolczynnik_liczbowy

print("Wartość całki wynosi: " + str(calka))



