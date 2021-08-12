# Homework_19


## 1. Project Setup

Use the HD-Wallet-Derive function to create addresses from passphrase generated online.

I used an .ipynb to test some function but all code is run through "wallet.py"

## 2. Constant Setup

Variables for coins stored in "constants.py".

## 3. Generate a Mnemonic

Mnemonic located in mnemonic.env.

## 4. Derive the wallet keys
<img width="823" alt="Derived Addresses" src="https://user-images.githubusercontent.com/8030533/129248517-99e31136-1f3d-42fe-9595-17075b748d51.png">
<img width="1053" alt="Derivation Function" src="https://user-images.githubusercontent.com/8030533/129248535-270053b5-88ed-4f8f-9875-12e34e99c8c0.png">

## 5. Linking the transaction signing libraries

Created functions to create transactions and send transactions. Code below:
<img width="837" alt="Transaction Code" src="https://user-images.githubusercontent.com/8030533/129248721-b33b1009-b297-4f41-ba4f-31c327aaebee.png">

## 6. Send some transactions

Screenshots below confirming sent and received BTCTEST. Sending account was funded via a faucet (screenshot below):
![Faucet Drop](https://user-images.githubusercontent.com/8030533/129248835-dfef10e1-ca35-4e93-85b1-bf4e2a521474.png)
<img width="1320" alt="Received BTCTEST" src="https://user-images.githubusercontent.com/8030533/129248782-13310c7f-fc90-46aa-a1d4-5b03c007b236.png">
<img width="1324" alt="Sent BTCTEST" src="https://user-images.githubusercontent.com/8030533/129248860-9a2a19ac-98bd-4957-b4a4-857730083955.png">
<img width="1087" alt="Terminal Transaction" src="https://user-images.githubusercontent.com/8030533/129248881-ebd7abc4-24f4-4a20-9d2f-b8aa6167bb33.png">

## 7. Description of Wallet

Created a wallet that holds the addresses to test ETH, & BTCTEST. Each coin has 3 children address that we can send and receive crpytp to/from. Addresses were derived using PHP code.

Functions were created to capture addresses, public key, & private keys.

Functions were then created to turn private key into an object.

Finally, functions were created for "create_tx" & "send_tx". "Create_tx" is used to create an unsigned transaction. "Send_tx" calls on "create_tx" and signs the transaction.

I was able to send and receive test funds through the terminal and via the "wallet.ipynb".
