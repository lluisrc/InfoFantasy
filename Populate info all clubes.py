import mysql.connector

# conexion = mysql.connector.connect(
#     host="192.168.178.53",
#     user="lroca",
#     password="lroca",
#     database="fantasy"
# )

## Para obtener esta data necesitas seleccionar todo la informacion de todos los jugadores de cada jornada ...
# Hacemos una select y copiamos la respuesta de la tabla y la pegamos en https://create.piktochart.com/teams/30440454/dashboard (creamos el grafico)

data = """1 

muletjr10
180.564.168

51
PFSY

2 

Payo Cayetano
136.701.516

39
PFSY

3 

makinaone
378.332.658

38
PFSY

4 

Tugoressss
484.757.410

33
PFSY
5 

PRATS
251.382.945

33
PFSY

6 

Elpu7
189.462.255

30
PFSY
7 

Sporting de Cananú
271.954.764

29
PFSY

8 

Ensaimada City
394.732.606

28
PFSY

9 

Jorch579
123.952.363

20
PFSY

10 

Al-bert Ibn al-Ettif
119.152.642

11
PFSY



1 

muletjr10
180.564.168

56
PFSY

2 

Tugoressss
484.757.410

56
PFSY

3 

Elpu7
189.462.255

53
PFSY

4 

makinaone
378.332.658

53
PFSY

5 

Payo Cayetano
136.701.516

49
PFSY

6 

Ensaimada City
394.732.606

46
PFSY
7 

Sporting de Cananú
271.954.764

42
PFSY
8 

PRATS
230.657.076

34
PFSY

9 

Al-bert Ibn al-Ettif
119.152.642

32
PFSY

10 

Jorch579
123.952.363

24
PFSY

1 

PRATS
230.657.076

65
PFSY

2 

Al-bert Ibn al-Ettif
119.152.642

65
PFSY

3 

Ensaimada City
394.732.606

52
PFSY

4 

Elpu7
189.462.255

50
PFSY

5 

Payo Cayetano
136.701.516

46
PFSY

6 

Jorch579
123.952.363

41
PFSY
7 

Sporting de Cananú
271.954.764

40
PFSY

8 

muletjr10
180.564.168

38
PFSY

9 

Tugoressss
484.757.410

38
PFSY

10 

makinaone
378.332.658

29
PFSY

1 

muletjr10
180.564.168

76
PFSY

2 

Elpu7
189.462.255

68
PFSY

3 

Tugoressss
484.757.410

59
PFSY

4 

Ensaimada City
394.732.606

51
PFSY

5 

Payo Cayetano
136.701.516

50
PFSY

6 

Al-bert Ibn al-Ettif
119.152.642

49
PFSY

7 

makinaone
378.332.658

43
PFSY
8 

Sporting de Cananú
271.954.764

37
PFSY
9 

PRATS
230.657.076

33
PFSY

10 

Jorch579
123.952.363

33
PFSY

1 

Ensaimada City
394.732.606

67
PFSY

2 

muletjr10
180.564.168

65
PFSY
3 

PRATS
230.657.076

62
PFSY

4 

makinaone
378.332.658

59
PFSY
5 

Sporting de Cananú
271.954.764

52
PFSY

6 

Tugoressss
484.757.410

52
PFSY

7 

Elpu7
189.462.255

49
PFSY

8 

Jorch579
123.952.363

44
PFSY

9 

Payo Cayetano
136.701.516

37
PFSY

10 

Al-bert Ibn al-Ettif
119.152.642

0
PFSY

1 

Ensaimada City
394.732.606

85
PFSY

2 

Elpu7
189.462.255

59
PFSY

3 

makinaone
378.332.658

59
PFSY
4 

Sporting de Cananú
271.954.764

58
PFSY
5 

PRATS
230.657.076

55
PFSY

6 

Payo Cayetano
136.701.516

51
PFSY

7 

Tugoressss
484.757.410

49
PFSY

8 

Al-bert Ibn al-Ettif
119.152.642

46
PFSY

9 

muletjr10
180.564.168

37
PFSY

10 

Jorch579
123.952.363

27
PFSY

1 

Ensaimada City
394.732.606

74
PFSY

2 

Elpu7
189.462.255

58
PFSY

3 

makinaone
378.332.658

57
PFSY

4 

Jorch579
123.952.363

52
PFSY
5 

Sporting de Cananú
271.954.764

47
PFSY
6 

PRATS
230.657.076

44
PFSY

7 

Al-bert Ibn al-Ettif
119.152.642

42
PFSY

8 

Tugoressss
484.757.410

41
PFSY

9 

muletjr10
180.564.168

28
PFSY

10 

Payo Cayetano
136.701.516

26
PFSY

1 

PRATS
230.657.076

76
PFSY

2 

Al-bert Ibn al-Ettif
119.152.642

66
PFSY

3 

Ensaimada City
394.732.606

60
PFSY

4 

muletjr10
180.564.168

54
PFSY
5 

Sporting de Cananú
271.954.764

52
PFSY

6 

Elpu7
189.462.255

49
PFSY

7 

makinaone
378.332.658

44
PFSY

8 

Tugoressss
484.757.410

41
PFSY

9 

Payo Cayetano
136.701.516

26
PFSY

10 

Jorch579
123.952.363

0
PFSY

1 

Ensaimada City
394.732.606

78
PFSY

2 

Tugoressss
484.757.410

68
PFSY
3 

PRATS
230.657.076

64
PFSY

4 

Elpu7
189.462.255

49
PFSY

5 

Jorch579
123.952.363

49
PFSY

6 

muletjr10
180.564.168

47
PFSY

7 

makinaone
378.332.658

41
PFSY

8 

Payo Cayetano
136.701.516

40
PFSY

9 

Al-bert Ibn al-Ettif
119.152.642

32
PFSY
10 

Sporting de Cananú
271.954.764

29
PFSY

1 

makinaone
378.332.658

84
PFSY
2 

PRATS
230.657.076

84
PFSY

3 

Ensaimada City
394.732.606

71
PFSY

4 

Tugoressss
484.757.410

66
PFSY

5 

Payo Cayetano
136.701.516

62
PFSY

6 

Al-bert Ibn al-Ettif
119.152.642

60
PFSY

7 

Elpu7
189.462.255

57
PFSY
8 

Sporting de Cananú
271.954.764

45
PFSY

9 

muletjr10
180.564.168

42
PFSY

10 

Jorch579
123.952.363

32
PFSY

1 

Jorch579
123.952.363

71
PFSY

2 

muletjr10
180.564.168

66
PFSY

3 

Elpu7
189.462.255

65
PFSY

4 

Ensaimada City
394.732.606

62
PFSY

5 

makinaone
378.332.658

61
PFSY

6 

Tugoressss
484.757.410

59
PFSY
7 

Sporting de Cananú
271.954.764

57
PFSY
8 

PRATS
230.657.076

51
PFSY

9 

Al-bert Ibn al-Ettif
119.152.642

43
PFSY

10 

Payo Cayetano
136.701.516

0
PFSY

1 

PRATS
230.657.076

94
PFSY

2 

Ensaimada City
394.732.606

78
PFSY

3 

Elpu7
189.462.255

75
PFSY

4 

Al-bert Ibn al-Ettif
119.152.642

72
PFSY
5 

Sporting de Cananú
271.954.764

70
PFSY

6 

makinaone
378.332.658

67
PFSY

7 

Jorch579
123.952.363

49
PFSY

8 

Tugoressss
484.757.410

37
PFSY

9 

muletjr10
180.564.168

35
PFSY

10 

Payo Cayetano
136.701.516

0
PFSY

1 

Tugoressss
484.757.410

79
PFSY
2 

PRATS
230.657.076

71
PFSY
3 

Sporting de Cananú
271.954.764

70
PFSY

4 

Al-bert Ibn al-Ettif
119.152.642

68
PFSY

5 

Ensaimada City
394.732.606

61
PFSY

6 

Jorch579
123.952.363

56
PFSY

7 

Elpu7
189.462.255

45
PFSY

8 

muletjr10
180.564.168

43
PFSY

9 

Payo Cayetano
136.701.516

41
PFSY

10 

makinaone
378.332.658

32
PFSY

1 

Ensaimada City
394.732.606

96
PFSY

2 

Tugoressss
484.757.410

75
PFSY
3 

PRATS
230.657.076

71
PFSY

4 

makinaone
378.332.658

71
PFSY
5 

Sporting de Cananú
271.954.764

56
PFSY

6 

muletjr10
180.564.168

56
PFSY

7 

Payo Cayetano
136.701.516

56
PFSY

8 

Jorch579
123.952.363

54
PFSY

9 

Al-bert Ibn al-Ettif
119.152.642

44
PFSY

10 

Elpu7
189.462.255

36
PFSY

1 

Ensaimada City
394.732.606

72
PFSY

2 

Al-bert Ibn al-Ettif
119.152.642

72
PFSY

3 

Payo Cayetano
136.701.516

68
PFSY

4 

Elpu7
189.462.255

64
PFSY

5 

muletjr10
180.564.168

64
PFSY
6 

PRATS
230.657.076

62
PFSY

7 

Jorch579
123.952.363

60
PFSY

8 

Tugoressss
484.757.410

59
PFSY

9 

makinaone
378.332.658

59
PFSY
10 

Sporting de Cananú
271.954.764

40
PFSY

1 

Ensaimada City
394.732.606

85
PFSY

2 

muletjr10
180.564.168

79
PFSY

3 

Elpu7
189.462.255

77
PFSY

4 

Tugoressss
484.757.410

72
PFSY

5 

makinaone
378.332.658

66
PFSY
6 

Sporting de Cananú
271.954.764

61
PFSY

7 

Jorch579
123.952.363

60
PFSY
8 

PRATS
230.657.076

59
PFSY

9 

Al-bert Ibn al-Ettif
119.152.642

58
PFSY

10 

Payo Cayetano
136.701.516

0
PFSY

1 

Tugoressss
484.757.410

83
PFSY

2 

Al-bert Ibn al-Ettif
119.152.642

75
PFSY

3 

Payo Cayetano
136.701.516

72
PFSY

4 

makinaone
378.332.658

70
PFSY
5 

Sporting de Cananú
271.954.764

65
PFSY

6 

muletjr10
180.564.168

65
PFSY

7 

Jorch579
123.952.363

65
PFSY

8 

Ensaimada City
394.732.606

63
PFSY
9 

PRATS
230.657.076

62
PFSY

10 

Elpu7
189.462.255

57
PFSY

1 

Tugoressss
484.757.410

109
PFSY

2 

Ensaimada City
394.732.606

87
PFSY
3 

PRATS
230.657.076

71
PFSY

4 

Al-bert Ibn al-Ettif
119.152.642

62
PFSY

5 

Payo Cayetano
136.701.516

58
PFSY

6 

makinaone
378.332.658

51
PFSY
7 

Sporting de Cananú
271.954.764

50
PFSY

8 

Elpu7
189.462.255

48
PFSY

9 

Jorch579
123.952.363

46
PFSY

10 

muletjr10
180.564.168

40
PFSY

1 

Ensaimada City
394.732.606

93
PFSY
2 

Sporting de Cananú
271.954.764

71
PFSY

3 

muletjr10
180.564.168

70
PFSY

4 

Elpu7
189.462.255

69
PFSY
5 

PRATS
230.657.076

62
PFSY

6 

Tugoressss
484.757.410

61
PFSY

7 

makinaone
378.332.658

50
PFSY

8 

Payo Cayetano
136.701.516

49
PFSY

9 

Jorch579
123.952.363

48
PFSY

10 

Al-bert Ibn al-Ettif
119.152.642

42
PFSY

1 

Al-bert Ibn al-Ettif
119.152.642

81
PFSY

2 

Ensaimada City
394.732.606

69
PFSY

3 

Jorch579
123.952.363

62
PFSY

4 

makinaone
378.332.658

61
PFSY

5 

Elpu7
189.462.255

59
PFSY

6 

muletjr10
180.564.168

54
PFSY
7 

Sporting de Cananú
271.954.764

52
PFSY

8 

Tugoressss
484.757.410

50
PFSY
9 

PRATS
230.657.076

48
PFSY

10 

Payo Cayetano
136.701.516

26
PFSY

1 

makinaone
378.332.658

95
PFSY

2 

Ensaimada City
394.732.606

76
PFSY
3 

Sporting de Cananú
271.954.764

75
PFSY

4 

Tugoressss
484.757.410

63
PFSY
5 

PRATS
230.657.076

63
PFSY

6 

Al-bert Ibn al-Ettif
119.152.642

55
PFSY

7 

Elpu7
189.462.255

53
PFSY

8 

Jorch579
123.952.363

41
PFSY

9 

muletjr10
180.564.168

35
PFSY

10 

Payo Cayetano
136.701.516

30
PFSY

1 

Sporting de Cananú
271.954.764

87
PFSY
2 

PRATS
230.657.076

77
PFSY

3 

muletjr10
180.564.168

71
PFSY

4 

Jorch579
123.952.363

71
PFSY

5 

Ensaimada City
394.732.606

69
PFSY

6 

makinaone
378.332.658

69
PFSY

7 

Payo Cayetano
136.701.516

67
PFSY

8 

Tugoressss
484.757.410

66
PFSY

9 

Elpu7
189.462.255

31
PFSY

10 

Al-bert Ibn al-Ettif
119.152.642

24
PFSY

1 

Tugoressss
484.757.410

90
PFSY
2 

Sporting de Cananú
271.954.764

79
PFSY

3 

makinaone
378.332.658

67
PFSY

4 

Payo Cayetano
136.701.516

67
PFSY
5 

PRATS
230.657.076

66
PFSY

6 

Jorch579
123.952.363

65
PFSY

7 

muletjr10
180.564.168

50
PFSY

8 

Elpu7
189.462.255

47
PFSY

9 

Ensaimada City
394.732.606

37
PFSY

10 

Al-bert Ibn al-Ettif
119.152.642

34
PFSY

1 

Ensaimada City
389.836.346

83
FSYP
2 

Sporting de Cananú
269.968.710

72
FSYP

3 

Al-bert Ibn al-Ettif
119.296.131

72
FSYP

4 

Elpu7
191.876.485

69
FSYP

5 

makinaone
377.042.762

63
FSYP

6 

Tugoressss
459.546.768

51
FSYP
7 

PRATS
236.921.835

50
FSYP

8 

Jorch579
123.161.313

50
FSYP

9 

muletjr10
169.273.570

44
FSYP

10 

Payo Cayetano
135.874.851

35
FSYP

1 

Elpu7
239.880.521

77
PFSY
2 

Sporting de Cananú
292.477.084

68
PFSY
3 

PRATS
234.023.704

65
PFSY

4 

makinaone
422.042.877

56
PFSY

5 

muletjr10
80.259.120

55
PFSY

6 

Jorch579
114.533.450

53
PFSY

7 

Tugoressss
362.588.988

51
PFSY

8 

Payo Cayetano
119.218.865

38
PFSY

9 

Al-bert Ibn al-Ettif
136.159.517

36
PFSY

10 

Ensaimada City
560.687.206

35
PFSY"""

data = data.split('\n')
data = [elemento for elemento in data if elemento != '']

print(data)
print(len(data))

POSICION = []
JORNADA = []
JUGADORES = []
PRECIO_EQUIPO = []
PUNTOS_JORNADA = []
PUNTOS_ACUMULATIVOS = []

PayoCayetano_actual = 0
muletjr10_actual = 0
makinaone_actual = 0
Tugoressss_actual = 0
PRATS_actual = 0
Elpu7_actual = 0
Sporting_de_Cananú_actual = 0
Ensaimada_City_actual = 0
Jorch579_actual = 0
Al_bert_Ibn_al_Ettif = 0

for i in range(0, int(int(len(data)/5))):
    POSICION.append(int(data[0+(i*5)]))

for i in range(0, int(len(data)/5)):
    print(data[1+(i*5)])
    JUGADORES.append(data[1+(i*5)])

    if (data[1+(i*5)] == 'Payo Cayetano'):
        PayoCayetano_actual = PayoCayetano_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(PayoCayetano_actual)
    
    if (data[1+(i*5)] == 'muletjr10'):
        muletjr10_actual = muletjr10_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(muletjr10_actual)

    if (data[1+(i*5)] == 'makinaone'):
        makinaone_actual = makinaone_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(makinaone_actual)

    if (data[1+(i*5)] == 'Tugoressss'):
        Tugoressss_actual = Tugoressss_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Tugoressss_actual)

    if (data[1+(i*5)] == 'PRATS'):
        PRATS_actual = PRATS_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(PRATS_actual)

    if (data[1+(i*5)] == 'Elpu7'):
        Elpu7_actual = Elpu7_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Elpu7_actual)

    if (data[1+(i*5)] == 'Sporting de Cananú'):
        Sporting_de_Cananú_actual = Sporting_de_Cananú_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Sporting_de_Cananú_actual)

    if (data[1+(i*5)] == 'Ensaimada City'):
        Ensaimada_City_actual = Ensaimada_City_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Ensaimada_City_actual)

    if (data[1+(i*5)] == 'Jorch579'):
        Jorch579_actual = Jorch579_actual + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Jorch579_actual)

    if (data[1+(i*5)] == 'Al-bert Ibn al-Ettif'):
        Al_bert_Ibn_al_Ettif = Al_bert_Ibn_al_Ettif + int(data[1+(i*5)+2])
        PUNTOS_ACUMULATIVOS.append(Al_bert_Ibn_al_Ettif)

for i in range(0, int(len(data)/5)):
    PRECIO_EQUIPO.append(int(data[2+(i*5)].replace('.','')))
    print(PRECIO_EQUIPO)

for i in range(0, int(len(data)/5)):
    PUNTOS_JORNADA.append(int(data[3+(i*5)]))

for i in range(0, len(JUGADORES)):
    JORNADA.append(int((i/10)+1))

print('Jornadas')
print(JORNADA) 

print('Jugadores')
print(JUGADORES)

print('Precio del Equipo')
print(PRECIO_EQUIPO)

print('Puntos por Jornada')
print(PUNTOS_JORNADA)

print('Puntos acumultaivos')
print(PUNTOS_ACUMULATIVOS)

print('Posición')
print(POSICION)


# Info puntos x jornada muletjr10 || 'muletjr10', 'Payo Cayetano', 'makinaone', 'Tugoressss', 'PRATS', 'Elpu7', 'Sporting de Cananú', 'Ensaimada City', 'Jorch579', 'Al-bert Ibn al-Ettif'
puntos_jornada_muletjr10 = []
puntos_jornada_PRATS = []
puntos_jornada_Elpu7 = []
puntos_jornada_makinaone = []
puntos_jornada_Payo_Cayetano = []
puntos_jornada_Tugoressss = []
puntos_jornada_Sporting_de_Cananu = []
puntos_jornada_Ensaimada_City = []
puntos_jornada_Jorch579 = []
puntos_jornada_Al_bert_Ibn_al_Ettif = []

InsertFixture = f"INSERT IGNORE INTO fixtures (infofantasy_id, fixtures_fixture, fixtures_position, fixtures_points, fixtures_acumulativepoints, fixtures_teamprice, fixtures_players_name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
InsertPlayers = f"INSERT IGNORE INTO players (players_name) VALUES (%s)"

for i in range(0, len(JUGADORES)):
    if JUGADORES[i] == 'muletjr10':
        puntos_jornada_muletjr10.append(PUNTOS_JORNADA[i])
    
    if JUGADORES[i] == 'PRATS':
        puntos_jornada_PRATS.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Elpu7':
        puntos_jornada_Elpu7.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'makinaone':
        puntos_jornada_makinaone.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Payo Cayetano':
        puntos_jornada_Payo_Cayetano.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Tugoressss':
        puntos_jornada_Tugoressss.append(PUNTOS_JORNADA[i])
    
    if JUGADORES[i] == 'Sporting de Cananú':
        puntos_jornada_Sporting_de_Cananu.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Ensaimada City':
        puntos_jornada_Ensaimada_City.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Jorch579':
        puntos_jornada_Jorch579.append(PUNTOS_JORNADA[i])

    if JUGADORES[i] == 'Al-bert Ibn al-Ettif':
        puntos_jornada_Al_bert_Ibn_al_Ettif.append(PUNTOS_JORNADA[i])
print('--')
print(puntos_jornada_muletjr10)
print(puntos_jornada_PRATS)
print(puntos_jornada_Elpu7)
print(puntos_jornada_makinaone)
print(puntos_jornada_Payo_Cayetano)
print(puntos_jornada_Tugoressss)
print(puntos_jornada_Sporting_de_Cananu)
print(puntos_jornada_Ensaimada_City)
print(puntos_jornada_Jorch579)
print(puntos_jornada_Al_bert_Ibn_al_Ettif)




# for i in range(0, 10):
    # cursor = conexion.cursor()
    # cursor.execute(InsertPlayers, [JUGADORES[i]])
    # conexion.commit()
    # cursor.close()

# for i in range(0, len(JUGADORES)):
    # UNIQUE_PLAYERPERJORNADA = str(JORNADA[i])+str(JUGADORES[i])
    # cursor = conexion.cursor()
    # cursor.execute(InsertFixture, [UNIQUE_PLAYERPERJORNADA,JORNADA[i],POSICION[i],PUNTOS_JORNADA[i],PUNTOS_ACUMULATIVOS[i],PRECIO_EQUIPO[i],JUGADORES[i]])
    # conexion.commit()
    # cursor.close()

## query para obtener grafica puntos acumulativos del fantasy
# SELECT 
#     p1.players_name, 
#     f1.fixtures_acumulativepoints AS F1, 
#     f2.fixtures_acumulativepoints AS F2,
#     f3.fixtures_acumulativepoints AS F3,
#     f4.fixtures_acumulativepoints AS F4,
#     f5.fixtures_acumulativepoints AS F5,
#     f6.fixtures_acumulativepoints AS F6,
#     f7.fixtures_acumulativepoints AS F7,
#     f8.fixtures_acumulativepoints AS F8,
#     f9.fixtures_acumulativepoints AS F9,
#     f10.fixtures_acumulativepoints AS F10,
#     f11.fixtures_acumulativepoints AS F11,
#     f12.fixtures_acumulativepoints AS F12,
#     f13.fixtures_acumulativepoints AS F13,
#     f14.fixtures_acumulativepoints AS F14,
#     f15.fixtures_acumulativepoints AS F15,
#     f16.fixtures_acumulativepoints AS F16,
#     f17.fixtures_acumulativepoints AS F17,
#     f18.fixtures_acumulativepoints AS F18,
#     f19.fixtures_acumulativepoints AS F19,
#     f20.fixtures_acumulativepoints AS F20,
#     f21.fixtures_acumulativepoints AS F21,
#     f22.fixtures_acumulativepoints AS F22,
#     f23.fixtures_acumulativepoints AS F23,
#     f24.fixtures_acumulativepoints AS F24
# FROM 
#     players AS p1
#     INNER JOIN fixtures AS f1 ON f1.fixtures_players_name = p1.players_name
#     INNER JOIN players AS p2 ON p2.players_name = p1.players_name
#     INNER JOIN fixtures AS f2 ON f2.fixtures_players_name = p2.players_name
#     INNER JOIN players AS p3 ON p3.players_name = p2.players_name
#     INNER JOIN fixtures AS f3 ON f3.fixtures_players_name = p3.players_name
#     INNER JOIN players AS p4 ON p4.players_name = p3.players_name
#     INNER JOIN fixtures AS f4 ON f4.fixtures_players_name = p4.players_name
#     INNER JOIN players AS p5 ON p5.players_name = p4.players_name
#     INNER JOIN fixtures AS f5 ON f5.fixtures_players_name = p5.players_name
#     INNER JOIN players AS p6 ON p6.players_name = p5.players_name
#     INNER JOIN fixtures AS f6 ON f6.fixtures_players_name = p6.players_name
#     INNER JOIN players AS p7 ON p7.players_name = p6.players_name
#     INNER JOIN fixtures AS f7 ON f7.fixtures_players_name = p7.players_name
#     INNER JOIN players AS p8 ON p8.players_name = p7.players_name
#     INNER JOIN fixtures AS f8 ON f8.fixtures_players_name = p8.players_name
#     INNER JOIN players AS p9 ON p9.players_name = p8.players_name
#     INNER JOIN fixtures AS f9 ON f9.fixtures_players_name = p9.players_name
#     INNER JOIN players AS p10 ON p10.players_name = p9.players_name
#     INNER JOIN fixtures AS f10 ON f10.fixtures_players_name = p10.players_name
#     INNER JOIN players AS p11 ON p11.players_name = p10.players_name
#     INNER JOIN fixtures AS f11 ON f11.fixtures_players_name = p11.players_name
#     INNER JOIN players AS p12 ON p12.players_name = p11.players_name
#     INNER JOIN fixtures AS f12 ON f12.fixtures_players_name = p12.players_name
#     INNER JOIN players AS p13 ON p13.players_name = p12.players_name
#     INNER JOIN fixtures AS f13 ON f13.fixtures_players_name = p13.players_name
#     INNER JOIN players AS p14 ON p14.players_name = p13.players_name
#     INNER JOIN fixtures AS f14 ON f14.fixtures_players_name = p14.players_name
#     INNER JOIN players AS p15 ON p15.players_name = p14.players_name
#     INNER JOIN fixtures AS f15 ON f15.fixtures_players_name = p15.players_name
#     INNER JOIN players AS p16 ON p16.players_name = p15.players_name
#     INNER JOIN fixtures AS f16 ON f16.fixtures_players_name = p16.players_name
#     INNER JOIN players AS p17 ON p17.players_name = p16.players_name
#     INNER JOIN fixtures AS f17 ON f17.fixtures_players_name = p17.players_name
#     INNER JOIN players AS p18 ON p18.players_name = p17.players_name
#     INNER JOIN fixtures AS f18 ON f18.fixtures_players_name = p18.players_name
#     INNER JOIN players AS p19 ON p19.players_name = p18.players_name
#     INNER JOIN fixtures AS f19 ON f19.fixtures_players_name = p19.players_name
#     INNER JOIN players AS p20 ON p20.players_name = p19.players_name
#     INNER JOIN fixtures AS f20 ON f20.fixtures_players_name = p20.players_name
#     INNER JOIN players AS p21 ON p21.players_name = p20.players_name
#     INNER JOIN fixtures AS f21 ON f21.fixtures_players_name = p21.players_name
#     INNER JOIN players AS p22 ON p22.players_name = p21.players_name
#     INNER JOIN fixtures AS f22 ON f22.fixtures_players_name = p22.players_name
#     INNER JOIN players AS p23 ON p23.players_name = p22.players_name
#     INNER JOIN fixtures AS f23 ON f23.fixtures_players_name = p23.players_name
#     INNER JOIN players AS p24 ON p24.players_name = p23.players_name
#     INNER JOIN fixtures AS f24 ON f24.fixtures_players_name = p24.players_name
# WHERE 
#     p1.players_name = 'makinaone' AND 
#     f1.fixtures_fixture = 1 
#     AND f2.fixtures_fixture = 2
#     AND f3.fixtures_fixture = 3
#     AND f4.fixtures_fixture = 4
#     AND f5.fixtures_fixture = 5
#     AND f6.fixtures_fixture = 6
#     AND f7.fixtures_fixture = 7
#     AND f8.fixtures_fixture = 8
#     AND f9.fixtures_fixture = 9
#     AND f10.fixtures_fixture = 10
#     AND f11.fixtures_fixture = 11
#     AND f12.fixtures_fixture = 12
#     AND f13.fixtures_fixture = 13
#     AND f14.fixtures_fixture = 14
#     AND f15.fixtures_fixture = 15
#     AND f16.fixtures_fixture = 16
#     AND f17.fixtures_fixture = 17
#     AND f18.fixtures_fixture = 18
#     AND f19.fixtures_fixture = 19
#     AND f20.fixtures_fixture = 20
#     AND f21.fixtures_fixture = 21
#     AND f22.fixtures_fixture = 22
#     AND f23.fixtures_fixture = 23
#     AND f24.fixtures_fixture = 24;


## query para obtener grafica puntos x jornada del fantasy
# SELECT 
#     p1.players_name, 
#     f1.fixtures_points AS F1, 
#     f2.fixtures_points AS F2,
#     f3.fixtures_points AS F3,
#     f4.fixtures_points AS F4,
#     f5.fixtures_points AS F5,
#     f6.fixtures_points AS F6,
#     f7.fixtures_points AS F7,
#     f8.fixtures_points AS F8,
#     f9.fixtures_points AS F9,
#     f10.fixtures_points AS F10,
#     f11.fixtures_points AS F11,
#     f12.fixtures_points AS F12,
#     f13.fixtures_points AS F13,
#     f14.fixtures_points AS F14,
#     f15.fixtures_points AS F15,
#     f16.fixtures_points AS F16,
#     f17.fixtures_points AS F17,
#     f18.fixtures_points AS F18,
#     f19.fixtures_points AS F19,
#     f20.fixtures_points AS F20,
#     f21.fixtures_points AS F21,
#     f22.fixtures_points AS F22,
#     f23.fixtures_points AS F23,
#     f24.fixtures_points AS F24
# FROM 
#     players AS p1
#     INNER JOIN fixtures AS f1 ON f1.fixtures_players_name = p1.players_name
#     INNER JOIN players AS p2 ON p2.players_name = p1.players_name
#     INNER JOIN fixtures AS f2 ON f2.fixtures_players_name = p2.players_name
#     INNER JOIN players AS p3 ON p3.players_name = p2.players_name
#     INNER JOIN fixtures AS f3 ON f3.fixtures_players_name = p3.players_name
#     INNER JOIN players AS p4 ON p4.players_name = p3.players_name
#     INNER JOIN fixtures AS f4 ON f4.fixtures_players_name = p4.players_name
#     INNER JOIN players AS p5 ON p5.players_name = p4.players_name
#     INNER JOIN fixtures AS f5 ON f5.fixtures_players_name = p5.players_name
#     INNER JOIN players AS p6 ON p6.players_name = p5.players_name
#     INNER JOIN fixtures AS f6 ON f6.fixtures_players_name = p6.players_name
#     INNER JOIN players AS p7 ON p7.players_name = p6.players_name
#     INNER JOIN fixtures AS f7 ON f7.fixtures_players_name = p7.players_name
#     INNER JOIN players AS p8 ON p8.players_name = p7.players_name
#     INNER JOIN fixtures AS f8 ON f8.fixtures_players_name = p8.players_name
#     INNER JOIN players AS p9 ON p9.players_name = p8.players_name
#     INNER JOIN fixtures AS f9 ON f9.fixtures_players_name = p9.players_name
#     INNER JOIN players AS p10 ON p10.players_name = p9.players_name
#     INNER JOIN fixtures AS f10 ON f10.fixtures_players_name = p10.players_name
#     INNER JOIN players AS p11 ON p11.players_name = p10.players_name
#     INNER JOIN fixtures AS f11 ON f11.fixtures_players_name = p11.players_name
#     INNER JOIN players AS p12 ON p12.players_name = p11.players_name
#     INNER JOIN fixtures AS f12 ON f12.fixtures_players_name = p12.players_name
#     INNER JOIN players AS p13 ON p13.players_name = p12.players_name
#     INNER JOIN fixtures AS f13 ON f13.fixtures_players_name = p13.players_name
#     INNER JOIN players AS p14 ON p14.players_name = p13.players_name
#     INNER JOIN fixtures AS f14 ON f14.fixtures_players_name = p14.players_name
#     INNER JOIN players AS p15 ON p15.players_name = p14.players_name
#     INNER JOIN fixtures AS f15 ON f15.fixtures_players_name = p15.players_name
#     INNER JOIN players AS p16 ON p16.players_name = p15.players_name
#     INNER JOIN fixtures AS f16 ON f16.fixtures_players_name = p16.players_name
#     INNER JOIN players AS p17 ON p17.players_name = p16.players_name
#     INNER JOIN fixtures AS f17 ON f17.fixtures_players_name = p17.players_name
#     INNER JOIN players AS p18 ON p18.players_name = p17.players_name
#     INNER JOIN fixtures AS f18 ON f18.fixtures_players_name = p18.players_name
#     INNER JOIN players AS p19 ON p19.players_name = p18.players_name
#     INNER JOIN fixtures AS f19 ON f19.fixtures_players_name = p19.players_name
#     INNER JOIN players AS p20 ON p20.players_name = p19.players_name
#     INNER JOIN fixtures AS f20 ON f20.fixtures_players_name = p20.players_name
#     INNER JOIN players AS p21 ON p21.players_name = p20.players_name
#     INNER JOIN fixtures AS f21 ON f21.fixtures_players_name = p21.players_name
#     INNER JOIN players AS p22 ON p22.players_name = p21.players_name
#     INNER JOIN fixtures AS f22 ON f22.fixtures_players_name = p22.players_name
#     INNER JOIN players AS p23 ON p23.players_name = p22.players_name
#     INNER JOIN fixtures AS f23 ON f23.fixtures_players_name = p23.players_name
#     INNER JOIN players AS p24 ON p24.players_name = p23.players_name
#     INNER JOIN fixtures AS f24 ON f24.fixtures_players_name = p24.players_name
# WHERE 
#     p1.players_name = 'Tugoressss' AND 
#     f1.fixtures_fixture = 1 
#     AND f2.fixtures_fixture = 2
#     AND f3.fixtures_fixture = 3
#     AND f4.fixtures_fixture = 4
#     AND f5.fixtures_fixture = 5
#     AND f6.fixtures_fixture = 6
#     AND f7.fixtures_fixture = 7
#     AND f8.fixtures_fixture = 8
#     AND f9.fixtures_fixture = 9
#     AND f10.fixtures_fixture = 10
#     AND f11.fixtures_fixture = 11
#     AND f12.fixtures_fixture = 12
#     AND f13.fixtures_fixture = 13
#     AND f14.fixtures_fixture = 14
#     AND f15.fixtures_fixture = 15
#     AND f16.fixtures_fixture = 16
#     AND f17.fixtures_fixture = 17
#     AND f18.fixtures_fixture = 18
#     AND f19.fixtures_fixture = 19
#     AND f20.fixtures_fixture = 20
#     AND f21.fixtures_fixture = 21
#     AND f22.fixtures_fixture = 22
#     AND f23.fixtures_fixture = 23
#     AND f24.fixtures_fixture = 24;


# CREATE TABLE IF NOT EXISTS `mydb`.`players` (
#   `players_name` VARCHAR(45) NOT NULL,
#   PRIMARY KEY (`players_name`))
# ENGINE = InnoDB
    
# CREATE TABLE IF NOT EXISTS `mydb`.`fixtures` (
#   `infofantasy_id` VARCHAR(45) NOT NULL,
#   `fixtures_fixture` INT NOT NULL,
#   `fixtures_position` INT NOT NULL,
#   `fixtures_points` INT NOT NULL,
#   `fixtures_acumulativepoints` INT NOT NULL,
#   `fixtures_teamprice` INT NOT NULL,
#   `fixtures_players_name` VARCHAR(45) NOT NULL,
#   PRIMARY KEY (`infofantasy_id`),
#   INDEX `fk_infofantasy_players_idx` (`fixtures_players_name` ASC) VISIBLE,
#   CONSTRAINT `fk_infofantasy_players`
#     FOREIGN KEY (`fixtures_players_name`)
#     REFERENCES `mydb`.`players` (`players_name`)
#     ON DELETE NO ACTION
#     ON UPDATE NO ACTION)
# ENGINE = InnoDB