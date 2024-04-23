# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6 

import calendar

# Printando o calendário por completo de um ano
print(calendar.calendar(2025))

# Printando o calendário de um mês de um ano específico
print(calendar.month(2026, 10))

# Printando o último dia do mês, junto com o dia da semana
print(calendar.monthrange(2024, 5))

# Printando qual dia da semana será em um dia específico
# Lembrando que; Os dias da semana em 'calendar' estão representados como valores inteiros;
# Ou seja, valores de 0 à 6 para representar os dias da semana.
# Começando por 0 - segunda até 6 - domingo.
print(calendar.weekday(2024, 4, 23))


# Agora parando para analisar este método; O calendário pode ser representado dentro de listas.
# Onde cada lista é uma semana do calendário, dito que; Os dias que possuem '0' são dias que não são do mês exibido.
# Vale a pena observar também que cada lista só possui 7 valores dentro dela, que são exatamente os dias de segunda à domingo.
# Lembrando sempre que o primeiro dia da semana é (0-Segunda). 
for semana in calendar.monthcalendar(2024, 4):
    print(semana)