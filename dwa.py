#wejscie = input()
#print(wejscie)
#print(type(wejscie))

#import sys
#wejscie2 = sys.stdin.readline()
#print(wejscie2)
#print(type(wejscie2))



# liczba = 10
# if liczba < 10:
#     print('cośtam1')
# elif liczba > 0:
#     print('cośtam2')
# else:
#     print('klapa')

#and or not
# if liczba > 0 and liczba < 11:
#      print('OK') 

#krócej
# if  0 < liczba < 11:
#      print('OK')     


#foreach
imie = 'Ariadna'
# for litera in imie:
#     print(litera, end = '')

#range
range(5) #start, stop, step
print(range(5))
print(list(range(2,10,2))) #stop = stop - step
print(list(range(10,2,-2)))

#[od:do]
print(imie[2:4])
print(imie[::2])


#pass
for liczba in range(5):
    pass #pass sprawia że nic nie robiąca pętla nie wywala errora
for litera in imie[::2]:
    pass


#while
# import random
# z = random.randint(1,20)

# while(z!=5):
#     print(str(z))
#     z = random.randint(1,20)
# else:
#     print("20, koniec")


