# from codio exercise
# url for ECM data in xml format
url = "http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"

import urllib.request

page = urllib.request.urlopen(url)
data_bytes = page.read()
data_string = data_bytes.decode('utf-8')
page.close()

import xml.etree.ElementTree as ET

data_tree = ET.fromstring(data_string)


def stringChanger(a):
    for child in data_tree[2][0]:
        countryD = child.attrib
        countryD[countryD["currency"]] = float(countryD["rate"])
        if a == countryD["currency"]:
            a = float(countryD["rate"])
    return a


def CurrencyConverter(InCurType, OutCurType, InCurAmt):
    InputCur = stringChanger(InCurType.upper())
    OutputCur = stringChanger(OutCurType.upper())

    OutCurAmt = round((int(InCurAmt) / InputCur) * OutputCur, 2)
    print("intiating \nConverting... \n...")
    return print(InCurAmt, InCurType.upper(), "=", OutCurAmt, OutCurType.upper())


a = input("CurrencyToBeConverted\n")
b = input("CurrecyConvertedTo\n")
c = input("CurrencyAmount\n")
CurrencyConverter(a, b, c)







