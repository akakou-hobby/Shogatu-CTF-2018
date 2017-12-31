# coding: utf-8
'''problem.py
    問題作成スクリプト
'''

''' 各変数の初期化 '''
### flagの画像ファイル
flag = {
    'file': open('flag.png', 'rb' ),    # ファイル
    'data': bytes(),                    # データ
    'length': int()                     # データの長さ
}
flag['data'] = flag['file'].read()
flag['length'] = len(flag['data'])

### ボケる方のファイル
boke = {
    'file': open('boke', 'wb'),         # ファイル
    'data': bytes()                     # データ
}

### 普通の方のファイル
hutsu = {
    'file': open('hutsu', 'wb'),        # ファイル
    'data': bytes()                     # データ
}

''' ファイルの切り分け '''
for count, data in enumerate(flag['data']):
    if (count + 1) % 3 == 0 or '3' in str(count + 1):
        ### ボケる場合
        boke['data'] += data.to_bytes(1, 'little')
        message = 'boke'
    else:
        ### ボケない場合
        hutsu['data'] += data.to_bytes(1, 'little')
        message = ''

    print('{0}/{1} {2} !'.format(count + 1, flag['length'] + 1, message))

''' ファイルの保存 '''
boke['file'].write(boke['data'])
hutsu['file'].write(hutsu['data'])
