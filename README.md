Code Analyzer
=============

Ten mały program liczy ile jest linii kodu w projekcie. Skrypt musi znajdować się w katalogu głównym projektu.

Aktualizacje
------------
##### 2 grudnia 2014
Możliwość dodawania własnych rozszerzeń dzięki argumentowi `--extensions`, gdzie jako kolejne parametry podajemy rozszerzenia plików, np.
```
$ python analyzer.py --extensions html css js php
```

##### 1 grudnia 2014
Dodano wyświetlanie większej ilości danych (ilość otworzonych i sprawdzonych plików oraz czas w jakim wykonano całą operację). Teraz wyniki prezentowane są w postaci:
```
Linii kodu: 561
Łącznie plików: 2
Czas sprawdzenia: 0.0553s
```

Jak używać?
-----------

1. Otwórz terminal
2. Wklej tę linijkę: `python analyzer.py` lub `python analyzer.py --extensions php js`, jeśli chcesz skanować własne pliki.
3. Po zakończonej operacji zostaną wyświetlone wyniki
