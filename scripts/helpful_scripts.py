from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3


DECIMAL = 8
STARTING_PRICE = 200000000000

FORKED_LOCAL_ENVIRONMENTS = ('mainnet-fork-dev', 'mainnet-fork')
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ('development', 'ganache-local')

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        # MockV3Aggregator.deploy(DECIMAL, Web3.toWei(STARTING_PRICE, "ether"), {"from": get_account()})
        MockV3Aggregator.deploy(DECIMAL, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
