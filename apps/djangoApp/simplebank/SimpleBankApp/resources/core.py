import json
import SimpleBankApp.resources.appConfig as appConfig
import SimpleBankApp.resources.accounts as accounts
import SimpleBankApp.resources.utilities as utlts
from web3 import Web3

# Instantiating the Web3 object to communicate with the given URL
w3 = Web3(Web3.HTTPProvider(appConfig.baseurl))


###
# Deposit Ethers to the contract
###
def deposit(deposit_from_addr_index, deposit_qty):
    try:
        mycontract = w3.eth.contract(address=appConfig.contract_address, abi=appConfig.contract_abi)  # Instantiating contract object
        deposit_from_acct = accounts.import_account_from_config(deposit_from_addr_index)
        deposit_from_addr = deposit_from_acct['address']
        txn = mycontract.functions.deposit() \
            .buildTransaction({'from': deposit_from_addr,
                               'nonce': w3.eth.getTransactionCount(deposit_from_addr),
                               'gasPrice': w3.eth.gas_price,
                               'value': w3.toWei(deposit_qty, 'ether')})  # Creating a raw transaction
        print(txn)
        signed_tx = w3.eth.account.sign_transaction(txn, deposit_from_acct['privatekey'])  # Signing the raw transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()  # Sending the transaction to Blockchain
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)  # Wait for the transaction to get included in a block
        # tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
        events = mycontract.events.Deposit().processReceipt(tx_receipt)  # Get the details of the Transfer event
        return tx_receipt, events
    except Exception as ex:
        raise Exception(str(ex))


###
# Grant allowance to an account
###
def grant_allowance(grant_from_addr_index, grant_to_addr_index, grant_qty):
    try:
        mycontract = w3.eth.contract(address=appConfig.contract_address, abi=appConfig.contract_abi)  # Instantiating contract object
        grant_from_acct = accounts.import_account_from_config(grant_from_addr_index)
        grant_from_addr = grant_from_acct['address']
        grant_to_acct = accounts.import_account_from_config(grant_to_addr_index)
        grant_to_addr = grant_to_acct['address']
        txn = mycontract.functions.grantAllowance(grant_to_addr, w3.toWei(grant_qty, 'ether')) \
            .buildTransaction({'from': grant_from_addr,
                               'nonce': w3.eth.getTransactionCount(grant_from_addr),
                               'gasPrice': w3.eth.gas_price})  # Creating a raw transaction
        print(txn)
        signed_tx = w3.eth.account.sign_transaction(txn, grant_from_acct['privatekey'])  # Signing the raw transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()  # Sending the transaction to Blockchain
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)  # Wait for the transaction to get included in a block
        events = mycontract.events.Grant().processReceipt(tx_receipt)  # Get the details of the Transfer event
        return tx_receipt, events
    except Exception as ex:
        raise Exception(str(ex))


###
# Withdraw Ethers from contract
###
def withdraw(withdraw_addr_index, withdraw_qty):
    try:
        mycontract = w3.eth.contract(address=appConfig.contract_address, abi=appConfig.contract_abi)  # Instantiating contract object
        withdraw_acct = accounts.import_account_from_config(withdraw_addr_index)
        withdraw_addr = withdraw_acct['address']
        txn = mycontract.functions.withdraw(w3.toWei(withdraw_qty, 'ether')) \
            .buildTransaction({'from': withdraw_addr,
                               'nonce': w3.eth.getTransactionCount(withdraw_addr),
                               'gasPrice': w3.eth.gas_price})  # Creating a raw transaction
        print(txn)
        signed_tx = w3.eth.account.sign_transaction(txn, withdraw_acct['privatekey'])  # Signing the raw transaction
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction).hex()  # Sending the transaction to Blockchain
        tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)  # Wait for the transaction to get included in a block
        events = mycontract.events.Grant().processReceipt(tx_receipt)  # Get the details of the Transfer event
        return tx_receipt, events
    except Exception as ex:
        print(ex)
        raise Exception(str(ex))


###
# Get the balance of the specified token for the given address
###
def get_allowance(_target_account_index):
    mycontract = w3.eth.contract(address=appConfig.contract_address, abi=appConfig.contract_abi)  # Instantiating contract object
    target_account = accounts.import_account_from_config(_target_account_index)
    _allowance = mycontract.functions.allowance().call({'from': target_account['address']})  # Check the balance of tokens for the specified address
    _allowance = w3.fromWei(_allowance, 'ether')
    return _allowance


###
# Get ether balance for the given address
###
def get_ether_balance(_address):
    balance = w3.eth.get_balance(_address)
    balance = Web3.fromWei(balance, 'ether')
    return balance


###
# Get ether balances for the given addresses
###
def get_ether_balances(_addresses):
    balances = []
    for address in _addresses:
        balance = get_ether_balance(address)
        balances.append(balance)
    return balances
