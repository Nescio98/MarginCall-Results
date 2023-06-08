# Backtest results of QQQ Mean Reversion

**QQQ Mean Reversion** is a trading strategy for QQQ(Nasdaq) that takes into account RSI and IBS indicators

Live backtest result at this [link](https://nescio98.github.io/MarginCall-Results/QQQ_Mean_Reversion.html)

# Index

* [Result comparison with Buy and Hold](#result-comparison-with-buy-and-hold)
* [Results year per year](#results-year-per-year)
* [Results compounding](#results-compounding)
* [Comparison with TLT](#comparison-with-tlt)


## Result comparison with Buy and Hold
![QQQ_Mean_Reversion vs Buy and Hold](https://github.com/Nescio98/MarginCall-Results/assets/101431140/8534e5fe-67ab-402b-9566-bd732bd754ca)



|           | Returns % | Buy and Hold | Number of trades | % of winning trades | Max_drawdown | Avg_drawdown | Exposure_time % |
|-----------|-----------|--------------|------------------|---------------------|--------------|--------------|-----------------|
| 2000-2001 |   70.11   |     -36.0     |         9               |         88.89            |     -12.6       |     -5.55       |       14.29          |
| 2001-2002 |   11.58   |     -31.17   |         9               |         77.78            |     -17.3       |     -6.0         |       19.76          |
| 2002-2003 |   28.74   |     -37.98   |         11             |         90.91            |     -7.41       |     -5.05       |       22.22          |
| 2003-2004 |   14.48   |     48.14     |         4               |         100.0            |     -3.84       |     -1.23       |       8.33            |
| 2004-2005 |   11.76   |     9.19       |         7               |         100.0            |     -2.66       |     -1.79       |       12.3            |
| 2005-2006 |   3.98     |     1.12       |         7               |         85.71             |     -2.44       |     -1.37       |       13.1            |
| 2006-2007 |   3.49     |     6.25       |         5               |         80.0               |     -5.32       |     -1.93       |       11.55          |
| 2007-2008 |   2.11     |     18.66     |         4               |         75.0               |     -2.72       |     -2.65       |       6.77            |
| 2008-2009 |   31.43   |     -42.54   |         10             |         70.0               |     -19.45     |     -6.57       |       17.79          |
| 2009-2010 |   23.53   |     55.5       |         7               |         71.43             |     -7.49       |     -2.89       |       13.89          |
| 2010-2011 |   7.52     |     17.83     |         5               |         80.0               |     -4.27       |     -2.24       |       11.9            |
| 2011-2012 |   9.93     |     1.64       |         8               |         87.5               |     -10.9       |     -3.05       |       12.3            |
| 2012-2013 |   0.3       |     11.95     |         6               |         50.0               |     -4.4         |     -4.4         |       12.4            |
| 2013-2014 |   4.35     |     31.2       |         2               |         100.0             |     -0.16       |     -0.16       |       3.17            |
| 2014-2015 |   5.21     |     19.36     |         4               |         75.0               |     -1.64       |     -1.64       |       5.16            |
| 2015-2016 |   2.71     |     8.78       |         6               |         83.33             |     -8.39       |     -3.15       |       8.33            |
| 2016-2017 |   9.73     |     9.58       |         8               |         87.5               |     -3.19       |     -1.73       |       15.48          |
| 2017-2018 |   3.23     |     31.53     |         2               |         100.0             |     -0.44       |     -0.3         |       3.59            |
| 2018-2019 |   7.58     |     -1.33      |         6               |         83.33             |     -7.8         |     -3.91       |       11.95          |
| 2019-2020 |   1.86     |     40.1       |         3               |         66.67             |     -3.13       |     -2.67       |       5.56            |
| 2020-2021 |   19.57   |     45.93     |         5               |         100.0             |     -4.96       |     -3.37       |       7.91            |
| 2021-2022 |   9.36     |     26.83     |         5               |         100.0             |     -2.09       |     -1.0         |       7.94            |


## Compounded results over 23 years

The **final equity** since January 2000 is **1673%** of the initial capital, starting with **10 000 USD** and **allocating 100%** of equity to every trade, ie. **compounding**, including **0.05% broker's fees** on each trade

### Strenghts:
* It never had a negative yearly return in the last 23 years
* Maximum drawdown of -19%
* Exposure time of only 11%


| Metric                     | Value              |
|----------------------------|--------------------|
| Start                      | 2000-01-03 00:00:00|
| End                        | 2023-06-07 00:00:00|
| Duration                   | 8556 days 00:00:00 |
| Exposure Time [%]          | 11.518236          |
| Equity Final [$]           | 177342.875828      |
| Equity Peak [$]            | 177342.875828      |
| Return [%]                 | 1673.428758        |
| Buy & Hold Return [%]      | 269.034305         |
| Return (Ann.) [%]          | 13.079637          |
| Volatility (Ann.) [%]      | 14.386543          |
| Sharpe Ratio               | 0.909158           |
| Sortino Ratio              | 2.017805           |
| Calmar Ratio               | 0.670973           |
| Max. Drawdown [%]          | -19.493541         |
| Avg. Drawdown [%]          | -3.429956          |
| Max. Drawdown Duration     | 218 days 00:00:00  |
| Avg. Drawdown Duration     | 37 days 00:00:00   |
| # Trades                   | 149                |
| Win Rate [%]               | 83.892617          |
| Best Trade [%]             | 16.783713          |
| Worst Trade [%]            | -12.69852          |
| Avg. Trade [%]             | 1.95076            |
| Max. Trade Duration        | 18 days 00:00:00   |
| Avg. Trade Duration        | 6 days 00:00:00    |
| Profit Factor              | 6.600219           |
| Expectancy [%]             | 2.005584           |
| SQN                        | 7.285934           |


## Comparison with TLT_Weekdays_Flip
This is an interesting comparison to another strategy we backtested. They seem to have **complementary returns**, covering each other in their respective worst years. Also, they are strategies on **not correlated instruments** ( QQQ vs. TLT).
![image_2023-06-07_01-51-10](https://github.com/Nescio98/MarginCall-Results/assets/101431140/0f55e943-c97a-4d1f-ae9c-dbbb128cac3c)


