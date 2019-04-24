from .models import Wallet
from .web3 import getAccount, getBalance, sendEther, unlockAccount
import json


class WalletHandler():

    @staticmethod
    def findAddress(user_id):
        return Wallet.objects.filter(user_id=user_id).first()

    def makeWallet(self, user_id, password):
        account = getAccount(user_id)  # Web3 통해서 먼저 어드레스를 받아오고
        wallet = Wallet(user_id=user_id, password=password, address=account['address'],
                        private_key=user_id)
        wallet.save()
        return wallet

    def findWallet(self, user_id, password):
        if not user_id or not password:
            raise AssertionError

        account = Wallet.objects.filter(
            user_id=user_id, password=password).first()
        return account

    def keystore(self):
        return Wallet.objects.all()

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

        print('Sender :', sender)
        print('Sender_address: ', sender_address)
        print('Receiver: ', receiver)
        print('Receiver_address: ', receiver_address)

        val_1 = unlockAccount(sender, str(sender_address), 1000)
        val_2 = unlockAccount(receiver, str(receiver_address), 1000)

        if val_1 is False or val_2 is False:
            raise ValueError

        transaction_result = sendEther(
            sender=str(sender_address), receiver=str(receiver_address), amount=amount)

        return transaction_result


class ContractHandler():
    def deployContract(self, user_id, address):
        result = unlockAccount(user_id=user_id, address=address, duration=1000)

        return result


class TransactionHandler():
    def sendToken(self):
        return ''
