# print-calendar
Ezt a kódot a linkedin.com Python Developers Community csoportjában, Meena Dogra által publikált naptárkép ihlette. Hogy ne legyen annyira egyszerű a feladat, a kód nem tartalmaz semmilyen importált modult.

This code was inspired by a calendar image published by Meena Dogra in the Python Developers Community group on linkedin.com. To make it not so simple, the code does not contain any imported modules.

Használatának egyszerűsége vetekszik a haszontalanságának mértékével.

```
c = Calendar(2020, 2)
print(c)
```

Output:
```
   2020. február
hé ke sz cs pé sz va
                1  2
 3  4  5  6  7  8  9
10 11 12 13 14 15 16
17 18 19 20 21 22 23
24 25 26 27 28 29

```

Ha paraméterként csak az évszám kerül megadásra, akkor a teljes évet kiírja.

If only the year is specified as the parameter, the full year is displayed.

```
c = Calendar(2020)
print(c)
```