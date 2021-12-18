import pandas as pd

num1 = input("Element Atomic Number:\n")
num1 = int(num1)

num1= num1-1

df = pd.read_excel(r'C:\Users\aya69\PycharmProjects\molarmasscalculator\MolarMassSpreadsheetvfinal.xlsx')

num3 = input("Element mass (g):\n")
num2 = (df['Molar Mass'].iloc[num1])

num3 = float(num3)
num2 = float(num2)

out = num3 / num2
print(float(out))
