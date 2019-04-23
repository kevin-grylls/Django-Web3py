from .models import Wallet
from .web3 import getAccount, getBalance, sendEther
import json


class WalletHandler():

    @staticmethod
    def findAddress(user_id):
        return Wallet.objects.filter(user_id=user_id).first()

    def makeWallet(self, user_id, password):
        account = getAccount()  # Web3 통해서 먼저 어드레스를 받아오고
        wallet = Wallet(user_id=user_id, password=password, address=account.address,
                        private_key=account.privateKey.hex())
        wallet.save()   # 개인, 월렛정보 추합 후 저장
        return wallet

    def keystore(self):
        return Wallet.objects.all()

    def findWallet(self, user_id, password):
        if not user_id or not password:
            raise AssertionError

        account = Wallet.objects.filter(
            user_id=user_id, password=password).first()
        return account

    def getRest(self, user_id):
        if not user_id:
            raise AssertionError

        account = self.findAddress(user_id=user_id)
        return getBalance(address=account.address)

    def transferEther(self, sender, receiver, amount):
        if not sender or not receiver or not amount:
            raise ValueError

        sender_address = self.findAddress(sender)
        receiver_address = self.findAddress(receiver)

        transaction_result = sendEther(
            '0x743A82902b6C9bE5e11175a8816f01F2532404e9', '0x28c8AfFf625F4bac2A3cE214224DBC6044b37F82', amount)

        return transaction_result


class ContractHandler():
    def deployContract(self):
        return ''


class TransactionHandler():
    def sendToken(self):
        return ''
