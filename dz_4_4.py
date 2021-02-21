from utils import currency_rates

# демонстрация работы моего внешнего модуля
print(*currency_rates('USD'))
print(*currency_rates('EUR'))
print(*currency_rates('USD', 'EUR'))
