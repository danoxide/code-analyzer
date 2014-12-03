Code Analyzer
=============

Code Analyzer to malutki program napisany w Pythonie, który informuje programustę ile linii kodu napisał, w ilu plikach oraz w jakim czasie wykonano całą operację sprawdzania.
Aby zacząć korzystać z narzędzia wystarczy, że skopiujesz plik do katalogu projektu i uruchomisz go w konsoli.

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
