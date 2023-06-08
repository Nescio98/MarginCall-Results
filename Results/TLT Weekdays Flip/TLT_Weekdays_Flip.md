# Backtest results of TLT Weekdays Flip

**TLT Weekdays Flip** is a trading strategy for TLT(iShares 20+ Treasury Bonds) that takes into account weekly fluctuations of bonds

</br>

### **<p align="center">INTERACTIVE BACKTEST RESULTS AT THIS <a href="https://nescio98.github.io/MarginCall-Results/TLT_Weekdays_Flip.html">LINK</a></p>**


# Index

* [Result comparison with Buy and Hold](#result-comparison-with-buy-and-hold)
* [Results year per year](#results-year-by-year)
* [Results compounding](#compounded-results-over-23-years)
* [Comparison with TLT](#comparison-with-tlt_weekdays_flip)


## Result comparison with Buy and Hold
This image shows how the strategy **outperformed** the Buy and Hold strategy not only **overall** but especially in the worst of the **downturns** with fews negative returns.

![TLT_Weekdays_Flip_vs_Buy_and_Hold](https://github.com/Nescio98/MarginCall-Results/blob/63a7dfc29a5082c720fe4d011794b4a27f084a0e/docs/img/TLT_Weekdays_Flip%20vs%20Buy%20and%20Hold.png)

## Results Year-By-Year


|     Year     | Returns (%) | Buy and Hold (%) | Number of Trades | % of Winning Trades | Max Drawdown (%) | Avg Drawdown (%) | Exposure Time (%) |
|:------------:|:-----------:|:---------------:|:---------------:|:------------------:|:----------------:|:----------------:|:-----------------:|
|  2005-2006   |    11.33    |       4.94      |        22       |       68.18        |       -5.85      |       -1.0       |       61.11       |
|  2006-2007   |    7.15     |      -3.54      |        22       |       63.64        |       -4.73      |      -1.29       |       61.35       |
|  2007-2008   |    16.02    |       3.99      |        22       |       68.18        |       -2.72      |      -0.98       |       61.35       |
|  2008-2009   |    -7.4     |       30.2      |        22       |       54.55        |      -11.83      |      -4.58       |       60.87       |
|  2009-2010   |    23.73    |      -25.23     |        22       |       72.73        |       -9.91      |      -1.73       |       61.11       |
|  2010-2011   |    30.89    |       4.09      |        22       |       72.73        |       -5.73      |      -1.42       |       61.11       |
|  2011-2012   |    -9.02    |      29.95      |        22       |        50.0        |      -23.38      |      -2.35       |       61.11       |
|  2012-2013   |    23.31    |       2.89      |        22       |       68.18        |       -6.23      |      -1.24       |       61.6        |
|  2013-2014   |    19.15    |      -14.59     |        22       |       77.27        |       -4.81      |      -1.11       |       61.11       |
|  2014-2015   |    20.86    |      23.57      |        22       |       72.73        |       -4.49      |      -0.92       |       61.11       |
|  2015-2016   |    33.32    |      -4.53      |        22       |       72.73        |       -7.39      |      -1.59       |       61.11       |
|  2016-2017   |    14.09    |      -2.58      |        22       |       54.55        |       -6.63      |      -1.33       |       61.11       |
|  2017-2018   |    -3.21    |       6.83      |        22       |       45.45        |       -8.09      |      -3.68       |       61.35       |
|  2018-2019   |    15.68    |      -4.62      |        22       |       72.73        |       -4.07      |      -1.06       |       61.35       |
|  2019-2020   |    19.45    |      11.96      |        22       |       68.18        |       -5.63      |      -1.31       |       61.11       |
|  2020-2021   |    11.57    |      15.11      |        22       |       54.55        |      -11.03      |      -2.71       |       60.87       |
|  2021-2022   |    -0.15    |      -5.66      |        22       |       54.55        |      -11.27      |      -3.58       |       61.11       |


## Compounded results over 23 years

The **final equity** since January 2005 is **988%%** of the initial capital, starting with **10 000 USD** and **allocating 100%** of equity to every trade, ie. **compounding**, including **0.05% broker's fees** on each trade

### Strenghts:
* It had only 3 negative yearly returns over 17 years
* Maximum drawdown of -23.4%
* High yearly returns overall



|            Metric             |         Value          |
|:-------------------------------:|:----------------------:|
|            Start              |  2005-01-03 00:00:00   |
|             End               |  2023-06-08 00:00:00   |
|           Duration            |    6730 days 00:00:00  |
|      Exposure Time [%]        |       66.637931       |
|       Equity Final [$]        |     98815.136964      |
|        Equity Peak [$]        |     102954.76958      |
|         Return [%]            |       888.15137       |
|    Buy & Hold Return [%]      |       14.588574       |
|      Return (Ann.) [%]        |       13.247652       |
|    Volatility (Ann.) [%]      |       12.998498       |
|         Sharpe Ratio          |       1.019168        |
|        Sortino Ratio          |       1.761362        |
|         Calmar Ratio          |       0.566055        |
|      Max. Drawdown [%]        |      -23.403488       |
|      Avg. Drawdown [%]        |      -1.845896        |
| Max. Drawdown Duration  | 476 days 00:00:00  |
| Avg. Drawdown Duration   |  30 days 00:00:00   |
|            # Trades           |          442           |
|       Win Rate [%]        |       62.443439       |
|        Best Trade [%]         |       6.721988        |
|       Worst Trade [%]         |      -8.172964        |
|       Avg. Trade [%]         |       0.520562        |
|    Max. Trade Duration  |  13 days 00:00:00   |
|   Avg. Trade Duration    |  10 days 00:00:00   |
|         Profit Factor         |       1.926831        |
|       Expectancy [%]        |       0.543089        |
|             SQN               |       4.109203         |



## Comparison with QQQ_Mean_Reversion
This is an interesting comparison to [another strategy] we backtested. They seem to have **complementary returns**, covering each other in their respective worst years. Also, they are strategies on **not correlated instruments** ( QQQ vs. TLT).

![comparison QQQ vs TLT](https://github.com/Nescio98/MarginCall-Results/blob/2e94dbfe5cb2770bd7eb1cc8a076a693ca6a18fe/docs/img/QQQ_Mean_Reversion%20vs%20TLT_Weekdays_Flip.png)


