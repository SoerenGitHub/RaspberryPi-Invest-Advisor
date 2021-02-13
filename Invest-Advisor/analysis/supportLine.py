import pandas as pd

class supportLine:

    def __init__(self, extrema):
        self.__ext = extrema
    
    def determine(self):
        min_pointer = 0

        # 1% Abweichung ist erlaubt 
        deviation = ((self.__ext.determine_global_max()-self.__ext.determine_global_min()) / 100) * 2

        # 10% Abstand von min_pointer zu max_pointer muss gegeben sein
        to_max_space = ((self.__ext.determine_global_max()-self.__ext.determine_global_min()) / 100) * 10

        # aktuelle Anzahl
        matchCounter = 0

        # Durchlaufe Minima
        for pointerDate, pointerPrice in pd.Series(self.__ext.determine_min())[::-1].items():

            # Merke Minima
            min_pointer = pointerPrice

            # Merke höchsten Minima Preis
            max_match = pointerPrice

            # Durchlaufe andere Minima ab dem Zeitpunkt des pointers
            for date, price in filter(lambda tupel: tupel[0] < pointerDate, pd.Series(self.__ext.determine_min())[::-1].items()):

                # Wenn Preis höher als höchsten Minima Preis
                if(price > max_match):

                    # Setze neuen höchsten Minima Preis
                    max_match = price

                # Wenn der Preis nicht abseits der Abweichung ist und der Kurs über die angegebenen Prozent war
                if(
                    (((pointerPrice >= price) & (pointerPrice-deviation <= price)) |
                    ((pointerPrice <= price) & (pointerPrice+deviation >= price))) &
                    (pointerPrice+to_max_space < max_match)
                ):

                    # Resette den höchsten Minima Preis
                    max_match = price

                    # Setze den Zähler eins hoch
                    matchCounter += 1

            # Wenn die Matches Länge mindestens drei beträgt
            if(matchCounter >= 3):

                # beende die Suche
                break

           # sonst
            else:

                # Resette den Match Zähler für den nächsten Pointer
                matchCounter = 0

        if(matchCounter >= 3):
            return min_pointer
        else:
            return 0