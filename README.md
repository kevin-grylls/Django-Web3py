##### WEB3.py API Server

###### Preparation before you go

---

- DB: PostgreSQL -> localhost:5432
- Web3: Web3.py -> EVM 테스트넷 기준으로 개발되었습니다.
- Contract: root/contracts/\* -> Solidity, ABI, Bytecode File

---

- CLI

```sh
$ pip install -r requirements.txt  // 가상환경 설치
$ python3 manage.py makemigrations // 마이그레이션 설정 파일 생성
$ python3 manage.py migrate        // 마이그레이션 (모델 기반 스키마 생성)
$ python3 manage.py runserver      // 테스트 서버 기동

```

---

- 테스트 절차
  - RPC 활성화된 Ethereum Node, PostgreSQL 을 기동해 주세요.
  - 커넥션 설정은 app/wallet/web3.py && app/settings.py 에서 작성합니다.
  - 스마트 컨트랙트는 app/contracts 디렉토리에서 확인 가능합니다.
  - 현 시점으로 회원가입, 정보조회, 스마트 컨트랙트 배포, 토큰 할당, 토큰 전송, 잔액 조회 API를 제공합니다.

---

- 1. 지갑 생성 (POST)
- http://localhost:8000/wallet/create/

```json
# Sample Request
{
  "userId": "kevin",
  "password": "1004"
}
```

- 2. 로그인 (POST)
- http://localhost:8000/wallet/login/

```json
# Sample Request
{
  "userId": "kevin",
  "password": "1004"
}
```
```json
# Sample Response
{
  "userId": "kevin",
  "password": "1004",
  "address": "0x9b69441c0b638f66C1f88411BD37f0D67C9975C5",
  "privateKey": "kevin",
  "createdAt": "2019-04-26T02:12:03.383Z"
}
```

- 3. 스마트 컨트랙트 배포 (POST)
- http://localhost:8000/wallet/deploy/
- 배포 계정이 Coinbase 설정 되어있고, EVM 채굴 상태이어야 합니다.

```json
# Sample Request
{
  "userId": "kevin",
  "address": "0x9b69441c0b638f66C1f88411BD37f0D67C9975C5"
}
```
```json
# Sample Response
{
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109",
  "createdAt": "2019-04-26 03:07:26.843151+00:00"
}
```

- 4. 토큰 에어 드랍 (POST)
- http://localhost:8000/wallet/transfer_token/
- 토큰 홀더만 API 실행 가능합니다.

```json
# Sample Request
{
  "receiver": {
    "userId": "ellie",
    "address": "0x3d2a0F636b3E95B9f15Ce8d0c57366e62D5514b8"
  },
  "amount": 100,
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109"
}
```
```json
# Sample Response
{
  "blockNumber": 8081,
  "from": "0xae628b2698d1f213d461307b139f255d01febafb",
  "gasUsed": 36158
}
```

- 5. 참여자간 토큰 전송 (POST)
- http://localhost:8000/wallet/transfer_token_from/
- 수신자와 송신자, 수량과 CA 정보로 API 호출합니다.

```json
# Sample Request
{
  "sender": {
    "userId": "irene",
    "address": "0x600aAD4C0089cb7b927ffff535779420237EBba5"
  },
  "receiver": {
    "userId": "ivy",
    "address": "0x9Cda9C301b07D4A2B03bfA945800501502f97F67"
  },
  "amount": 100,
  "contractAddress": "0xA4753bA6DDb8C86b205f228ddfE63a95803d888b"
}
```
```json
# Sample Response
{
  "blockNumber": 8304,
  "from": "0xae628b2698d1f213d461307b139f255d01febafb",
  "gasUsed": 37408
}
```

- 6. 계정의 토큰 잔고 확인 (POST)
- http://localhost:8000/wallet/balance_of/

```json
# Sample Request
{
  "userId": "irene",
  "address": "0x62Cf333dB24179824ddD7036ea9De7771C875A36",
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109"
}
```
```json
# Sample Response
{
  "result": 5200
}
```

- 7. 스마트 컨트랙트 모든 계정의 잔고 확인 (POST)
- http://localhost:8000/wallet/balance_of_all/

```json
# Sample Request
{
	"contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D"
}
```
```json
# Sample Response
{
    "result": [
        {
            "userId": "kevin",
            "balance": 2000
        },
        {
            "userId": "sunny",
            "balance": 2500
        },
        {
            "userId": "irene",
            "balance": 1000
        },
        {
            "userId": "jeanie",
            "balance": 1000
        },
        {
            "userId": "angelica",
            "balance": 1000
        },
        {
            "userId": "roy",
            "balance": 1500
        },
        {
            "userId": "mark",
            "balance": 1000
        }
    ]
}
```

- 8. 코인베이스 계정 확인 (GET)
- http://localhost:8000/wallet/get_coinbase/

```json
# Sample Response
{
    "result": "0x5fc1b8f93cF4a6Aa3b35a928882Fda0296bd07F7"
}
```

- 9. 채굴 상태 확인 (GET)
- http://localhost:8000/wallet/status_miner/

```json
# Sample Response
{
    "result": true
}
```

- 10. 채굴 On / Off (POST)
- http://localhost:8000/wallet/set_miner/

```json
# Sample Request
{
	"status": true
}
```

```json
# Sample Response 
{
  "result": true
}
```

- 11. 모든 트랜잭션 확인 (GET)
- http://localhost:8000/wallet/get_transaction_all/

```json
# Sample Response
{
    "result": [
        {
            "contractAddress": "0x4448541739677099A84A24888eb0d9ad7f2fEc0e",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x24d8c6df24F27159C29CF7C314A5AE44C1952Db4",
            "amount": 100,
            "gasUsed": 36222,
            "blockNumber": 3894,
            "txHash": "0xcaba7134244770e4c967b48d095e50c565efeba727be2708ac53420839ae1fa3",
            "createdAt": "2019-04-29T14:27:56.386Z"
        },
        {
            "contractAddress": "0x4448541739677099A84A24888eb0d9ad7f2fEc0e",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0xdFE96eA2100648025bf9A748a1Ead28734357201",
            "amount": 100,
            "gasUsed": 36222,
            "blockNumber": 3895,
            "txHash": "0x1d9bb207386e9196ad6c1d5a15e45f2c5c7d40ded28dbdd94764ca45f5cea95f",
            "createdAt": "2019-04-29T14:28:56.041Z"
        },
        {
            "contractAddress": "0x4448541739677099A84A24888eb0d9ad7f2fEc0e",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x8889D2eE6b47984c16C24d755000fc9cF562DbF1",
            "amount": 100,
            "gasUsed": 36158,
            "blockNumber": 3899,
            "txHash": "0x7cdf4637874fe06d16166d97a610e20124818a150c8a7d625df9f292ea0b3c19",
            "createdAt": "2019-04-29T14:29:18.026Z"
        },
        {
            "contractAddress": "0x4448541739677099A84A24888eb0d9ad7f2fEc0e",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x5fc1b8f93cF4a6Aa3b35a928882Fda0296bd07F7",
            "amount": 1000,
            "gasUsed": 37600,
            "blockNumber": 4223,
            "txHash": "0x8f9eeeaa706e8a5da347503475f92876093f5e070e67dcc667a641f201400aa1",
            "createdAt": "2019-04-29T15:30:02.467Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x8889D2eE6b47984c16C24d755000fc9cF562DbF1",
            "amount": 1000,
            "gasUsed": 51222,
            "blockNumber": 5414,
            "txHash": "0x4bb7b28de7093ce685c5f630bab36393089a0e57fcfc6f2d2f2cbe3d32bcd701",
            "createdAt": "2019-04-30T02:31:02.641Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0xdFE96eA2100648025bf9A748a1Ead28734357201",
            "amount": 1000,
            "gasUsed": 51286,
            "blockNumber": 5416,
            "txHash": "0x003af556d6331669fb93bf787dec4113bd391d30f67e456e9e309195fa7da24b",
            "createdAt": "2019-04-30T02:31:16.345Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x24d8c6df24F27159C29CF7C314A5AE44C1952Db4",
            "amount": 1000,
            "gasUsed": 51286,
            "blockNumber": 5420,
            "txHash": "0x6b53f499c93c9925477473dfe5195d2ade059f9ab31f27a120c8cbd54c9cdfb4",
            "createdAt": "2019-04-30T02:32:31.504Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x66D93a3B1d024E86bef3dd8E17e9644F41ef0252",
            "amount": 1000,
            "gasUsed": 51286,
            "blockNumber": 5421,
            "txHash": "0x2f8f6cf54a210dc85e69785b427d4f8dc59cec8a08229ef55d7a27158c876815",
            "createdAt": "2019-04-30T02:32:43.835Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0xe21751aCa387b7d66Fc8F1873DC16Eb243cA1e5A",
            "amount": 1000,
            "gasUsed": 51286,
            "blockNumber": 5422,
            "txHash": "0xdf37ddc8587e8f5c96d12e0cde83ec289ad08a85c22a1fcdab171b8e28d9ce5d",
            "createdAt": "2019-04-30T02:33:06.746Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x0137dFea2CdF3A1C7fd25FfE95E99eAd3dC5cAac",
            "amount": 1000,
            "gasUsed": 51286,
            "blockNumber": 5423,
            "txHash": "0xdb2746f9fc3907cf37e71e65851f099ccb04a2cd73de358225c29484926d4b6a",
            "createdAt": "2019-04-30T02:33:19.064Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0xe21751aCa387b7d66Fc8F1873DC16Eb243cA1e5A",
            "amount": 2000,
            "gasUsed": 36286,
            "blockNumber": 5424,
            "txHash": "0x99ae413a4ce89b7899f218dbe9a1ad939d2d7b000e1bd69f2bed556aa4788553",
            "createdAt": "2019-04-30T02:34:20.698Z"
        },
        {
            "contractAddress": "0x74a65E4E1a5418ef09C6b36689980c830E781e0D",
            "origin": "0x5fc1b8f93cf4a6aa3b35a928882fda0296bd07f7",
            "destination": "0x8889D2eE6b47984c16C24d755000fc9cF562DbF1",
            "amount": 1500,
            "gasUsed": 37536,
            "blockNumber": 5427,
            "txHash": "0x02a05a6fd5c0d71f92e2e4d38aadc9a1e66bc70171ddc629ab51574eeb9ebb2b",
            "createdAt": "2019-04-30T02:34:47.071Z"
        }
    ]
}
```

- 12. 트랜잭션 확인 (POST)
- http://localhost:8000/wallet/get_transfer_of/

```json
# Sample Request
{
	"txHash": "0xcaba7134244770e4c967b48d095e50c565efeba727be2708ac53420839ae1fa3"
}
```
```json
# Sample Response
{
    "result": {
        "blockHash": "0x2fb59c951a9cafb0d93a2a7b879efef2c6ef36be91db74efaaf1607d87caed36",
        "blockNumber": 3894,
        "gas": 136222,
        "gasPrice": 1000000000,
        "hash": "0xcaba7134244770e4c967b48d095e50c565efeba727be2708ac53420839ae1fa3",
        "input": "0xa9059cbb00000000000000000000000024d8c6df24f27159c29cf7c314a5ae44c1952db40000000000000000000000000000000000000000000000000000000000000064",
        "nonce": 15,
        "transactionIndex": 0,
        "from": "0x5fc1b8f93cF4a6Aa3b35a928882Fda0296bd07F7",
        "to": "0x4448541739677099A84A24888eb0d9ad7f2fEc0e",
        "value": 0,
        "v": 101,
        "r": "0xe94b03f436a7ce2e7bc2ed6f1852801f7899af8312122b7b3feab7f861309ee3",
        "s": "0x25d3098f3fa5c27e97728d1328f98d8aa62362d6e73fa20d25f599822bda47be"
    }
}
```


- 13. 토큰 총 발행량 확인 (GET)
- http://localhost:8000/wallet/total_supply?ca={스마트 컨트랙트 주소}

```json
# Sample Response
{
  "result": 10000
}
```

- 14. 발행된 스마트 컨트랙트 함수 확인 (GET)
- http://localhost:8000/wallet/all_functions?ca={스마트 컨트랙트 주소}

```json
# Sample Response
{
  "result": "[<Function acceptOwnership()>, <Function approve(address,uint256)>, <Function approveAndCall(address,uint256,bytes)>, <Function transfer(address,uint256)>, <Function transferAnyERC20Token(address,uint256)>, <Function transferFrom(address,address,uint256)>, <Function transferOwnership(address)>, <Function allowance(address,address)>, <Function balanceOf(address)>, <Function decimals()>, <Function name()>, <Function newOwner()>, <Function owner()>, <Function symbol()>, <Function totalSupply()>]"
}
```

- 15. 모든 계정 언락 (GET)
- http://localhost:8000/wallet/unlock_all/

```json
# Sample Response
{
    "result": true
}
```


- 16. 모든 계정(지갑) 보기 (GET)
- http://localhost:8000/wallet/list/

```json
# Sample Response
[
    {
        "user_id": "kevin",
        "password": "1004",
        "address": "0x5fc1b8f93cF4a6Aa3b35a928882Fda0296bd07F7",
        "private_key": "kevin",
        "created_at": "2019-04-29T12:30:36.086854Z"
    },
    {
        "user_id": "sunny",
        "password": "1004",
        "address": "0x8889D2eE6b47984c16C24d755000fc9cF562DbF1",
        "private_key": "sunny",
        "created_at": "2019-04-29T12:30:46.119890Z"
    },
    {
        "user_id": "irene",
        "password": "1004",
        "address": "0xdFE96eA2100648025bf9A748a1Ead28734357201",
        "private_key": "irene",
        "created_at": "2019-04-29T12:30:58.444471Z"
    },
    {
        "user_id": "jeanie",
        "password": "1004",
        "address": "0x24d8c6df24F27159C29CF7C314A5AE44C1952Db4",
        "private_key": "jeanie",
        "created_at": "2019-04-29T12:31:09.284028Z"
    },
    {
        "user_id": "angelica",
        "password": "1004",
        "address": "0x66D93a3B1d024E86bef3dd8E17e9644F41ef0252",
        "private_key": "angelica",
        "created_at": "2019-04-29T22:44:08.596005Z"
    },
    {
        "user_id": "roy",
        "password": "1004",
        "address": "0xe21751aCa387b7d66Fc8F1873DC16Eb243cA1e5A",
        "private_key": "roy",
        "created_at": "2019-04-29T22:45:26.153686Z"
    },
    {
        "user_id": "mark",
        "password": "1004",
        "address": "0x0137dFea2CdF3A1C7fd25FfE95E99eAd3dC5cAac",
        "private_key": "mark",
        "created_at": "2019-04-29T22:47:49.933206Z"
    }
]
```
