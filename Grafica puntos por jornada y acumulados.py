import matplotlib.pyplot as plt

# Datos para el gráfico, si quiero calcular los puntos por jornada tengo que quitar el 0 de fixture
fixture = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

muletjr10 = [51, 56, 38, 76, 65, 37, 28, 54, 47, 42, 66, 35, 43, 56, 64, 79, 65, 40, 70, 54, 35, 71, 50, 44, 55]
PRATS = [33, 34, 65, 33, 62, 55, 44, 76, 64, 84, 51, 94, 71, 71, 62, 59, 62, 71, 62, 48, 63, 77, 66, 50, 65]
Elpu7 = [30, 53, 50, 68, 49, 59, 58, 49, 49, 57, 65, 75, 45, 36, 64, 77, 57, 48, 69, 59, 53, 31, 47, 69, 77]
makinaone = [38, 53, 29, 43, 59, 59, 57, 44, 41, 84, 61, 67, 32, 71, 59, 66, 70, 51, 50, 61, 95, 69, 67, 63, 56]
Payo_Cayetano = [39, 49, 46, 50, 37, 51, 26, 26, 40, 62, 0, 0, 41, 56, 68, 0, 72, 58, 49, 26, 30, 67, 67, 35, 38]
Tugoressss = [33, 56, 38, 59, 52, 49, 41, 41, 68, 66, 59, 37, 79, 75, 59, 72, 83, 109, 61, 50, 63, 66, 90, 51, 51]
Sporting_de_Cananu = [29, 42, 40, 37, 52, 58, 47, 52, 29, 45, 57, 70, 70, 56, 40, 61, 65, 50, 71, 52, 75, 87, 79, 72, 68]
Ensaimada_City = [28, 46, 52, 51, 67, 85, 74, 60, 78, 71, 62, 78, 61, 96, 72, 85, 63, 87, 93, 69, 76, 69, 37, 83, 35]
Jorch579 = [20, 24, 41, 33, 44, 27, 52, 0, 49, 32, 71, 49, 56, 54, 60, 60, 65, 46, 48, 62, 41, 71, 65, 50, 53]
Al_bert_Ibn_al_Ettif = [11, 32, 65, 49, 0, 46, 42, 66, 32, 60, 43, 72, 68, 44, 72, 58, 75, 62, 42, 81, 55, 24, 34, 72, 36]

acumulativo_muletjr10 = [0]
acumulativo_PRATS = [0]
acumulativo_Sporting_de_Cananu = [0]
acumulativo_Elpu7 = [0]
acumulativo_makinaone = [0]
acumulativo_Payo_Cayetano = [0]
acumulativo_Tugoressss = [0]
acumulativo_Ensaimada_City = [0]
acumulativo_Jorch579 = [0]
acumulativo_Al_bert_Ibn_al_Ettif = [0]

for i in range(0, len(muletjr10)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + muletjr10[j]
    acumulativo_muletjr10.append(acumulativo)

for i in range(0, len(PRATS)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + PRATS[j]
    acumulativo_PRATS.append(acumulativo)
        
for i in range(0, len(Sporting_de_Cananu)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Sporting_de_Cananu[j]
    acumulativo_Sporting_de_Cananu.append(acumulativo)

for i in range(0, len(Elpu7)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Elpu7[j]
    acumulativo_Elpu7.append(acumulativo)

for i in range(0, len(makinaone)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + makinaone[j]
    acumulativo_makinaone.append(acumulativo)
        
for i in range(0, len(Tugoressss)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Tugoressss[j]
    acumulativo_Tugoressss.append(acumulativo)

for i in range(0, len(Ensaimada_City)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Ensaimada_City[j]
    acumulativo_Ensaimada_City.append(acumulativo)

for i in range(0, len(Jorch579)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Jorch579[j]
    acumulativo_Jorch579.append(acumulativo)

for i in range(0, len(Al_bert_Ibn_al_Ettif)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Al_bert_Ibn_al_Ettif[j]
    acumulativo_Al_bert_Ibn_al_Ettif.append(acumulativo)

for i in range(0, len(Payo_Cayetano)):
    acumulativo = 0
    for j in range(0, i+1):
        acumulativo = acumulativo + Payo_Cayetano[j]
    acumulativo_Payo_Cayetano.append(acumulativo)

print(acumulativo_Ensaimada_City)

    

# Crear el gráfico
plt.figure(figsize=(8, 6))  # Establecer el tamaño de la figura
plt.plot(fixture, Sporting_de_Cananu, 'r--', label='Sporting de Cananu')  # Línea roja con guiones
# plt.plot(fixture, acumulativo_Ensaimada_City, 'g--', label='Ensaimada City')  # Línea verde con guión-punto
plt.plot(fixture, PRATS, 'b--', label='PRATS')  # Línea azul con puntos
plt.plot(fixture, Tugoressss, 'y--', label='Tugoressss')  # Línea roja con guiones
plt.plot(fixture, makinaone, 'g--', label='makinaone')  # Línea verde con guión-punto
# plt.plot(fixture, acumulativo_Payo_Cayetano, 'c--', label='Payo Cayetano')  # Línea azul con puntos
# plt.plot(fixture, acumulativo_muletjr10, 'm--', label='muletjr10')  # Línea roja con guiones
# plt.plot(fixture, acumulativo_Jorch579, 'k--', label='Jorch579')  # Línea verde con guión-punto
# plt.plot(fixture, acumulativo_Elpu7, 'g:', label='Elpu7')  # Línea azul con puntos
# plt.plot(fixture, acumulativo_Al_bert_Ibn_al_Ettif, 'r:', label='Al-bert Ibn al-Ettif')  # Línea roja con guiones
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.title('Gráfico de ejemplo con múltiples líneas')  # Título del gráfico
plt.legend()  # Mostrar leyenda
plt.grid(True)  # Mostrar cuadrícula
plt.show()  # Mostrar el gráfico

