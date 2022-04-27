from brownie import KADToken
from scripts.helpful_scripts import get_accounts
from web3 import Web3


initial_supply = Web3.toWei(5000, "ether")


def deploy_kadToken():
    account = get_accounts()
    kad_token = KADToken.deploy(initial_supply, {"from": account})
    print(kad_token.name())


def main():
    deploy_kadToken()
