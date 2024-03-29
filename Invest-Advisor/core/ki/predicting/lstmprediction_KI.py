import math
import pandas_datareader as web
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


class LSTMPredictionKI:
    __model = None
    __scaler = None

    def __init__(self, stock, predicting_days) -> None:
        self.__predicting_days = predicting_days
        self.__stock = stock
        self.__train()
        self.__predict()

    def __train(self):
        data=self.__stock.get_history().filter(['Close'])
        dataset = data.values
        train_data_len = math.ceil( len(dataset) * .8 )
        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(dataset)
        train_data = scaled_data[0:train_data_len, :]
        x_train = []
        y_train = []
        for i in range(self.__predicting_days, len(train_data)):
            x_train.append(train_data[i-self.__predicting_days:i, 0])
            y_train.append(train_data[i, 0])
        
        x_train, y_train = np.array(x_train), np.array(y_train)
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
        model.add(LSTM(50, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))

        model.compile(optimizer='adam', loss='mean_squared_error')
        model.fit(x_train, y_train, batch_size=1, epochs=1)

        test_data = scaled_data[train_data_len - self.__predicting_days: , :]
        x_test = []
        y_test = dataset[train_data_len:, :]
        for i in range(self.__predicting_days, len(test_data)):
            x_test.append(test_data[i-self.__predicting_days:i, 0])

        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)

        train = data[:train_data_len]
        valid = data[train_data_len:]
        valid['Predictions'] = predictions

    def __predict(self):
        new_df = self.__stock.get_history().filter(['Close'])
        last_x_days = new_df[-self.__predicting_days:].values
        last_x_days_scaled = scaler.transform(last_x_days)
        x_test = []
        x_test.append(last_x_days_scaled)
        x_test = np.array(x_test)
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        pred_price = model.predict(x_test)
        pred_price = scaler.inverse_transform(pred_price)
        print(pred_price)
       
