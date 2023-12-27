fo = open("2/input.txt", "r")

selectionPoints = {'X':1, 'Y':2, 'Z':3}
# 0 lost, 3 draw, 6 win
roundPoints = {"XA":3, "XC":6, "XB":0,
               "YA":6, "YC":0, "YB":3,
               "ZA":0, "ZC":3, "ZB":6}
decrypt = {"AX":'Z', "AY":'X', "AZ":'Y',
           "BX":'X', "BY":'Y', "BZ":'Z',
           "CX":'Y', "CY":'Z', "CZ":'X'}

totPointsPart1 = 0
totPointsPart2 = 0
for line in fo.readlines():
    line = line.strip()
    oponent, me = line[0], line [2]
    totPointsPart1 += roundPoints[me+oponent] + selectionPoints[me]
    me = decrypt[oponent+me]
    totPointsPart2 += roundPoints[me+oponent] + selectionPoints[me]
    
print(totPointsPart1)
print(totPointsPart2)