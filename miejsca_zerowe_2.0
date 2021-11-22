def ObliczWartoscFunkcji(x):
    wartosc = 0
    error = False
    for i in range(0,len(dictionary['liczby'])):
        if (float(dictionary['wykladniki'][i]) <= 0 and x == 0):
            wartosc = 1000
            error = True
        else:
            wartosc += float(dictionary['liczby'][i]) * x ** float(dictionary['wykladniki'][i])
    if not error:
        wartosc+= wspolczynnik_liczbowy
    return wartosc

def CzyRozneZnaki(a,b):
    if(a!=0 and b!=0):
        if(a>0):
            if(b>0):
                return False
            else:
                return True
        else:
            if(b>0):
                return True
            else:
                return False
    else:
        return 0

def WybierzPrzedział(a,b):
    if(CzyRozneZnaki(a,b) == True):
        return 1
    else:
        return 2

#wprowadzanie danych
poprawne_dane = False
while(poprawne_dane == False):
    wzor_funkcji = input('Podaj wzór funkcji: ')
    zakres_a = input('Podaj dolną granicę: ')
    zakres_b = input('Podaj górną granicę: ')
    #cyfry
    cyfry = ['0','1','2','3','4','5','6','7','8','9','.']
    cyfry_bez_kropki = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
        c_wykladnik += wzor_funkcji[element + 2]
        k=3
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
    if(wzor_funkcji[i] in cyfry_bez_kropki):
        if((wzor_funkcji[i-1]!='^' and (wzor_funkcji[i-2]!='^' or wzor_funkcji[i-1]!='-')) or wzor_funkcji[i]==0):
            pozycje_cyfr.append(i)

c_liczba_wolna = ''
for cyfra in pozycje_cyfr:
    if(wzor_funkcji[cyfra+1]=='+' or wzor_funkcji[cyfra+1]=='-' or wzor_funkcji[cyfra+1]==' '):
        c_liczba_wolna += wzor_funkcji[cyfra]
        m = 1
        while (wzor_funkcji[cyfra-m] != '+' and wzor_funkcji[cyfra-m] != '-' and cyfra-m != -1 and wzor_funkcji[cyfra-m] != '^'):
            c_liczba_wolna = wzor_funkcji[cyfra-m] + c_liczba_wolna
            m+=1

        if (wzor_funkcji[cyfra-m] == '-'):
            dictionary['wolne_liczby'].append('-' + c_liczba_wolna)
            c_liczba_wolna = ''
        elif (wzor_funkcji[cyfra-m] == '+'):
            dictionary['wolne_liczby'].append(c_liczba_wolna)
            c_liczba_wolna = ''
        elif (wzor_funkcji[cyfra - m] == '^'):
            break
        else:
            dictionary['wolne_liczby'].append(c_liczba_wolna)
            c_liczba_wolna = ''

miejsca_zerowe = []
wspolczynnik_liczbowy = 0
for n in range(0,len(dictionary['wolne_liczby'])):
    wspolczynnik_liczbowy += float(dictionary['wolne_liczby'][n])

#znajdywanie przedziałów monotnoiczności
liczba_podzialow = 10000
jednostka = (abs(float(zakres_b)) + abs(float(zakres_a)))/liczba_podzialow
x = float(zakres_a)
a_list = []
b_list = []
nw = 1
ca = float(zakres_a)
cb = float(zakres_a)

if(ObliczWartoscFunkcji(x)>ObliczWartoscFunkcji(x+jednostka)):
    nw=0

warunek = 0
for i in range(int(zakres_a),int(zakres_b)):
    if(ObliczWartoscFunkcji(i)==0):
        warunek+=1
if (warunek>=(abs(int(zakres_a))+abs(int(zakres_b)))-1):
    nw = 2

while(x<=float(zakres_b)):
    if(nw == 1):
        while(ObliczWartoscFunkcji(x+jednostka)>=ObliczWartoscFunkcji(x) and x<= float(zakres_b)):
            x+=jednostka
            cb+=jednostka
        a_list.append(round(ca*100)/100)
        b_list.append(round(cb*100)/100)
        ca = cb
        nw = 0
    elif(nw == 0):
        while(ObliczWartoscFunkcji(x+jednostka)<=ObliczWartoscFunkcji(x) and x<= float(zakres_b)):
            x+=jednostka
            cb+=jednostka
        a_list.append(round(ca*100)/100)
        b_list.append(round(cb*100)/100)
        ca = cb
        nw = 1
    else:
        x+=jednostka

for i in range(0,len(a_list)):
    a = a_list[i]
    b = b_list[i]
    mid = (a+b)/2
    war_mid = ObliczWartoscFunkcji(mid)
    war_a = ObliczWartoscFunkcji(a)
    war_b = ObliczWartoscFunkcji(b)

    if(CzyRozneZnaki(war_a,war_b) == True):
        while(abs(war_mid)>0.0001):
            mid = (a+b)/2
            war_mid = ObliczWartoscFunkcji(mid)
            war_a = ObliczWartoscFunkcji(a)
            war_b = ObliczWartoscFunkcji(b)
            if(WybierzPrzedział(war_a,war_mid)==1):
                b = mid
            else:
                a = mid
        miejsca_zerowe.append(mid)
    else:
        if(ObliczWartoscFunkcji(a)==0):
            miejsca_zerowe.append(a)
        if(ObliczWartoscFunkcji(b)==0):
            miejsca_zerowe.append(b)


#wyświetlanie wyników
elementy = []
for element in miejsca_zerowe:
    if(miejsca_zerowe.count(element)>1):
        miejsca_zerowe.remove(element)
    else:
        element = round(element*1000)/1000
        elementy.append(element)
        if(element%1==0):
            elementy.remove(element)
            element = str(element)
            element = element[:-2]
            element = int(element)
            elementy.append(element)




if(len(miejsca_zerowe) == 0):
    if(ObliczWartoscFunkcji(x)!=0):
        print('ta funkcja nie ma miejsc zerowych w tym przedziale')
    else:
        print('ta funkcja ma nieskonczenie wiele miejsc zerowych')
else:
    print('Miejsca zerowe funkcji w tym przedziale to: ')
    for element in elementy:
        print(element)

