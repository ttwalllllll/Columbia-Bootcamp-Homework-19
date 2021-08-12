# Homework_19


## 1. Project Setup

Use the HD-Wallet-Derive function to create addresses from passphrase generated online.

I used an .ipynb to test some function but all code is run through "wallet.py"

## 2. Constant Setup

Variables for coins stored in "constants.py".

## 3. Generate a Mnemonic

Mnemonic located in mnemonic.env.

## 4. Derive the wallet keys


## 5. Linking the transaction signing libraries

Created functions to create transactions and send transactions. Code below:

## 6. Send some transactions

Screenshots below confirming sent and received BTCTEST. Sending account was funded via a faucet (screenshot below):

## 7. Description of Wallet

Created a wallet that holds the addresses to test ETH, & BTCTEST. Each coin has 3 children address that we can send and receive crpytp to/from. Addresses were derived using PHP code.

Functions were created to capture addresses, public key, & private keys.

Functions were then created to turn private key into an object.

Finally, functions were created for "create_tx" & "send_tx". "Create_tx" is used to create an unsigned transaction. "Send_tx" calls on "create_tx" and signs the transaction.

I was able to send and receive test funds through the terminal and via the "wallet.ipynb".