####

- 참고사항

---

- DB: PostgreSQL -> localhost:5432
- Web3: Web3.py -> 가나슈 혹은 로컬 개발환경에 맞춰서 사용하면 됩니다.
- Contract: root/contracts/\* -> 토큰 디플로이에 시간이 소요되므로 잠시 기다리셔야 됩니다.

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

- ERC20 토큰 내에서 거래할 계정들을 먼저 생성합니다.
- POST -> http://localhost:8000/wallet/create/

```json
{
  "userId": "kevin",
  "password": "1004"
}
```

- 계정 생성 직후나 로그인 후에도 개인 정보 확인이 가능합니다.
- POST -> http://localhost:8000/wallet/login/

```json
{
  "userId": "kevin",
  "password": "1004"
}
```

- 정상적인 호출인 경우

```json
{
  "userId": "kevin",
  "password": "1004",
  "address": "0x9b69441c0b638f66C1f88411BD37f0D67C9975C5",
  "privateKey": "kevin",
  "createdAt": "2019-04-26T02:12:03.383Z"
}
```

- 발급할 토큰 홀더 정보와 함께 디플로이를 요청 합니다.
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

- 토큰 생성 직후, 참여자들에게 토큰을 배분합니다.
- 스마트 컨트랙트 디플로이 후 홀더가 참여자에게 토큰을 배분하는 API
- 토큰 홀더용 API 이기 때문에, 수신자 정보와 금액, CA 정보만 사용합니다.
- POST -> http://localhost:8000/wallet/transfer_token

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

- 토큰이 전송 되었는지, 각 계정의 잔고를 확인하는 방법
- POST -> http://localhost:8000/wallet/balance_of/

```json
{
  "userId": "irene",
  "address": "0x62Cf333dB24179824ddD7036ea9De7771C875A36",
  "contractAddress": "0x5EDD1E5BDB6ddF68515F3c18FCbc133C6c2E3109"
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
