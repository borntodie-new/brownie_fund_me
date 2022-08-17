from brownie import FundMe, MockV3Aggregator, config, network, accounts
from .helpful_scripts import get_account, deploy_mock, LOCAL_BLOCKCHAIN_ENVIRONMENTS 


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on a persistent network rinkeby, use the associated address
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        price_feed_address = MockV3Aggregator[-1].address


    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Contract deployed to {fund_me.address}")

    return fund_me



def main():
    deploy_fund_me()

