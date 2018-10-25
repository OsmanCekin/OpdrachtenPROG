file = open('C:/Users/Fener/PycharmProjects/Opdrachten/Opdracht 7/hardlopers.txt', 'a')


import time
time = time.strftime('%a %d %b %Y, %H:%M:%S, ', time.localtime())
naam = input('Naam: ')
file.write(str(time) + ',' + naam + '\n')

file.close()