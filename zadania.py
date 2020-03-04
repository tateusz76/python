#pierwiastek
# import math  

# x = int(input())
# if x < 0:
#     print("Nie działamy na liczbach zespolonych!!!") 
# else:
#     print(type(x))
#     print("Pierwiastek z " + str(x) + " wynosi: ", end = '')
#     print(round(math.sqrt(x),2))



#czylitera/cyfra
y = input()
if y.isdigit():
    print("Jest to cyfra/liczba")
else:
    print("Jest to litera/ciąg liter")
