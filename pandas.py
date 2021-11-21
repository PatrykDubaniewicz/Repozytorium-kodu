import pandas as pd
import openpyxl
from datetime import datetime
import io

def GenerateSalutation(name):
    if name.endswith('a'):
        return "Szanowna Pani " + name
    else:
        return "Szanowny Panie " + name

def GenerateTextFile(name_param,debt_param,date_param):
    return GenerateSalutation(name_param) + ", \n  Prosimy o spłatę długu w wysokości " + str(debt_param) + "zł do " + str(date_param)

def GenerateFilename(name_param):
    return str(name_param + ".txt")


filepath = "Baza (1).xlsx"

excel_file = pd.read_excel(filepath, index_col=0)
excel_file = excel_file.iloc[1:]
for index, row in excel_file.iterrows():
    name = row[0]
    debt = row[1]
    date = datetime.strftime(row[2], '%d.%m.%Yr.')
    with io.open(GenerateFilename(name), "w", encoding="utf-8") as file:
        file.write(GenerateTextFile(name,debt,date))

    file.close()
