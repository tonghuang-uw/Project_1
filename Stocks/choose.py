import pandas as pd
from pandas.core.window.rolling import Window
import sqlalchemy as sql
import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import questionary
import numpy as np



    
    




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