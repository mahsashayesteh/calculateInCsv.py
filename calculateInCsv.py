import csv
import random


def randomNum():
    num = random.randint(1, 100)
    return num


lstRand1 = []

for i in range(1, 100):
    lstRand1.append(random.randint(1, 10))

lstRand2 = []
for i in range(1, 100):
    lstRand2.append(random.randint(1, 10))

headers = [['row', 'firstNum', 'secondNum', 'sum', 'multiple', 'minus', 'divide']]

with open('D:\\Calulate.csv', "w", newline="") as f:
    madeCsv = csv.writer(f)
    madeCsv.writerows(headers)
    print(lstRand1)

    i = 1
    listRow = []
    while i < 99:
        row = i
        firstRandNum1 = lstRand1[i]

        secondRandNum2 = lstRand2[i]

        sum = firstRandNum1 + secondRandNum2

        mult = firstRandNum1 * secondRandNum2
        minus = firstRandNum1 - secondRandNum2
        divide = firstRandNum1 / secondRandNum2
        row = [row, firstRandNum1, secondRandNum2, sum, mult, minus, divide]
        listRow.append(row)
        i += 1
    print(listRow)
    madeCsv.writerows(listRow)


#
# [i], [lstRand2[1]], [randnum2], [randnum1 + randnum2], [randnum1 * randnum2], [randnum1 - randnum2],
# [randnum1 - randnum2], [randnum1 / randnum2]]
