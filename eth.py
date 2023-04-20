from web3 import Web3
from eth_account import Account
import os

# Підключенні до мережі
web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

def create_account():
    account = Account.create()
    return {"address": account.address, "private_key": account.key.hex()}

def load_account(private_key):
    account = Account.from_key(private_key)
    return {"address": account.address, "private_key": account.key.hex()}

def get_balance(address):
    balance = web3.eth.get_balance(address)
    return web3.from_wei(balance, "ether")

def send_transaction(sender_private_key, recipient_address, amount):
    sender_address = Account.from_key(sender_private_key)
    nonce = web3.eth.get_transaction_count(sender_address.address)
    tx = {
        "nonce": nonce,
        "to": recipient_address,
        "value": web3.to_wei(amount, "ether"),
        "gas": 2000000,
        "gasPrice": web3.to_wei("50", "gwei")
    }
    signed_tx = web3.eth.account.sign_transaction(tx, sender_private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return tx_hash.hex()
