def GetFilteredDimensions(parameter_array):
    return [i for i in parameter_array if i != "0"]

def Write_4_1_ResultsToFile(filename, dictionary):
    file_wynik4_1 = open(filename , "w")
    for key in dictionary:
        file_wynik4_1.write(key + " " + str(dictionary[key]) + "\n")
    file_wynik4_1.close()

def Write_4_2_ResultsToFile(filename, dictionary_count, dictionary_surface):
    file_wynik4_2a = open(filename, "w")
    for key in dictionary_count:
        file_wynik4_2a.write(key + " " + str(dictionary_surface[key]) + " " + str(dictionary_count[key]) + "\n")
    file_wynik4_2a.close()

def Write_4_2_b_ResultsToFile(filename, biggest, smallest, dictionary):
    file_wynik4_2b = open(filename, "w")
    file_wynik4_2b.write(biggest + " " + str(dictionary[biggest]) + "\n")
    file_wynik4_2b.write(smallest + " " + str(dictionary[smallest]) + "\n")
    file_wynik4_2b.close()

def Write_4_3_ResultsToFile(filename, most, least, dictionary_different_stores):
    file_wynik4_3 = open(filename, "w")
    file_wynik4_3.write(most + " " + str(dictionary_different_stores[most]) + "\n")
    file_wynik4_3.write(least + " " + str(dictionary_different_stores[least]))
    file_wynik4_3.close()


filepath_galerie = "galerie.txt"
file_galerie = open(filepath_galerie)

CountryGalleriesCountDictionary = {}
CityGalleriesSurface = {}
CityGalleriesStoresCount = {}
CityGalleriesDifferentShops = {}
MostDifferentStores = "MostInitial"
LeastDifferentStores = "LeastInitial"

BiggestSurfaceValue = 0
SmallestSurfaceValue = 99999999
BiggestSurface = ""
SmallestSurface = ""


CityGalleriesDifferentShops[MostDifferentStores] = 0
CityGalleriesDifferentShops[LeastDifferentStores] = 9999

for line in file_galerie:
    galerie_parameters = line.split()
    current_country = galerie_parameters.pop(0)
    current_city = galerie_parameters.pop(0)
    filtered_dimensions = GetFilteredDimensions(galerie_parameters)

    #zadanie 4.1
    if current_country in CountryGalleriesCountDictionary:
        CountryGalleriesCountDictionary[current_country] += 1
    else:
        CountryGalleriesCountDictionary[current_country] = 1

    #zadanie 4.2
    CityGalleriesStoresCount[current_city] = len(filtered_dimensions)/2

    TotalGallerySurface = 0

    StoreSurfaceDictionary = {}

    while len(filtered_dimensions) > 0:
        width = filtered_dimensions.pop(0)
        height = filtered_dimensions.pop(0)
        store_surface = int(width) * int(height)
        TotalGallerySurface += store_surface

        if store_surface in StoreSurfaceDictionary:
            StoreSurfaceDictionary[store_surface] += 1
        else:
            StoreSurfaceDictionary[store_surface] = 1

    CityGalleriesSurface[current_city] = int(TotalGallerySurface)

    if CityGalleriesSurface[current_city] > BiggestSurfaceValue:
        BiggestSurface = current_city
        BiggestSurfaceValue = CityGalleriesSurface[current_city]

    if CityGalleriesSurface[current_city] < SmallestSurfaceValue:
        SmallestSurface = current_city
        SmallestSurfaceValue = CityGalleriesSurface[current_city]

    CityGalleriesDifferentShops[current_city] = len(StoreSurfaceDictionary)

    if int(CityGalleriesDifferentShops[current_city]) > int(CityGalleriesDifferentShops[MostDifferentStores]):
        MostDifferentStores = current_city

    if int(CityGalleriesDifferentShops[current_city]) < int(CityGalleriesDifferentShops[LeastDifferentStores]):
        LeastDifferentStores = current_city



Write_4_1_ResultsToFile("wynik4_1.txt", CountryGalleriesCountDictionary)
Write_4_2_ResultsToFile("wynik4_2a.txt", CityGalleriesStoresCount, CityGalleriesSurface)
Write_4_2_b_ResultsToFile("wynik4_2b.txt", BiggestSurface, SmallestSurface, CityGalleriesSurface)
Write_4_3_ResultsToFile("wynik4_3.txt", MostDifferentStores, LeastDifferentStores, CityGalleriesDifferentShops)
