from sys import argv
from utils import currency_rates

if __name__ == '__main__':
    program, *args = argv
    for i in (args):
        print(*currency_rates(i))

# тестовые строки - для терминала: один параметр и несколько
# python dz_4_5.py USD
# python dz_4_5.py USD EUR GBP
