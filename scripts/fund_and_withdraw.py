from brownie import config, network, FundMe
from .helpful_scripts import get_account

def fund():
    account = get_account()
    fund_me = FundMe[-1]
    entrence_fee = fund_me.getEntranceFee()
    print(f"The current entry fee is {entrence_fee}")
    print("Funding...")
    # print(entrence_fee)
    fund_me.fund({'from': account, 'value': entrence_fee})

def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print(f"The current balance is {account.balance()}")
    print('withdraw...')
    fund_me.withdraw({"from": account})
    print('withdrawed...')
    print(f"The current balance is {account.balance()}")

def main():
    fund()
    withdraw()