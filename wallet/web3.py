from web3 import Web3, HTTPProvider, IPCProvider
import os


w3 = Web3(HTTPProvider('http://192.168.0.27:7545'))
w3.eth.enable_unaudited_features()


def getSalt():
    return os.urandom(16)


def getWeb3():
    return w3


def getAccount():
    address = w3.eth.account.create(getSalt())
    return address


def getBalance(address):
    balance = w3.fromWei(w3.eth.getBalance(address), 'ether')
    return balance


def sendEther(sender, receiver, amount):
    wai_amount = w3.toWei(str(amount), 'ether')  # wei 변환
    result = w3.eth.sendTransaction(
        {'to': receiver, 'from': sender, 'value': wai_amount})
    return result


def deployContract():
    return ''
