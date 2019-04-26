from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .controllers import WalletHandler, ContractHandler, Test
from .serializers import WalletSerializer
import json

# Create your views here.


def write_response(result):
    # For Test
    return {'userId': result.user_id, 'password': result.password,
            'address': result.address, 'privateKey': result.private_key,
            'createdAt': result.created_at}


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
def transfer_token(request):
    data = json.loads(request.body)

    result = ContractHandler().transferToken(
        receiver=data['receiver'], amount=data['amount'], ca=data['contractAddress'])

    return JsonResponse({'result': True})


@api_view(['POST'])
def transfer_token_from(request):
    data = json.loads(request.body)

    result = ContractHandler().transferTokenFrom(
        sender=data['sender'], receiver=data['receiver'], amount=data['amount'], ca=data['contractAddress']
    )

    return JsonResponse({'result': result})


@api_view(['GET'])
def unlock_all(request):
    result = Test().unlockAll()
    return JsonResponse({'result': result})
