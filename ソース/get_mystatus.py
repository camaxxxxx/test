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
    # Get My Status.
    mystatus, info = api("/my/status")
    print(json.dumps(mystatus, indent=4))