from backtesting import Backtest
import yfinance as yf
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np

#from TLT_Weekdays_Flip import TLT_Weekdays_Flip

class Utility:


    @staticmethod
    def print_each_year(start_year: int, stop_year:int, instrument: str, strategy: object, cash = 10000, commission=0.0005):

        def calcola_variazione(numero_precedente, numero_successivo):
            variazione = numero_successivo - numero_precedente
            percentuale_variazione = (variazione / numero_precedente) * 100
            return percentuale_variazione


        years = [str(x) for x in range(start_year, stop_year)]
        equity,exposure_time, returns, max_drawdown, avg_drawdown,buy_and_hold, number_of_trades, win_rate = [],[],[],[],[],[],[],[]# 4, 3, 6, 13, 14,17,18
        for i in range(1,len(years)-1):
            data = yf.download(instrument, start=years[i-1]+"-01-01", end=years[i]+"-01-01")
            backtest = Backtest(data, strategy, cash=cash,trade_on_close=True, commission=commission)
            res = backtest.run()
            exposure_time.append(round(res[3],2))
            equity.append(res[4])
            returns.append(round(res[6],2))
            buy_and_hold.append(round(calcola_variazione(data.loc[data.index[0], "Open"], data.loc[data.index[-1], "Open"]),2))
            max_drawdown.append(round(res[13],2))
            avg_drawdown.append(round(res[14],2))
            win_rate.append(round(res[18],2))
            number_of_trades.append(res[17])

        for i in range(1,len(years)-1):
            print("## "+years[i-1]+"-"+years[i])  
            print("**Returns %**:" + str(returns[i-1]))
            print(" ")
            print("**Buy and Hold**: "+str(buy_and_hold[i-1]))
            print(" ")
            print("**Number of trades**: "+str(number_of_trades[i-1]))
            print(" ")
            print("**% of winning trades**: "+str(win_rate[i-1]))
            print(" ")
            print("**Max_drawdown** :"+str(max_drawdown[i-1]))
            print(" ")
            print("**Avg_drawdown**:"+str(avg_drawdown[i-1]))
            print(" ")
            print("**Exposure_time** % "+str(exposure_time[i-1]))
            print(" ")

    @staticmethod
    def backtest_result(start_year: int, stop_year:int, instrument: str, strategy: object, cash = 10000, commission=0.0005):
        data = yf.download(instrument, start=str(start_year)+"-01-01", end=str(stop_year)+"-01-01")
        backtest = Backtest(data, strategy, cash=cash,trade_on_close=True, commission=commission)
        print(backtest.run())

    @staticmethod
    def backtest_plot(start_year: int, stop_year:int, instrument: str, strategy: object, cash = 10000, commission=0.0005):
        data = yf.download(instrument, start=str(start_year)+"-01-01", end=str(stop_year)+"-01-01")
        backtest = Backtest(data, strategy, cash=cash,trade_on_close=True, commission=commission)
        print(backtest.run())
        backtest.plot(plot_return=True,plot_drawdown=True, show_legend=False)

    @staticmethod
    def plot_difference(start_year: int, stop_year:int, instrument: str, strategy: object, cash = 10000, commission=0.0005):
        
        def calcola_variazione(numero_precedente, numero_successivo):
            variazione = numero_successivo - numero_precedente
            percentuale_variazione = (variazione / numero_precedente) * 100
            return percentuale_variazione


        years = [str(x) for x in range(start_year, stop_year)]
        equity,exposure_time, returns, max_drawdown, avg_drawdown,buy_and_hold, number_of_trades, win_rate = [],[],[],[],[],[],[],[]# 4, 3, 6, 13, 14,17,18
        for i in range(1,len(years)):
            data = yf.download(instrument, start=years[i-1]+"-01-01", end=years[i]+"-01-01")
            backtest = Backtest(data, strategy, cash=cash,trade_on_close=True, commission=commission)
            res = backtest.run()
            returns.append(round(res[6],2))
            buy_and_hold.append(round(calcola_variazione(data.loc[data.index[0], "Open"], data.loc[data.index[-1], "Open"]),2))

        X_axis = np.arange(len(years)-1)
        
        plt.bar(X_axis - 0.15, returns, 0.4, label = strategy.name())
        plt.bar(X_axis + 0.15, buy_and_hold, 0.4, label = 'Buy and Hold')
        
        plt.xticks(X_axis, years[:-1])
        plt.xlabel("Years")
        plt.ylabel("Profits or Loss")
        plt.title("Returns comparison: "+strategy.name())
        plt.legend()
        plt.show()

    @staticmethod
    def plot_compare(start_year: int, stop_year:int, instrument1: str, strategy1: object,instrument2: str, strategy2:object, cash = 10000, commission=0.0005):


        years = [str(x) for x in range(start_year, stop_year)]
        returns1,returns2,  = [],[]
        for i in range(1,len(years)):

            data1 = yf.download(instrument1, start=years[i-1]+"-01-01", end=years[i]+"-01-01")
            backtest1 = Backtest(data1, strategy1, cash=cash,trade_on_close=True, commission=commission)
            res = backtest1.run()
            returns1.append(round(res[6],2))

            data2 = yf.download(instrument2, start=years[i-1]+"-01-01", end=years[i]+"-01-01")
            backtest2 = Backtest(data2, strategy2, cash=cash,trade_on_close=True, commission=commission)
            res=backtest2.run()
            returns2.append(round(res[6],2))


        X_axis = np.arange(len(years)-1)
        
        plt.bar(X_axis - 0.15, returns1, 0.4, label = strategy1.name())
        plt.bar(X_axis + 0.15, returns2, 0.4, label = strategy2.name())
        
        plt.xticks(X_axis, years[:-1])
        plt.xlabel("Years")
        plt.ylabel("Profits or Loss")
        plt.title("Returns comparison: "+strategy1.name()+" vs "+strategy2.name())
        plt.legend()
        plt.show()

