
import time
from rest_api.functions import rest_api_account

class MyCount:


    def __init__(self, client):
        self.client = client
        self.info = rest_api_account.get_account(client=self.client, omit_zero_balances=True)['data']
        self.symbol = 'BTCUSDT'
        self.end_time = int(time.time() * 1_000)
        self.start_time = self.end_time - (30 * 24 * 60 * 60 * 1_000)
        self.tax = self.calculate_taxes()


    def calculate_taxes(self) -> float:
        '''
        Calculate taxes rate for each order
        '''
        comission_data = rest_api_account.account_comission(client=self.client, symbol=self.symbol)['data']
        # calculate taxes
        taxes = eval(comission_data.standard_commission.taker) + eval(comission_data.special_commission.taker) + eval(comission_data.tax_commission.taker)
        # calculate discount
        discount_taxes = comission_data.discount.discount if (self.check_coin_in_account(coin=comission_data.discount.discount_asset) and comission_data.discount.enabled_for_account) else 0
        return taxes * (1-discount_taxes)
        

    def check_coin_in_account(self, coin: str) -> bool:
        '''
        Check if the coin is in account.
        '''
        balances = self.info.balances
        bnb_balance = next((balance for balance in balances if coin.lower() in balance.asset.lower()), None)
        return True if eval(bnb_balance.free) > .1 else False


