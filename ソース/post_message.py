import sys, os
import urllib.request
import json
import pprint

# APIのエンドポイント
ENDPOINT = "https://api.chatwork.com/v2"

# APIキー
apikey = "e1531a1547f378ae47ceb94c4a1ad151"

# ChatworkのAPIをコールする関数
# @params path（必須）: APIのパス
# @params data（任意）: 送信するデータ
def api (path, data=None):
    # 送信データがある場合にはURLエンコードする
    if data != None:
        data = urllib.parse.urlencode(data)
        data = data.encode('utf-8')
    # APIキーをヘッダーに付与する
    headers = {"X-ChatWorkToken": apikey}
    # リクエストの生成と送信
    req = urllib.request.Request(ENDPOINT + path, data=data, headers=headers)
    with urllib.request.urlopen(req) as res:
        # API結果
        result = json.loads(res.read().decode("utf-8"))
        # レスポンスヘッダ（残利用可能数などが入っている）
        info = dict(res.info())
        return result, info

if __name__ == '__main__':
    argv = sys.argv
    # つぶやく
    roomid = argv[1]
    path = "/rooms/%s/messages" % roomid
    str_arg = argv[0].replace('％', os.linesep)
    #data = {"body": argv[2]}
    data = {"body": str_arg}
    result, info = api(path, data)
    print(json.dumps(result, indent=4, sort_keys=True, ensure_ascii=False))
