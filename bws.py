from web3 import Web3

rpc = "https://base-rpc.publicnode.com"
w3 = Web3(Web3.HTTPProvider(rpc))

private_key = input("Private key: ")
to = input("Send to: ")
amount = float(input("Amount ETH: "))

account = w3.eth.account.from_key(private_key)
nonce = w3.eth.get_transaction_count(account.address)

tx = {
    'nonce': nonce,
    'to': to,
    'value': w3.to_wei(amount, 'ether'),
    'gas': 21000,
    'gasPrice': w3.to_wei('1', 'gwei'),
    'chainId': 8453
}

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print("TX HASH:", w3.to_hex(tx_hash))