# Método Wanderley de Investimentos (MWI)

"""
This is an auto-searching script for evaluating stock investiments in Brazilian companies
on the stock market, using data from the Status Invest website and referencing.
"""

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import glob
import os
import shutil
import pandas as pd
import numpy as np
import time
import warnings

# Suprimir warnings específicos
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# ----------------------------------------------------------------

download_csv = True  # Alterado para True para testar

investment_amount = 1000

investments = {
    "EMAE4": 654.4,
    "POMO3": 547.2,
    "LAVV3": 494.72,
    "POMO4": 473.46,
    "CAMB3": 487.06,
    "EALT4": 421.12,
    "ITSA4": 602.68,
    "ITSA3": 379.52,
    "CSUD3": 315.2,
    "VULC3": 325.44,
}

# ----------------------------------------------------------------

_this_path = os.path.dirname(os.path.abspath(__file__))

if download_csv:
    # Configurações para suprimir logs do Edge
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    edge_options.add_argument("--log-level=3")  # Suprime a maioria dos logs
    edge_options.add_argument("--disable-logging")
    edge_options.add_argument("--disable-dev-shm-usage")
    edge_options.add_argument("--no-sandbox")
    edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    # Configurar o serviço para suprimir logs
    service = Service(
        os.path.join(_this_path, "msedgedriver.exe"),
        log_path=os.devnull  # Redireciona logs para null
    )
    
    try:
        # Inicializar driver com configurações de supressão de logs
        driver = webdriver.Edge(service=service, options=edge_options)
        
        driver.get("https://statusinvest.com.br/acoes/busca-avancada")
        wait = WebDriverWait(driver, 15)

        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')))
        search_button.click()
        time.sleep(2)

        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/i')))
        download_button.click()
        time.sleep(2)
        
        print("Download realizado com sucesso!")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

    # Encontrar e mover o arquivo baixado
    try:
        old_csv_path = glob.glob(os.path.join(os.path.expanduser("~/Downloads"), "*statusinvest*.csv"))[0]
        new_csv_path = os.path.join(_this_path, "statusinvest_data.csv")
        shutil.move(old_csv_path, new_csv_path)
        print(f"Arquivo movido para: {new_csv_path}")
    except IndexError:
        print("Arquivo CSV não encontrado na pasta de Downloads")
        # Tentar encontrar em outros locais possíveis
        possible_paths = glob.glob(os.path.join(_this_path, "*statusinvest*.csv"))
        if possible_paths:
            new_csv_path = possible_paths[0]
            print(f"Usando arquivo existente: {new_csv_path}")
        else:
            print("Nenhum arquivo CSV encontrado")
            exit(1)
else:
    new_csv_path = glob.glob(os.path.join(_this_path, "*statusinvest*.csv"))[0]

# Resto do código permanece igual...
lines = ''
with open(new_csv_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

df = pd.DataFrame([line.strip().replace('.', '').replace(',', '.').split(';') for line in lines])

df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

df.columns = df.columns.str.strip()
df = df.loc[:,['TICKER', 'PRECO', 'MARGEM BRUTA', 'MARGEM EBIT', 'MARG LIQUIDA', 'DIVIDA LIQUIDA / EBIT', 
               'DIV LIQ / PATRI', 'ROE', 'ROA', 'ROIC', 'LIQUIDEZ MEDIA DIARIA', 'VPA', 'LPA']]

for column in df.columns:
    if column != 'TICKER':
        df[column] = pd.to_numeric(df[column], errors='coerce')

df = df.fillna(0)

# Aplicar filtros de forma mais eficiente
filter_conditions = (
    (df['MARGEM BRUTA'] > 10) &
    (df['MARGEM EBIT'] > 10) &
    (df['MARG LIQUIDA'] > 10) &
    (df['DIVIDA LIQUIDA / EBIT'] < 2) &
    (df['DIV LIQ / PATRI'] < 2) &
    (df['ROE'] > 10) &
    (df['ROA'] > 10) &
    (df['ROIC'] > 10) &
    (df['LIQUIDEZ MEDIA DIARIA'] > 10**5)
)

df = df[filter_conditions].reset_index(drop=True)

# Criar novas colunas usando .copy() para evitar warnings
df['GRAHAM'] = round((1.5 * df['VPA'] * 15 * df['LPA']) ** (1/2), 2)
df['GRAHAM / PRECO'] = df['GRAHAM'] / df['PRECO']
df['OPORTUNIDADE'] = df['GRAHAM / PRECO'] > 1.15

ref_price_idx = df[df['OPORTUNIDADE']]['PRECO'].idxmax()
ref_price = df.loc[ref_price_idx, 'PRECO']

new_df = df.copy()

new_df['QTDE'] = np.where(
    new_df['OPORTUNIDADE'],
    (ref_price / new_df['PRECO']).astype(int),
    0
)
new_df['SHARE'] = round((new_df['QTDE'] * new_df['PRECO']) / (new_df['QTDE'] * new_df['PRECO']).sum(), 2) * 100
new_df['VALUE'] = new_df['PRECO'] * new_df['QTDE']
total_investment = round(new_df['VALUE'].sum(), 2)

print("-"*200)
print(f"This script selected the tickers below as good investments")
print(f"And these are the best options to buy")
print("-"*200)
new_df = new_df[new_df['OPORTUNIDADE']].reset_index(drop=True)
print(new_df)

for ticker in investments.keys():
    '''if ticker not in new_df['TICKER'].values and\
        ticker not in df['TICKER'].values:'''
    if ticker not in new_df['TICKER'].values:
        print("-"*200)
        print("ATTENTION")
        print(f"\nYOU SHOULD SELL ALL YOUR SHARES OF {ticker}!")
        print("-"*200)
        investment_amount += investments[ticker]

# Criar uma cópia explícita para evitar warnings
df_work = new_df.copy()
df_work['INVEST PRESENT'] = df_work['TICKER'].map(investments)
df_work['QTD PRESENT'] = (df_work['INVEST PRESENT'] / df_work['PRECO']).fillna(0).astype(int)

sum_ref = 0
mult = 1
while sum_ref < investment_amount - df_work['VALUE'].sum():
    df_work['QTD FUTURE'] = df_work['QTDE'] * mult
    df_work['QTD MISSING'] = df_work['QTD FUTURE'] - df_work['QTD PRESENT']
    df_work['INVEST FUTURE'] = df_work['PRECO'] * df_work['QTD MISSING']
    sum_ref = df_work['INVEST FUTURE'].sum().round(2)
    mult += 1

# Correção principal: usar .loc para atribuição
df_final = df_work[['TICKER', "QTD MISSING"]].copy()
df_final.loc[:, 'QTD MISSING'] = [val if val >= 0 else 0 for val in df_final['QTD MISSING']]

print(df_final)

print(f"\nIs estimated to be invested R${sum_ref}")
