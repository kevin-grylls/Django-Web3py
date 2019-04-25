import sys
import os
import json

cur_dir = os.path.dirname(__file__)
abi_path = os.path.join(cur_dir, '..', 'contracts', 'abi.json')
bin_path = os.path.join(cur_dir, '..', 'contracts', 'bytecode.json')


# ERC20 Token 종류에 따라 추가/커스텀해서 사용하세요.


def get_abi():
    with open(abi_path, 'r') as f:
        source = f.read()

    return source


def get_bin():
    with open(bin_path, 'r') as f:
        source = f.read()

    return json.loads(source)
