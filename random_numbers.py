from random import randrange, randint
import csv
import datetime

nconsultas = 5000

# startdate = datetime.date(2010, 01, 01)
# header =['CONCODIGO', 'MEDCODIGO', 'PACCODIGO', 'DATA']
# consultas = [[x, randrange(1000, 1570), randrange(100, 200), (startdate + datetime.timedelta(randint(1, 365))).strftime("%d%m%Y")] for x in range(1, nconsultas)]
#
# with open('consultas.csv', 'wb') as myfile:
#     wr = csv.writer(myfile)
#     wr.writerow(header)
#     for r in consultas:
#         wr.writerow(r)

with open('medicamentos.csv', 'rb') as f:
    reader = csv.reader(f)
    next(reader, None)
    medicamentos = list(reader)

header = ['CONCODIGO', 'MDCODIGO', 'POSOLOGIA']
prescricoes = [
    [x, int(medicamentos[randrange(1, 3388)][0]), 'Tomar 1 comprimido {0} vezes ao dia, durante {1} dias'.format(randrange(2, 4), randrange(7, 30))]
    for x in range(1, nconsultas)]

with open('PRESCRICAO.csv', 'wb') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(header)
    for r in prescricoes:
        wr.writerow(r)
