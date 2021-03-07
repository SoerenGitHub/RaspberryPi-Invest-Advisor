import matplotlib.pyplot as plt
import pandas as pd
import os

class Graph:

    def __init__(self, arr, name):
        plt.figure()
        pd.Series(arr).plot(figsize=(10,8), alpha=.3)
        
    def draw_down_arrow(self, arr):
        arr.plot(style='.', lw=10, color='red', marker="v")

    def draw_up_arrow(self, arr):
        arr.plot(style='.', lw=10, color='green', marker="^")

    def draw_line(self, arr):
        pd.Series(arr).plot()

    def draw_hline(self, y):
        plt.axhline(y) 

    def show(self):
        plt.show()

    def save(self, name, date):
        self.__create_folder('./temp/'+date+'/')
        plt.savefig('./temp/'+date+'/'+name+'.png')
        return './temp/'+date+'/'+name+'.png'

    def __create_folder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)