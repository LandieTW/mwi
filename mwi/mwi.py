# Método Wanderley de Investimentos (MWI)

"""
This is an auto-searching script for evaluating stock investiments in Brazilian companies
on the stock market, using data from the Status Invest website and referencing.
Find below the criterion used int the analysis:
- Margens > 10%
- Rentabilidade > 10%
- Dívida/EBITDA < 2
- Liquidez > 1M
- Graham/Preço > 10%

Remember to download the webdriver from the link below
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
Then, unpack it in the same directory of this script
Also you need to have installed a compatible version of the web browser Edge

Pip install the libs below
- selenium
- webdriver-manager
- glob
- pandas
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

# True if you want to download it
download_csv = False

_this_path = os.path.dirname(os.path.abspath(__file__))

if download_csv:
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    service = Service(os.path.join(_this_path, "msedgedriver.exe"))
    driver = webdriver.Edge(service=service, options=edge_options)

    try:
        driver.get("https://statusinvest.com.br/acoes/busca-avancada")
        wait = WebDriverWait(driver, 15)

        search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[3]/div/div/div/button[2]')))
        search_button.click()
        time.sleep(2)

        download_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-2"]/div[4]/div/div[1]/div[2]/a/i')))
        download_button.click()
        time.sleep(2)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()

    old_csv_path = glob.glob(os.path.join(os.path.expanduser("~/Downloads"), "*statusinvest*.csv"))[0]
    new_csv_path = glob.glob(os.path.join(_this_path, "*statusinvest*.csv"))[0]
    shutil.move(old_csv_path, new_csv_path)
else:
    new_csv_path = glob.glob(os.path.join(_this_path, "*statusinvest*.csv"))[0]

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

df = df[df['MARGEM BRUTA'] > 10]
df = df[df['MARGEM EBIT'] > 10]
df = df[df['MARG LIQUIDA'] > 10]
df = df[df['DIVIDA LIQUIDA / EBIT'] < 2]
df = df[df['DIV LIQ / PATRI'] < 2]
df = df[df['ROE'] > 10]
df = df[df['ROA'] > 10]
df = df[df['ROIC'] > 10]
df = df[df['LIQUIDEZ MEDIA DIARIA'] > 10**5]

df = df.reset_index(
    drop=True,
    inplace=False
)

df['GRAHAM'] = round((1.5 * df['VPA'] * 15 * df['LPA']) ** (1/2), 2)
df['GRAHAM / PRECO'] = df['GRAHAM'] / df['PRECO']
df['OPORTUNIDADE'] = df['GRAHAM / PRECO'] > 1.1

ref_price_idx = df[df['OPORTUNIDADE']]['PRECO'].idxmax()
ref_price = df[ref_price_idx:ref_price_idx + 1]['PRECO'].values[0]

df['QTDE'] = np.where(
    df['OPORTUNIDADE'],
    (ref_price / df['PRECO']).astype(int),
    0
)
df['SHARE'] = round((df['QTDE'] * df['PRECO']) / (df['QTDE'] * df['PRECO']).sum(), 2) * 100
df['VALUE'] = df['PRECO'] * df['QTDE']
total_investment = round(df['VALUE'].sum(), 2)

print("-"*200)
print(f"This script selected the tickers below as good investments")
print("-"*200)
print(df)

print("-"*200)
print(f"And these are the best options to buy")
print(f"Total investment: R$ {total_investment}")
print("-"*200)

print(df[df['OPORTUNIDADE']].reset_index(drop=True, inplace=False))
