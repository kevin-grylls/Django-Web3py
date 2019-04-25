from web3 import Web3, HTTPProvider, IPCProvider
from .contracts import get_abi, get_bin

w3 = Web3(HTTPProvider('http://192.168.0.27:8545'))
w3.eth.enable_unaudited_features()

ca_for_test = '0x02a56b13256c4899775dfe54ed5da9bd1a066948'


def deployContract(address):
    """
    컨트랙트를 디플로이하고 CA를 반환합니다.
    """

    w3.eth.defaultAccount = address

    Contract = w3.eth.contract(abi=get_abi(), bytecode=get_bin()['object'])
    tx_hash = Contract.constructor().transact()
    tx_receipt = w3.eth.waitForTransactionReceipt(str(tx_hash.hex()))

    print('Contract: ', Contract)
    print('tx_hash: ', tx_hash.hex())
    print('CA: ', tx_receipt['contractAddress'])

    return tx_receipt['contractAddress']


def checksumAddress(address):

    return w3.toChecksumAddress(address)


def getContract(address):
    """
    배포된 컨트랙트를 반환합니다.
    """
    return w3.eth.contract(address=checksumAddress(address), abi=get_abi())


def getWeb3():
    """
    Web3 인스턴스 반환
    """
    return w3


def getAccount(user_id):
    """
    사용자의 지갑 정보를 반환
    """

    address = w3.personal.newAccount(user_id)
    return {'address': address, 'private_key': user_id}


def unlockAccount(user_id, address, duration):
    """
    트랜잭션 수행 전 계정을 언락상태로 설정하고 결과 값을 리턴합니다.
    """
    result = w3.personal.unlockAccount(address, user_id, duration)
    print('Unlock Result: ', result)
    return result


def getBalance(address):
    """
    이더 잔액을 조회합니다.
    """
    balance = w3.fromWei(w3.eth.getBalance(address), 'ether')
    return balance


def sendEther(sender, receiver, amount):
    """
    이더를 전송합니다.
    """
    wai_amount = w3.toWei(str(amount), 'ether')  # wei 변환
    result = w3.eth.sendTransaction(
        {'to': receiver, 'from': sender, 'value': wai_amount})
    return result
