invoer = '5-9-7-1-7-8-3-2-4-8-7-9'

invoer = invoer.split('-')

print('Gesorteerde list van ints: ' + str(invoer))
print('Grootste getal: ' + str(max(invoer)) + ' en Kleinste getal: ' + str(min(invoer)))
print('Aantal getallen: ' + str(len(invoer)) + ' en Som van de getallen: ' + str(sum(invoer)))