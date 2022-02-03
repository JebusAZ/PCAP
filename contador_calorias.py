from datetime import date
today = date.today()

print("La fecha del día de hoy es: ", today)
print("Ahora ingresa tus calorias ingeridas en el desayuno")
desayuno=int(input())
print("Ahora ingresa tus calorias ingeridas en la comida")
comida=int(input())
print("Ahora ingresa tus calorias ingeridas en la cena")
cena=int(input())
print("Ahora ingresa tus calorias ingeridas en tentempies")
tentempies=int(input())

totalCalorias= desayuno + comida + cena + tentempies

print("Las calorías ingeridas el día de hoy", today, "es", totalCalorias)
