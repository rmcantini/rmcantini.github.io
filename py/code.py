'''Timesheet calc'''
from datetime import datetime


TOTAL_TIME = '08:00'


worked_time = input('')
# print(worked_time)

FORMAT_H = '%H:%M'

time_solo = datetime.strptime(TOTAL_TIME, FORMAT_H) - \
    datetime.strptime(worked_time, FORMAT_H)
time_final = time_solo / 2


answer = (f'Tempo de espera total {time_solo}. \nRegistre ambos, \
Super e Eletro, com {time_final} cada.')

print('Timesheet', answer)
