from web3 import Web3, HTTPProvider, IPCProvider
from .contracts import get_abi, get_bin

w3 = Web3(HTTPProvider('http://192.168.0.27:8545'))
# w3 = Web3(HTTPProvider('http://localhost:7545'))
w3.eth.enable_unaudited_features()


def deployContract(address):
    """
    컨트랙트를 디플로이하고 CA를 반환합니다.
    """

    w3.eth.defaultAccount = address

    Contract = w3.eth.contract(abi=get_abi(), bytecode=get_bin()['object'])
    tx_hash = Contract.constructor().transact()
    print('tx_hash: ', tx_hash.hex())

    tx_receipt = w3.eth.waitForTransactionReceipt(str(tx_hash.hex()))
    return tx_receipt


def checksumAddress(address):

    return w3.toChecksumAddress(address)


def setDefaultAccount(address):
    w3.eth.defaultAccount = checksumAddress(address)
    return True


def statusMining():
    return w3.eth.mining


def setMining(status):
    if status is True:
        w3.miner.start(1)
        return True
    else:
        w3.miner.stop()
        return False


def getContract(address):
    """
    배포된 컨트랙트를 반환합니다.
    """
    return w3.eth.contract(address=checksumAddress(address), abi=get_abi())


def getTransactionReceipt(tx_hash):
    """
    작업 중인 블록넘버를 제외하고 트랜잭션 결과를 반환합니다.
    waitForTransactionReceipt() 보다 빠릅니다.
    """
    return w3.eth.getTransaction(tx_hash)


def waitForTransactionReceipt(tx_hash):
    """
    작업 중인 블록넘버까지 포함합니다.
    getTransactionReceipt() 보다 느립니다.
    """
    return w3.eth.waitForTransactionReceipt(tx_hash)


def getWeb3():
    """
    Web3 인스턴스 반환
    """
    return w3


def getCoinbase():
    return w3.eth.coinbase


def getAccount(user_id):
    """
    사용자의 지갑 정보를 반환
    """

    address = w3.personal.newAccount(user_id)
    return {'address': address, 'private_key': user_id}


def unlockAccount(user_id, address, duration):
    """
    계정을 언락상태로 설정하고 실행 결과를 리턴합니다.
    """
    result = w3.personal.unlockAccount(
        checksumAddress(address), user_id, duration)
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
