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

- 발급할 토큰 홀더 정보와 함께 디플로이를 요청 합니다.
- 홀더 계정이 eth.coinbase 이면서, 마이닝을 하고 있는 상태이어야 합니다.
- POST -> http://localhost:8000/wallet/deploy/

```json
{
  "userId": "kevin",
  "address": "0x9b69441c0b638f66C1f88411BD37f0D67C9975C5"
}
```

- 정상적인 호출인 경우

```json
{
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109",
  "createdAt": "2019-04-26 03:07:26.843151+00:00"
}
```

- 스마트 컨트랙트 배포 후, 참여자들에게 토큰을 배분합니다.
- 토큰 홀더용 API 이기 때문에, 수신자 정보와 금액, CA 정보만 사용합니다.
- POST -> http://localhost:8000/wallet/transfer_token/

```json
{
  "receiver": {
    "userId": "ellie",
    "address": "0x3d2a0F636b3E95B9f15Ce8d0c57366e62D5514b8"
  },
  "amount": 100,
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109"
}
```

- 정상적인 호출인 경우 반환되는 메시지

```json
{
  "blockNumber": 8081,
  "from": "0xae628b2698d1f213d461307b139f255d01febafb",
  "gasUsed": 36158
}
```

- 이제 참여자간 토큰을 전송해 보겠습니다.
- 수신자와 송신자, 수량과 CA 정보로 API 호출합니다.
- POST -> http://localhost:8000/wallet/transfer_token_from/

```json
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

- 정상적인 호출 시 반환 예상 값

```json
{
  "blockNumber": 8304,
  "from": "0xae628b2698d1f213d461307b139f255d01febafb",
  "gasUsed": 37408
}
```

- 토큰이 전송 되었는지, 각 계정의 잔고를 확인하는 방법
- POST -> http://localhost:8000/wallet/balance_of/

```json
{
  "userId": "irene",
  "address": "0x62Cf333dB24179824ddD7036ea9De7771C875A36",
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109"
}
```

- 정상적으로 수행되었을 경우, 반환 값

```json
{
  "result": 5200
}
```

- 추가1: 토큰 총 발행량 확인
- GET -> http://localhost:8000/wallet/total_supply?ca={스마트 컨트랙트 주소}

```json
{
  "result": 10000
}
```

- 추가2: 발행된 스마트 컨트랙트 함수 확인
- GET -> http://localhost:8000/wallet/all_functions?ca={스마트 컨트랙트 주소}

```json
{
  "result": "[<Function acceptOwnership()>, <Function approve(address,uint256)>, <Function approveAndCall(address,uint256,bytes)>, <Function transfer(address,uint256)>, <Function transferAnyERC20Token(address,uint256)>, <Function transferFrom(address,address,uint256)>, <Function transferOwnership(address)>, <Function allowance(address,address)>, <Function balanceOf(address)>, <Function decimals()>, <Function name()>, <Function newOwner()>, <Function owner()>, <Function symbol()>, <Function totalSupply()>]"
}
```

- 추가3: 테스트용 계정 언락 API
- GET -> http://localhost:8000/wallet/unlock_all/

```json
{
  "result": true
}
```
