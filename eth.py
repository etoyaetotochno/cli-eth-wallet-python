from web3 import Web3
from eth_account import Account
import os

# Підключенні до мережі
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

def create_account():
    account = Account.create()
    return {"address": account.address, "private_key": account.key.hex()}

