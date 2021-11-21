def PoliczSylaby(word):
    sylaby = 0
    samogloski = ['a','e','i','y','u','o','ą','ę','ó','A','E','I','Y','U','O','Ą','Ę','Ó']
    for letter in range(0,len(word)):
        if word[letter] in samogloski:
            if word[letter] == 'i':
                if word[letter-1] not in samogloski and word[letter+1] in samogloski:
                    sylaby+=0
            else:
                sylaby+=1

    return sylaby

filename = "tekst1.txt"
filename2 = "wyniki.txt"
file = open(filename,'r',encoding='utf8')
file2 = open(filename2,'w',encoding='utf8')

for line in file:
    if not (PoliczSylaby(line)==13):
        if(PoliczSylaby(line)>10 and PoliczSylaby(line)<18):
            file2.write(line.replace(line[-1],'') + ";|" + str(PoliczSylaby(line))+"\n")
