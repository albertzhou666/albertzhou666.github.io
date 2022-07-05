from ast import Try
from typing import final


x = 40
y = 0

print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print(e)
    print('Not allowed to devide by zero')
else:
    print('Something else went wrong')
finally:
    print('This is our cleanup code')
print()