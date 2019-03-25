import dots
from nearest_neighbor import nearest_neightbor as nn

# Get map dots
print('\n')
dots.get_dots()

# Select map
print('Please select a map')
print('----------------------')
print('0) Fairy Fountains.')
print('1) Memories.')
print('2) Shrines.\n')

m = input('Map: ')

if m == '0':
    nn(m)
elif m == '1':
    nn(m)
elif m == '2':
    nn(m)
else:
    print('Invalid Input')
