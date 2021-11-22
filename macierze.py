macierz = []
for i in range(1,10):
    macierz.append(float(input('podaj ' + str(i) + ' element macierzy: ')))
 
wyznacznik = 0
wyznacznik += macierz[0]*macierz[4]*macierz[8]+macierz[1]*macierz[5]*macierz[6]+macierz[2]*macierz[3]*macierz[7]
wyznacznik = wyznacznik - macierz[1]*macierz[3]*macierz[8]-macierz[0]*macierz[5]*macierz[7]-macierz[2]*macierz[4]*macierz[6]
 
print('Wyznacznik macierzy wynosi: ' + str(wyznacznik))
