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
