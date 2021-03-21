import pandas as pd

class RSLineAnalysis:

    __max_counter = 0
    __min_counter = 0

    def __init__(self, extrema, deviation, trigger_zone, trigger_peek, current_price):
        self.__ext = extrema
        # x% Abweichung vom pointer der Folgepunkte ist erlaubt 
        self.__deviation = (current_price / 100) * deviation
        # x% Abstand vom pointer (Preisebene), die überschritten werden müssen für ein Match nach oben, sowie unten
        self.__trigger_peek = (current_price / 100) * trigger_peek
        # x% in dem sich der pointer vom aktuellen Preis befinden muss um aussagekräftig zu sein nach oben, sowie unten
        self.__trigger_zone = (current_price / 100) * trigger_zone

        self.__current_price = current_price
    
    def rsline(self):
        pointer = 0
        #liste mit Minima und Maxima mit chronisch invertierter Reihenfolge
        extrema_list = pd.Series(self.__ext.determine_min()).append(self.__ext.determine_max())
        extrema_list = extrema_list.sort_index(ascending=False).items()
        # Durchlaufe Minima und Maxima
        for pointerDate, pointerPrice in extrema_list:
            if(
                (pointerPrice < self.__current_price+self.__trigger_zone) &
                (pointerPrice > self.__current_price-self.__trigger_zone)
            ):
                # Merke Minima oder Maxima
                pointer = pointerPrice
                # Merke höchsten Minima Preis
                max_match = pointerPrice
                #Merke niedrigsten Maxima Preis
                min_match = pointerPrice
                # Durchlaufe andere Minima ab dem Zeitpunkt des pointers
                for date, price in filter(lambda tupel: tupel[0] < pointerDate, extrema_list):
                    # Wenn Preis höher als höchsten Minima Preis
                    if(price > max_match):
                        # Setze neuen höchsten Minima Preis
                        max_match = price
                    # Wenn Preis niedriger als niedrigster Maxima Preis
                    if(price < min_match):
                        # Setze neuen niedrigsten Maxima Preis
                        min_match = price
                    # Wenn der Preis nicht abseits der Abweichung ist und der Kurs über die angegebenen Prozent war
                    if(
                        (((pointerPrice >= price) & (pointerPrice-self.__deviation <= price)) |
                        ((pointerPrice <= price) & (pointerPrice+self.__deviation >= price))) &
                        (pointerPrice+self.__trigger_peek < max_match)
                    ):
                        # Resette den höchsten Minima Preis
                        max_match = price
                        # Setze den Zähler eins hoch
                        self.__min_counter += 1
                    # Wenn der Preis nicht abseits der Abweichung ist und der Kurs unter die angegebenen Prozent war
                    if(
                        (((pointerPrice >= price) & (pointerPrice-self.__deviation <= price)) |
                        ((pointerPrice <= price) & (pointerPrice+self.__deviation >= price))) &
                        (pointerPrice-self.__trigger_peek > min_match)
                    ):
                        # Resette den niedrigsten Maxima Preis
                        min_match = price
                        # Setze den Zähler eins hoch
                        self.__max_counter += 1
                # Wenn die Matches Länge mindestens drei beträgt
                if(self.__min_counter+self.__max_counter >= 3):
                    # beende die Suche
                    break
                # sonst
                else:
                    # Resette die Match Zähler für den nächsten Pointer
                    self.__min_counter = 0
                    self.__max_counter = 0
        if(self.__min_counter+self.__max_counter >= 3):
            return pointer
        else:
            return None