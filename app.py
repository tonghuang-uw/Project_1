# A Watchlist Analyzer

# Import modules
import pandas as pd
from pandas.core.window.rolling import Window
import sqlalchemy as sql
import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import questionary
import numpy as np

#load env file
load_dotenv()

# Set the variables for the Alpaca API and secret keys
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version ="v2")

# Choose between stocks and crypto
def choose_stocks_or_cryptos():
    """ Ask users if they want to select stocks or crypto, and select one of them.

    Returns:
         Either a stock ticker or a cryptocurrency.
    """

    s_o_c = questionary.select(
        "Which section do you want to select?",
        choices = ["Stocks", "Cryptocurrency"],
    ).ask()
    
    if s_o_c == "Stocks":
        ticker = questionary.text(
            "Please enter a ticker name you want to research:(It is case sensitive)"
        ).ask()
    else:
        crypto = questionary.text(
            "Please enter a cryptocurrency you want to research:"
        ).ask()

    return ticker, crypto

def load_ticker(ticker):
    """Load data based on users choice from 07/01/2018 to 07/01/2021.

    Parameter: A string
    Returns:
        A dataframe of a ticker
    """
    timeframe = "1D"
    start_date = pd.Timestamp("2018-07-01",tz = "America/New_York").isoformat()
    end_date = pd.Timestamp("2021-07-01",tz = "America/New_York").isoformat()
    df = alpaca.get_barset(ticker, timeframe, start = start_date, end = end_date).df

    # Choosing only close price data for the dataframe.
    df = df["close"]
    df.index = df.index.date
    return df

def technical_or_fundamental():
    """Ask users if they want to analyze the technical or fundamental side of a ticker.

    Returns:
        A string of choice user make.
    """

    t_o_f = questionary.select(
        "Which side of the ticker you want to analyze?",
        choices=["Techical","Fundamental"],
    ).ask()
    
    if t_o_f == "Technical":
        print("   There are two types of technical analysis for you")
        print("   Moving Average/ Mean and Variance")
        technical_analysis_choice = questionary.select(
            "Which technical analysis do you want to see?",
            choices=["Moving Average", "Mean and Variance"],
        ).ask()
        print("...Running to get the result for technical analysis of the ticker...")
    else:
        print("...Runing to get the result for fundamental analysis of the ticker...")
    return t_o_f, technical_analysis_choice

def moving_average_analysis(df):
    """ Present a moving_average_analysis

    Parameter: 
        A Dataframe

    Returns:
        A String
     """
     # Calculate the 42 days and 252 days moving average
     
     df["42d"] = np.round(df['close'].rolling(Window=42).mean(),2)
     df["252d"] = np.round(df['close'].rolling(Window=252).mean(),2)

     # Chart
     df["close","42d","252d"].plot(grid=True, figsize=(8,6))
     
     # Give suggestions.
     if df["42d"][-1] > df["252d"][-1]:
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
    rets = df['close']/df['close'].shift(1)

    std = rets.std() * 252

    annualized_returns = rets.mean() * 252
    print(f'The annualized returns of the stock is {annualized_returns}, and the standard deviation of the stock is {std}')





def technical_analysis(ticker, technical_analysis_choice):
    """ Doing technical analysis based on user's choice

    Parameter: A ticker (String)
               A choice (String)
    Returns: 
               Moving Average analysis or Mean and variance analysis
    """
    #Load a dataframe of the ticker
    df = load_ticker(ticker)


    if technical_analysis_choice == "Moving Average":
        print("\n---The Moving Average can define the main trend of the stock.---\n")
        print("......")
        print("The system use 42 days and 252 day moving average as buy and sell signals.\n")
        print("Buy signal: The 42 days moving average is above the 252 day moving average.\n")
        print("Sell signal: The 42 days moving average is below the 252 day moving average.\n")
        print("......")
        moving_average_analysis(df)
    else:
        print("\n---The Mean and Variance can identify the stock's historical performance---\n")
        print("......")
        mean_variance_analysis(df)
