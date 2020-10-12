# para trabajar con fechas usamos libreria datetime
from datetime import date
from datetime import datetime

# dia actual
today = date.today()

# fecha actual
now = datetime.now()

print(today)
print(now)

# date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))

# datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))
