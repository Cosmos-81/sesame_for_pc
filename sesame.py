import os
import datetime, base64, requests, json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES

def operation_sesame(operation_username,cmd_number):

    # cmd_number # 88/82/83 = toggle/lock/unlock

    # 認証項目を環境変数から取得
    uuid = os.getenv('API_KEY_SESAME4_UUID')
    secret_key = os.getenv('API_KEY_SESAME4_SECRET_KEY')
    api_key = os.getenv('API_KEY_SESAME4_API_KEY')

    # 環境変数のチェック
    if uuid is None or secret_key is None or api_key is None:
        print('環境変数が設定されていません')
        return    

    # ユーザー名をbase64でエンコード
    operation_username = str(operation_username)
    base64_history = base64.b64encode(bytes(operation_username, 'utf-8')).decode()

    headers = {'x-api-key': api_key}
    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)

    ts = int(datetime.datetime.now().timestamp())
    message = ts.to_bytes(4, byteorder='little')
    message = message.hex()[2:8]
    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)

    cmac.update(bytes.fromhex(message))
    sign = cmac.hexdigest()
    # 鍵の操作
    url = f'https://app.candyhouse.co/api/sesame2/{uuid}/cmd'
    body = {
        'cmd': cmd_number,
        'history': base64_history,
        'sign': sign
    }
    res = requests.post(url, json.dumps(body), headers=headers)

    if(res.status_code == 200):
        return True
    else:
        return False