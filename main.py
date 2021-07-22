import questionary
import pandas as pd
import alpaca_trade_api as tradeapi
from questionary import question
import sqlalchemy as sql
import os
from dotenv import load_dotenv
import numpy as np
import scipy.optimize as sco




from analysis import (
    moving_average_analysis,
    mean_variance_analysis,
    technical_analysis
)

from crypto import (
    btc,
    eth,
    uni,
    bnb,
    aave,
    sushi,
    maker,
    snx,
    ada,
    comp,
    doge,
    sol,
    pol
)


def choose_stocks_or_cryptos():
    """ Ask users if they want to select stocks or crypto, and select one of them.

    Returns:
         Either a stock ticker or a cryptocurrency.
    """

    s_o_c = questionary.select(
        "Which section do you want to select?",
        choices = ["Stocks", "Cryptocurrency"],
    ).ask()
    return s_o_c
                
        
def technical_analysis_choice():
    """Ask users if they want to analyze the technical side of a ticker.

    Returns:
        A string of choice user make.
    """

    print("---There are two types of technical analysis for you---")
    print("---Moving Average/ Mean and Variance---")
    print("......")
    print("Both ways of technical analysis will base on the historical data of the ticker you chose!")
    technical_analysis_choice = questionary.select(
        "Which technical analysis do you want to see?",
        choices=["Moving Average", "Mean and Variance"],
        ).ask()
    print("...Running to get the result for technical analysis of the ticker...")
    
    return  technical_analysis_choice


def load_ticker(ticker):
    """Load data based on users choice from 07/01/2018 to 07/01/2021.

    Parameter: A string
    Returns:
        A dataframe of a ticker
    """
    timeframe = "1D"
    start_date = pd.Timestamp("2018-07-01",tz = "America/New_York").isoformat()
    end_date = pd.Timestamp("2021-07-01",tz = "America/New_York").isoformat()
    df = alpaca.get_barset(ticker, timeframe, limit = 1000, start = start_date, end = end_date).df

    # Choosing only close price data for the dataframe.
    
    df = pd.DataFrame(df[f'{ticker}']['close'])
    
    return df

def add_to_watch_list(ticker):
    """ Ask users if they want to add the ticker into watchlist.
    
    """
    
    add_or_not = questionary.confirm("Do you want to add the ticker into watchlist?").ask()
    
    if add_or_not == True:
        df.to_sql(
            f'{ticker}', 
            engine, 
            index=False, 
            if_exists='replace')

def optimazer_tickers():
    """ Choose what tickers user want for optimizer from sql.

    """
    list = engine.table_names()
    print(list)

    tickers = questionary.checkbox(
        'Choose stocks',
        choices = list).ask()

    return tickers

def statistics(weights):
    """
    Returns portfolio statistics
    """
    
    weights = np.array(weights)
    pret = np.sum(log_returns.mean() * weights) * 252
    pvol = np.sqrt(np.dot(weights.T, np.dot(log_returns.cov() * 252, weights)))
    return np.array([pret,pvol])

def min_func_variance(weights):
    return statistics(weights)[1] ** 2

def delete_ticker():

    list = engine.table_names()
    print("Do you want to delete any tickers in your watchlist?")
    print("Press ENTER if you don't want to delete any!")

    tickers = questionary.checkbox(
        "Choose tickers",
        choices=list
    ).ask()
    return tickers


if __name__ == "__main__":
    
    load_dotenv()

    alpaca_api_key = os.getenv("ALPACA_API_KEY")
    alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")
    alpaca = tradeapi.REST(alpaca_api_key, alpaca_secret_key, api_version ="v2")

    database_connection_string = "sqlite:///./SQL/stocks.db"

    engine = sql.create_engine(database_connection_string)

    print(engine)
    
    s_o_c = choose_stocks_or_cryptos()

    if s_o_c == "Stocks":
        print("\n...Welcome to stock analysis!...\n")
        print("The application will provide a watchlist that you can add stocks and delete stocks\n")
        print("which will also provide you analysis and weighting optimizer!\n")

        ticker = questionary.text(
            "Please enter a ticker name you want to research:(It is case sensitive)"
        ).ask()

        print("Running report ...")
        

        df = load_ticker(ticker)

        choice = technical_analysis_choice()


        technical_analysis(df,choice)

        add_to_watch_list(ticker)

        print(engine.table_names())
    

        if len(engine.table_names()) >= 2:
            print("The application provide an optimization when there are more than two stocks in the portfolio.")
            opts = questionary.confirm("Do you want to optimize the portfolio by minimizing the risk?").ask()
            if opts == True:
                tickers = optimazer_tickers()
                noa = len(tickers)
                print(tickers)
                data = pd.DataFrame()
            
                for ticker in tickers:
                    data[ticker] = load_ticker(ticker)['close']
                log_returns = np.log(data/data.shift(1))

                weights = np.random.random(noa)
                weights /= np.sum(weights)
                pret,pvar = statistics(weights)
                min_func_variance(weights)
                cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
                bnds = tuple((0, 1) for x in range(noa))
                optv = sco.minimize(min_func_variance, noa * [1. / noa,], method = 'SLSQP', bounds=bnds, constraints=cons)
                optv_weighting = optv['x'].round(3)
                weighting_df = pd.DataFrame(optv_weighting,index=tickers,columns=['Weighting'])
                print(weighting_df)
            else:
                tickers = delete_ticker()
                for ticker in tickers:
                    engine.execute(f'DROP TABLE {ticker}')
        view = questionary.confirm(
            'Do you want to view your watchlist?',
        ).ask()
        if view == True:
            print(engine.table_names())
    else:
        print("\n...Welcome to cryptocurrency analysis!...\n")
        print("This report will return  information of cryptocurrency you choose!")
        
        crypto = questionary.select(
            "Please select a cryptocurrency you want to research:",
            choices=["BTC","ETH","UNI","BNB","AAVE","SUSHI","COMP","MKR","SNX","ADA","DOGE","SOL","POL"]
            ).ask()

        print("Running report...")
        if crypto == "BTC":
            btc()
        elif crypto == "ETH":
            eth()
        elif crypto == "UNI":
            uni()
        elif crypto == "BNB":
            bnb()
        elif crypto == "AAVE":
            aave()
        elif crypto == "SUSHI":
            sushi()
        elif crypto == "COMP":
            comp()
        elif crypto == "MKR":
            maker()
        elif crypto == "SNX":
            snx()
        elif crypto == "ADA":
            ada()
        elif crypto == "DOGE":
            doge()
        elif crypto == "SOL":
            sol()
        else:
            pol()
                
