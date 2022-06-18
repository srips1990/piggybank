
# URL of the Blockchain node to communicate with
import json
import os

baseurl = "http://localhost:8545"

# The ABI of the smart contract
contract_abi_file_name = 'abi.json'
contract_abi_file_path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
contract_abi = json.load(open(os.path.join(contract_abi_file_path,contract_abi_file_name), 'r', encoding='utf8'))

# Address of the smart contract which stores the information of all tokens deployed through the application
contract_address = "0x344A718a55c6C7964E5e4d617091a806261DD9Ce"		# Ganache

# List of private keys for the user accounts used by the application
user_accounts = [{'privatekey': '5eecb0e4be108806275be20cd3610f64faa99d763d13dd5db1f3f1d5067847bb', 'role': 'father'},
                 {'privatekey': 'de3e68b553d2baf22f7c6a3f97f12ef509065e7f96448e5dadcfcab361489586', 'role': 'child'}]
