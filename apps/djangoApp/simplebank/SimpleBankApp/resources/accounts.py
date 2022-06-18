
import web3
import SimpleBankApp.resources.appConfig as appConfig


# Import the account details for the specified account index. Account index is not related to Blockchain
def import_account_from_config(account_index):
    privkey = '0x' + appConfig.user_accounts[account_index]['privatekey']
    role = appConfig.user_accounts[account_index]['role']
    new_account = web3.eth.Account.privateKeyToAccount(privkey)
    return {'index': account_index, 'address': new_account.address,
            'privatekey': new_account.privateKey.hex(), 'role': role}


###
# Get the information of all user accounts used by the mock application
###
def get_all_accounts():
    accounts_all = []
    for i in range(0, len(appConfig.user_accounts)):
        acct = import_account_from_config(i)
        accounts_all.append(acct)
    return accounts_all
