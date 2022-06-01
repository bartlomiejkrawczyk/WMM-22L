# Wstęp do Multimediów

Laboratorium 8 - Generowanie grafiki z wykorzystaniem popularnej biblioteki graficznej

Bartłomiej Krawczyk, 310774

# Składanie transformacji

Wizualizacja stworzonego robota w innym kolorze niż ten pokazany w instrukcji:

![](./images/robot.png)

# Cieniowanie

Przyjęte podstawowe wartości:
```py
OBJECT_COLOR = (0.8, 0.8, 0.8)
LIGHT_COLOR = (1, 1, 1)

LIGHT_POSITION = (3, 0, 5)
VIEW_POSITION = (5, 0, 0)

SHININESS = 5
```

```c++
// Surroundings factor
float ambient = 0.6;
// Light diffuse factor
float diffuse = 0.6;
// Reflectivity factor
float specular = 0.3;
```


## Położenie źródła światła

| Położenie  | Zdjęcie                   |
|------------|---------------------------|
| (3, 0, 5)  | ![](./images/default.png) |
| (3, 0, -5) | ![](./images/p2.png)      |
| (1, 3, 0)  | ![](./images/p3.png)      |
| (3, -1, 0) | ![](./images/p4.png)      |

## Różna połyskliwość obiektu

| Połyskliwość | Zdjęcie                   |
|--------------|---------------------------|
| 1            | ![](./images/s1.png)      |
| 5            | ![](./images/default.png) |
| 20           | ![](./images/s20.png)     |
| 100          | ![](./images/s100.png)    |

## Różne kolory obiektu

| Kolor obiektu   | Zdjęcie                   |
|-----------------|---------------------------|
| (0.8, 0.8, 0.8) | ![](./images/default.png) |
| (0.8, 0, 0)     | ![](./images/red.png)     |
| (0, 0.8, 0)     | ![](./images/green.png)   |
| (0, 0, 0.8)     | ![](./images/blue.png)    |

## Różne kolory światła


| Kolor światła | Zdjęcie                   |
|---------------|---------------------------|
| (1, 1, 1)     | ![](./images/default.png) |
| (1, 1, 0)     | ![](./images/lyellow.png) |
| (0, 0.3, 0.5) | ![](./images/lblue.png)   |

Aby osiągnąć trochę inne efekty postanowiłem zmienić podstawowy kolor obiektu na:
```py
OBJECT_COLOR = (0.8, 0.2, 0.5)
```

| Kolor światła | Zdjęcie                   |
|---------------|---------------------------|
| (1, 1, 1)     | ![](./images/lpink.png)   |
| (0, 1, 1)     | ![](./images/l_blue.png)  |
| (0.3, 1, 0.4) | ![](./images/l_brown.png) |
| (0, 1, 0)     | ![](./images/l_green.png) |