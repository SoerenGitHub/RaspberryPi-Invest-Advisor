import yfinance as yf
from yfinance import tickers
import pandas as pd

class Environment:
    _actions = []
    _symbols = []
    _tickers = None
    _current = None
    _index = -1
    _step = 0
    _stepSize = 100
    
    def __init__(self, symbols, stepSize):
        self._symbols = symbols
        self._stepSize = stepSize
        self._tickers = yf.Tickers(" ".join(self._symbols))
        self.next()
    
    def reset(self):
        self._actions = []
        return self._current[:self._stepSize]
    
    def calcReward(self, actions):
        reward = None
        #BUY and SIT gets their reward on SELL
        if 2 in actions[0]:#SELL
            if(len(actions) <= 1):
                reward = 0
            else:
                currentRow = self._current[self._stepSize+self._step]
                actionBuyIndex = [i for i, action in enumerate(actions) if 1 in action][0]#first BUY action index
                buyIndex = len(actions) - actionBuyIndex
                buyRow = self._current[self._stepSize+self._step-buyIndex]
                #reward for all actions => len(actions)
                reward = (buyRow['Open'] - currentRow['Open']) / len(actions)
        return reward
        
        
    def step(self, actions):
        self._step += 1
        newRange = self._current[self._step:self._stepSize+self._step]
        rewards = [self.calcReward(actions)] * len(actions) # => [reward, reward, reward....]
        done = (pd.DataFrame(newRange).index[len(newRange)-1] == self._current.index[len(self._current)-1])
        info = 'nothing'
        return newRange, rewards, done, info
        
    def next(self):
        self._index += 1
        self._current = self._tickers.tickers[self._symbols[self._index].upper()].history(period="5y", interval="1d")