# funkcje
def IsLongest(gap):
    if gap > longest_gap:
        return True
    else:
        return False


def IsShortest(gap):
    if gap < shortest_gap:
        return True
    else:
        return False

def CalculateGap(left, right):
    return abs(left - right)

def WriteLongestAndShortestGapToFile(filename):
    filename.write("Dlugosc najwiekszej luki: " + str(longest_gap) + "\n")
    filename.write("Dlugosc najmniejszej luki: " + str(shortest_gap) + "\n\n")

def WriteLongestRegularPartToFile(filename, start, end, length):
    filename.write("Najdluzszy fragment: od " + str(start) + " do " + str(end) + "\n")
    filename.write("Dlugosc: " + str(length) + "\n\n")

def Write_4_3_resultsToFile(filename,gaps, gap_count):
    filename.write("Krotnosc najczestszej luki: " + str(gap_count) + "\n")
    filename.write("Wartosci najczestszych luk: ")
    for i in range(0, len(gaps)):
        filename.write(str(gaps[i]) + " ")


# otwieranie plików
filepath_dane = 'dane4.txt'
filepath_wynik = 'wynik_4.txt'
file_dane = open(filepath_dane)
file_wynik = open(filepath_wynik, 'w')

# podstawowe zmienne

all_numbers = []
prevline = ""

number = 0
previous_number = 0

gap = 0
previous_gap = 0
shortest_gap = 0
longest_gap = 0
gap_update = 0

regular_part = []
longest_regular_part_start = 0
longest_regular_part_end = 0
longest_regular_part_length = 0
longest_regular_part = ""

dictionary_gap_count = {}

Initialize = False

with file_dane as file:
    for line in file:
        all_numbers.append(int(line))


        if not Initialize:
            previous_number = 0
            shortest_gap = int(line)
            Initialize = True
        else:
            previous_number = int(prevline)

        # zaktualizowanie wartości zmiennych
        number = int(line)
        gap = abs(number - previous_number)

        # zadanie 4.1
        if IsLongest(gap):
            longest_gap = gap
        if IsShortest(gap):
            shortest_gap = gap

        # zadanie 4.2
        if previous_gap == gap:
            regular_part.append(previous_number)
        else:
            if len(regular_part) > longest_regular_part_length:
                longest_regular_part_start = regular_part[0]
                longest_regular_part_end = regular_part[len(regular_part) - 1]
                longest_regular_part_length = len(regular_part)
                regular_part.clear()
            else:
                regular_part.clear()

        # zadanie 4.3
        gap_update = dictionary_gap_count.get(str(gap), 0) + 1
        dictionary_gap_count[str(gap)] = gap_update

        biggest = 0
        biggestGap = ''
        biggestGapCollection = []

        for key in dictionary_gap_count:
            current_count = dictionary_gap_count[key]
            if current_count > biggest:
                biggest = current_count
                biggestGap = key
                biggestGapCollection = [biggestGap]
            else:
                if current_count == biggest:
                    biggestGapCollection.append(key)

        # zapisanie poprzednich linii
        prevline = line
        previous_gap = gap

current = all_numbers[0]
next_number = all_numbers[1]
index = 0
longest_sequence = []
gap_counter = 0
previous_gap = 0
current_sequence = [all_numbers[index]]

while index < len(all_numbers) - 2:
    current = all_numbers[index]
    next_number = all_numbers[index + 1]
    current_gap = CalculateGap(current, next_number)
    if current_gap != previous_gap:
        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence
            longest_sequence.append(current)
        current_sequence = []
    current_sequence.append(current)
    index += 1
    previous_gap = current_gap

print(longest_sequence)


#Zapisanie do pliku
WriteLongestAndShortestGapToFile(file_wynik)
WriteLongestRegularPartToFile(file_wynik, longest_sequence[0], longest_sequence[len(longest_sequence) - 1],
                              len(longest_sequence))
Write_4_3_resultsToFile(file_wynik,biggestGapCollection,biggest)

file_dane.close()
file_wynik.close()
