from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .controllers import WalletHandler, ContractHandler, TransactionHandler, Test
from .serializers import WalletSerializer, TransactionSerializer
import json

# Create your views here.


def write_response(result):
    # For Test
    return {'userId': result.user_id, 'password': result.password,
            'address': result.address, 'privateKey': result.private_key,
            'createdAt': result.created_at}


def write_block_response(result):
    return {
        'blockHash': result['blockHash'].hex(),
        'blockNumber': result['blockNumber'],
        'gas': result['gas'],
        'gasPrice': result['gasPrice'],
        'hash': result['hash'].hex(),
        'input': result['input'],
        'nonce': result['nonce'],
        'transactionIndex': result['transactionIndex'],
        'from': result['from'],
        'to': result['to'],
        'value': result['value'],
        'v': result['v'],
        'r': result['r'].hex(),
        's': result['s'].hex()
    }


class WalletList(generics.ListCreateAPIView):
    queryset = WalletHandler().keystore()
    serializer_class = WalletSerializer


@api_view(['POST'])
def create(request):
    # 프론트 JS = camelCase / 백엔드 PY = snake_case
    data = json.loads(request.body)

    result = WalletHandler().makeWallet(
        user_id=data['userId'], password=data['password'])

    response = write_response(result)
    return JsonResponse(response)


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)

    result = WalletHandler().findWallet(
        user_id=data['userId'], password=data['password'])

    response = write_response(result)
    return JsonResponse(response)


@api_view(['GET'])
def balance(request, user_id):
    result = WalletHandler().getRest(user_id=user_id)
    return JsonResponse({'userId': user_id, 'balance': result})


@api_view(['POST'])
def transfer_ether(request):
    data = json.loads(request.body)

    result = WalletHandler().transferEther(
        sender=data['sender'], receiver=data['receiver'], amount=data['amount'])
    print(result)

    return JsonResponse({'result ': 'ok'})


@api_view(['POST'])
def deploy(request):
    data = json.loads(request.body)

    result = ContractHandler().initContract(
        user_id=data['userId'], address=data['address'])

    return JsonResponse({'contractAddress': str(result.address), 'createdAt': str(result.created_at)})


@api_view(['GET'])
def all_functions(request):
    data = request.query_params
    result = ContractHandler().getAllFunctions(ca=data['ca'])
    return JsonResponse({'result': result})


@api_view(['GET'])
def total_supply(request):
    data = request.query_params
    result = ContractHandler().totalSupply(ca=data['ca'])

    return JsonResponse({'result': result})


@api_view(['POST'])
def balance_of(request):
    data = json.loads(request.body)

    result = ContractHandler().balanceOf(
        data['userId'], address=data['address'], ca=data['contractAddress'])

    return JsonResponse({'result': result})


@api_view(['POST'])
def balance_of_all(request):
    data = json.loads(request.body)
    result = ContractHandler().balanceOfAll(
        ca=data['contractAddress'])
    return JsonResponse({'result': result})


@api_view(['POST'])
def transfer_token(request):
    data = json.loads(request.body)

    result = ContractHandler().transferToken(
        receiver=data['receiver'], amount=data['amount'], ca=data['contractAddress'])

    # print('Transfer Result: ', result)
    # print('ca: ', data['contractAddress'])
    # print('origin: ', result['from'])
    # print('dest: ', data['receiver'])
    # print('amount: ', data['amount'])
    # print('tx_hash: ', result['transactionHash'].hex())
    # print('block: ', int(result['blockNumber']))
    # print('gas used: ', result['gasUsed'])

    transaction = TransactionHandler().saveTransaction(ca=data['contractAddress'], origin=result['from'], dest=data['receiver']['address'], amount=float(
        data['amount']), gas_used=int(result['gasUsed']), tx_hash=result['transactionHash'].hex(),    block=int(result['blockNumber']))

    return JsonResponse({'blockNumber': result['blockNumber'],
                         'from': result['from'], 'gasUsed': result['gasUsed']})


@api_view(['POST'])
def transfer_token_from(request):
    data = json.loads(request.body)

    result = ContractHandler().transferTokenFromTo(
        sender=data['sender'], receiver=data['receiver'], amount=data['amount'], ca=data['contractAddress']
    )

    transaction = TransactionHandler().saveTransaction(ca=data['contractAddress'], origin=result['from'], dest=data['receiver']['address'], amount=float(
        data['amount']), gas_used=int(result['gasUsed']), tx_hash=result['transactionHash'].hex(),    block=int(result['blockNumber']))

    return JsonResponse({'blockNumber': result['blockNumber'],
                         'from': result['from'], 'gasUsed': result['gasUsed']})


class TransactionList(generics.ListCreateAPIView):
    queryset = TransactionHandler().getTransactionAll()
    serializer_class = TransactionSerializer


@api_view(['GET'])
def get_transaction_all(request):
    result = TransactionHandler().getTransactionFromDB()
    return JsonResponse({'result': result})


@api_view(['POST'])
def get_transaction_of(request):
    data = json.loads(request.body)
    result = TransactionHandler().getTransactionFromEVM(data['txHash'])
    response = write_block_response(result)
    return JsonResponse({'result': response})


@api_view(['GET'])
def get_latest_block(request):
    result = TransactionHandler().getLatestBlock()
    print(result)
    return JsonResponse({'result': 'ok'})


@api_view(['GET'])
def unlock_all(request):
    result = Test().unlockAll()
    return JsonResponse({'result': result})


@api_view(['GET'])
def get_coinbase(request):
    result = Test().getCoinbase()
    return JsonResponse({'result': str(result)})


@api_view(['GET'])
def status_miner(request):
    result = Test().statusMining()
    return JsonResponse({'result': result})


@api_view(['POST'])
def set_miner(request):
    data = json.loads(request.body)
    result = Test().setMiner(data['status'])
    print(result)
    return JsonResponse({'result': result})
