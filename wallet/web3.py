from web3 import Web3, HTTPProvider, IPCProvider
import os

# Web3 Handler 따로 구현해서 메소드만 호출하는 방식

w3 = Web3(HTTPProvider('http://localhost:7545'))
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
    tranfer_amount = w3.toWei(str(amount), 'ether')  # wei 변환
    result = w3.eth.sendTransaction(
        {'to': receiver, 'from': sender, 'value': tranfer_amount})

    return result


def deployContract():
    return ''
