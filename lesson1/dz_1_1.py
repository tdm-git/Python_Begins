# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# # до минуты: <s> сек;
# # * до часа: <m> мин <s> сек;
# # * до суток: <h> час <m> мин <s> сек;

duration = int(input('введите длительность (сек): '))
if duration < 60:
    result = f'{duration} сек'
elif duration < 3600:
    minutes = duration // 60
    sekunds = duration % 60
    result = f'{minutes} мин {sekunds} сек'
elif duration < 24*3600:
    hours = duration // 3600
    duration = duration - hours*3600
    minutes = duration // 60
    sekunds = duration % 60
    result = f'{hours} час {minutes} мин {sekunds} сек'
else:
    days = duration // (3600 * 24)
    duration = duration - days * 24 * 3600
    hours = duration // 3600
    duration = duration - hours * 3600
    minutes = duration // 60
    sekunds = duration % 60
    result = f'{days} дн {hours} час {minutes} мин {sekunds} сек'
print(result)
