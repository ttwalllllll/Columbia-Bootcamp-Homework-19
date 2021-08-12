import subprocess
import json
import os
from constants import BTC, BTCTEST, ETH
from dotenv import load_dotenv
from bip_utils import Bip32, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
from bit import PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3, middleware, Account
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware
from web3.auto.gethdev import w3

load_dotenv('mnemonic.env')
mnemonic= os.getenv("mnemonic")

#print(constants.BTCTEST)
#print(mnemonic)

#Create a function called `derive_wallets`
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./hd-wallet-derive/hd-wallet-derive.php -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

numderive = 3

# Create a dictionary object called coins to store the output from `derive_wallets`.

coins = {"btc-test": derive_wallets(mnemonic, BTCTEST, numderive), "eth": derive_wallets(mnemonic, ETH, numderive)}

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, receiver, amount):
    if coin == ETH:
        gasEstimate = w3.eth.estimateGas(
            {"from":eth_acc.address, "to": to, "value": amount}
        )
        return {
            "from": eth_acc.address,
            "to": receiver,
            "value": amount,
            "gasPrice": w3.eth.gasPrice,
            "gas": gasEstimate,
            "nonce": w3.eth.getTransactionCount(eth_acc.address),
            "chainID": web3.eth.chain_id,
        }

    elif coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address,[(receiver, amount, BTC)])

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(coin, account, receiver, amount):
    txn = create_tx(coin, account, receiver, amount)
    if coin == ETH:
        signed_txn = eth_acc.sign_transaction(txn)
        result = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return result
    
    elif coin == BTCTEST:
        tx_btctest = create_tx(coin, account, receiver, amount)
        signed_txn = account.sign_transaction(txn)
        return NetworkAPI.broadcast_tx_testnet(signed_txn)
    
btc_sender = coins["btc-test"][0]['privkey']
#sending account
btc_receiver = coins["btc-test"][1]['address']  
#receiving account    



