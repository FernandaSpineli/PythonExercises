from datetime import date, time, datetime


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%d %m %Y'))

def trabalhando_com_time():
    horario = time(hour = 15, minute = 18, second = 30)
    print(horario)
    horario_str = horario.strftime('%H, %M, %S')    
    print(horario_str)
    
def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2018, 6, 30, 15, 30, 20)
    print(data_criada)
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    
    