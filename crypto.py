import cryptocompare
import requests
import pandas as pd
import hvplot.pandas
import numpy as np
import sqlalchemy
import json
import matplotlib.pyplot as plt

def get_crypto_price(symbol, exchange, days):
    api_key = 'ab6ad894d07d6bbe3fc934992e69a745c6a0cea542193cd07d90b120388a85a4'
    api_url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={symbol}&tsym={exchange}&limit={days}&api_key={api_key}'
    raw = requests.get(api_url).json()
    df = pd.DataFrame(raw['Data']['Data'])[['time', 'high', 'low', 'open','close']].set_index('time')
    df.index = pd.to_datetime(df.index, unit = 's')
    return df

api_url2= f' https://cryptofees.info//api/v1/fees'
response = requests.get(api_url2).json()

def btc():
    print('BITCOIN')
    price = cryptocompare.get_price('BTC', 'USD')
    print(price)
    BTC = get_crypto_price('BTC', 'USD', 15)
    
    print(BTC)
    
    BTC.plot(figsize=(10,8), title= 'BTC')
    
    plt.show()
    BTC_info= response['protocols'][6]
    print(f" Coin Name: {BTC_info['name']}")
    print(f" Description: {BTC_info['description']}")
    print(f" Fee Description: {BTC_info['feeDescription']}")
    BTC_df= pd.DataFrame(response['protocols'][6]['fees']).set_index('date')
    BTC_df.index = pd.to_datetime(BTC_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    BTC_df['fee'] = BTC_df['fee'].map('${:,.2f}'.format)
    print(BTC_df)

def eth():
    print("ETHEREUM")
    price = cryptocompare.get_price('eth', 'USD')
    print(price)
    ETH = get_crypto_price('ETH', 'USD', 15)
    print(ETH)
    ETH.plot(figsize=(10,8), title= 'ETHEREUM')
    plt.show()
    ETHER= response['protocols'][0]
    print(f" Blockchain is $ {ETHER['blockchain']}")

    print(f" Coin Name: {ETHER['name']}")
    print(f" Description: {ETHER['description']}")
    print(f" Fee Description: {ETHER['feeDescription']}")
    ETH_df= pd.DataFrame(response['protocols'][0]['fees']).set_index('date')
    ETH_df.index = pd.to_datetime(ETH_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    ETH_df['fee'] = ETH_df['fee'].map('${:,.2f}'.format)
    print(ETH_df)

def uni():
    print("UNISWAP")
    price = cryptocompare.get_price('UNI', 'USD')
    print (price)
    UNI = get_crypto_price('UNI', 'USD', 15)
    print(UNI)
    UNI.plot(figsize=(10,8), title= 'UNISWAP')
    plt.show()
    UNITOKEN= response['protocols'][1]
    print(f" Blockchain is $ {UNITOKEN['blockchain']}")
    print(f" Coin Name: {UNITOKEN['name']}")
    print(f" Description: {UNITOKEN['description']}")
    print(f" Fee Description: {UNITOKEN['feeDescription']}")
    UNI_df= pd.DataFrame(response['protocols'][1]['fees']).set_index('date')
    UNI_df.index = pd.to_datetime(UNI_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    UNI_df['fee'] = UNI_df['fee'].map('${:,.2f}'.format)
    print(UNI_df)   

def bnb():
    print("BINANCE SMART CHAIN")
    price = cryptocompare.get_price('BNB', 'USD')
    print (price)
    bnb = get_crypto_price('BNB', 'USD', 15)
    print(bnb)
    bnb.plot(figsize=(10,8), title= 'BINANCE')
    plt.show()
    BNB= response['protocols'][2]
    print(f" Blockchain is $ {BNB['blockchain']}")
    print(f" Coin Name: {BNB['name']}")
    print(f" Description: {BNB['description']}")
    print(f" Fee Description: {BNB['feeDescription']}")
    BNB_df= pd.DataFrame(response['protocols'][2]['fees']).set_index('date')
    BNB_df.index = pd.to_datetime(BNB_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    BNB_df['fee'] = BNB_df['fee'].map('${:,.2f}'.format)
    print(BNB_df)

def aave():
    print("AAVE")
    price = cryptocompare.get_price('AAVE', 'USD')
    print (price)
    AAVE = get_crypto_price('AAVE', 'USD', 15)
    print(AAVE)
    AAVE.plot(figsize=(10,8), title= 'AAVE')
    plt.show()
    AAVE_DF= response['protocols'][4]
    print(f" Blockchain is $ {AAVE_DF['blockchain']}")
    print(f" Coin Name: {AAVE_DF['name']}")
    print(f" Description: {AAVE_DF['description']}")
    print(f" Fee Description: {AAVE_DF['feeDescription']}")
    AAVE_DF= pd.DataFrame(response['protocols'][4]['fees']).set_index('date')
    AAVE_DF.index = pd.to_datetime(AAVE_DF.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    AAVE_DF['fee'] = AAVE_DF['fee'].map('${:,.2f}'.format)
    print(AAVE_DF)

def sushi():
    print("SUSHISWAP")
    price = cryptocompare.get_price('SUSHI', 'USD')
    print (price)
    SUSHI = get_crypto_price('SUSHI', 'USD', 15)
    print(SUSHI)
    SUSHI.plot(figsize=(10,8), title= 'SUSHISWAP')
    plt.show()
    SUSHI_DF= response['protocols'][5]
    print(f" Blockchain is $ {SUSHI_DF['blockchain']}")
    print(f" Coin Name: {SUSHI_DF['name']}")
    print(f" Description: {SUSHI_DF['description']}")
    print(f" Fee Description: {SUSHI_DF['feeDescription']}")
    SUSHI_DF= pd.DataFrame(response['protocols'][5]['fees']).set_index('date')
    SUSHI_DF.index = pd.to_datetime(SUSHI_DF.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    SUSHI_DF['fee'] = SUSHI_DF['fee'].map('${:,.2f}'.format)
    print(SUSHI_DF)
    
def comp():
    print("COMPOUND")
    price = cryptocompare.get_price('COMP', 'USD')
    print (price)
    COMP= get_crypto_price('COMP', 'USD', 15)
    print(COMP)
    COMP.plot(figsize=(10,8), title= 'COMPOUND')
    plt.show()
    COMP_DF= response['protocols'][7]
    print(f" Blockchain is $ {COMP_DF['blockchain']}")
    print(f" Coin Name: {COMP_DF['name']}")
    print(f" Description: {COMP_DF['description']}")
    print(f" Fee Description: {COMP_DF['feeDescription']}")
    COMP_DF= pd.DataFrame(response['protocols'][7]['fees']).set_index('date')
    COMP_DF.index = pd.to_datetime(COMP_DF.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    COMP_DF['fee'] = COMP_DF['fee'].map('${:,.2f}'.format)
    print(COMP_DF)

def maker():
    print("MAKERDAO")
    price = cryptocompare.get_price('MKR', 'USD')
    print (price)
    MAKER= get_crypto_price('MKR', 'USD', 15)
    print(MAKER)
    MAKER.plot(figsize=(10,8), title= 'MAKERdao')
    plt.show()
    MAKER_DF= response['protocols'][11]
    print(f" Blockchain is $ {MAKER_DF['blockchain']}")
    print(f" Coin Name: {MAKER_DF['name']}")
    print(f" Description: {MAKER_DF['description']}")
    print(f" Fee Description: {MAKER_DF['feeDescription']}")
    MAKER_DF= pd.DataFrame(response['protocols'][11]['fees']).set_index('date')
    MAKER_DF.index = pd.to_datetime(MAKER_DF.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    MAKER_DF['fee'] = MAKER_DF['fee'].map('${:,.2f}'.format)
    print(MAKER_DF)

def snx():
    print("SYNTHETIX")
    price = cryptocompare.get_price('SNX', 'USD')
    print (price)
    SNX= get_crypto_price('SNX', 'USD', 15)
    print(SNX)
    SNX.plot(figsize=(10,8), title= 'SYNTHETIX')
    plt.show()
    SNX_DF= response['protocols'][10]
    print(f" Blockchain is $ {SNX_DF['blockchain']}")
    print(f" Coin Name: {SNX_DF['name']}")
    print(f" Description: {SNX_DF['description']}")
    print(f" Fee Description: {SNX_DF['feeDescription']}")
    SNX_DF= pd.DataFrame(response['protocols'][10]['fees']).set_index('date')
    SNX_DF.index = pd.to_datetime(SNX_DF.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    SNX_DF['fee'] = SNX_DF['fee'].map('${:,.2f}'.format)
    print(SNX_DF)

def ada():
    print("Cardano")
    price = cryptocompare.get_price('ADA', 'USD')
    print(price)
    ADA = get_crypto_price('ADA', 'USD', 15)
    print(ADA)
    ADA.plot(figsize=(10,8), title= 'ADA - CARDANO')
    plt.show()
    ADA_info= response['protocols'][19]
    print(f" Coin Name: {ADA_info['name']}")
    print(f" Description: {ADA_info['description']}")
    print(f" Fee Description: {ADA_info['feeDescription']}")
    ADA_df= pd.DataFrame(response['protocols'][19]['fees']).set_index('date')
    ADA_df.index = pd.to_datetime(ADA_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    ADA_df['fee'] = ADA_df['fee'].map('${:,.2f}'.format)
    print(ADA_df)

def doge():
    print('DOGECOIN')
    price = cryptocompare.get_price('DOGE', 'USD')
    print(price)
    DOGE = get_crypto_price('DOGE', 'USD', 15)
    print(DOGE)
    DOGE.plot(figsize=(10,8), title= 'DOGE')
    plt.show()
    DOGE_info= response['protocols'][20]
    print(f" Coin Name: {DOGE_info['name']}")
    print(f" Description: {DOGE_info['description']}")
    print(f" Fee Description: {DOGE_info['feeDescription']}")
    DOGE_df= pd.DataFrame(response['protocols'][20]['fees']).set_index('date')
    DOGE_df.index = pd.to_datetime(DOGE_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    DOGE_df['fee'] = DOGE_df['fee'].map('${:,.2f}'.format)
    print(DOGE_df)

def sol():
    print("SOLANA")
    price = cryptocompare.get_price('SOL', 'USD')
    print(price)
    SOLANA = get_crypto_price('SOL', 'USD', 15)
    print(SOLANA)
    SOLANA.plot(figsize=(10,8), title= 'SOLANO')
    plt.show()

def pol():
    print("Polkadot")
    price = cryptocompare.get_price('DOT', 'USD')
    print(price)
    Polkadot = get_crypto_price('DOT', 'USD', 15)
    print(Polkadot)
    Polkadot.plot(figsize=(10,8), title= 'Polkadot')
    plt.show()
    POLKA= response['protocols'][39]
    print(f" Blockchain is $ {POLKA['blockchain']}")
    print(f" Coin Name: {POLKA['name']}")
    print(f" Description: {POLKA['description']}")
    print(f" Fee Description: {POLKA['feeDescription']}")
    POLKA_df= pd.DataFrame(response['protocols'][39]['fees']).set_index('date')
    POLKA_df.index = pd.to_datetime(POLKA_df.index)
    #'${:, .2f}'.format to roud decimals and dollar$
    POLKA_df['fee'] = POLKA_df['fee'].map('${:,.2f}'.format)
    print(POLKA_df)