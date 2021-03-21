import matplotlib.pyplot as plt
import pandas as pd
import os

class Graph:

    def __init__(self, arr):
        plt.figure()
        pd.Series(arr).plot(figsize=(10,8), alpha=.3, label='Close-Price')
        plt.ylabel('Price in EUR')
        
    def draw_down_arrow(self, arr):
        arr.plot(style='.', lw=10, color='red', marker="v")

    def draw_up_arrow(self, arr):
        arr.plot(style='.', lw=10, color='green', marker="^")

    def draw_line(self, arr, label):
        pd.Series(arr).plot(label=label)

    def draw_hline(self, y, label):
        plt.axhline(y, label=label) 

    def show(self):
        plt.show()

    def save(self, name, date):
        plt.legend(loc='best')
        self.__create_folder('./temp/'+date+'/')
        plt.savefig('./temp/'+date+'/'+name+'.png')
        plt.close()
        return './temp/'+date+'/'+name+'.png'

    def __create_folder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)