import pandas as pd
from pandas.core.window.rolling import Window
import numpy as np
import matplotlib.pyplot as plt


def moving_average_analysis(df):
    """ Present a moving_average_analysis

    Parameter: 
        A Dataframe
    Returns:
        A String
     """
     # Calculate the 42 days and 252 days moving average
    df["7d"] = np.round(df['close'].rolling(window=7).mean(),2)

    df["21d"] = np.round(df['close'].rolling(window=21).mean(),2)

     # Chart
    df[["close","7d","21d"]].plot(grid=True, figsize=(8,6))

    plt.show()
     
     # Give suggestions.
    if df["7d"][-1] > df["21d"][-1]:
        print("The trend is positive, you can think about buying the stock")
    else:
        print("The trend is negative, I guess it is not a good time to buy the stock")


def mean_variance_analysis(df):
    """It determines the annualized returns and variance(volatility) based on historical data.

    Parameter:
        A dataframe.
    Returns:
        A table.
    """
    rets = np.log(df['close']/df['close'].shift(1))

    std = rets.std()* 252

    annualized_returns = rets.mean() * 252

    print(f'The annualized returns of the stock is {annualized_returns}, and the standard deviation of the stock is {std}')


def technical_analysis(df, technical_analysis_choice):
    """ Doing technical analysis based on user's choice

    Parameter: A ticker (String)
               A choice (String)
    Returns: 
               Moving Average analysis or Mean and variance analysis
    """

    

    if technical_analysis_choice == "Moving Average":
        print("\n---The Moving Average can define the main trend of the stock.---\n")
        print("......")
        print("The system use 7 days and 21 day moving average as buy and sell signals.\n")
        print("Buy signal: The 7 days moving average is above the 21 day moving average.\n")
        print("Sell signal: The 7 days moving average is below the 21 day moving average.\n")
        print("......")
        return moving_average_analysis(df)
    else:
        print("\n---The Mean and Variance can identify the stock's historical performance---\n")
        print("......")
        return mean_variance_analysis(df)