from Methods import enter
from Methods import prime_factors as prime
from Methods import list_in_text as txt
import os

os.system('cls')

num = enter('Введите число, для которого необходимо найти список простых чисел: ')

factors = prime(num)

output = txt(factors)
print(output)