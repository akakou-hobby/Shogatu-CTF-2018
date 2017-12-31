# coding: utf-8
'''problem.py
    問題作成スクリプト
'''

''' 各変数の初期化 '''
### flagの画像ファイル
flag = {
    'file': open('flag.png', 'wb' ),    # ファイル
    'data': bytes(),                    # データ
    'length': int()                     # データの長さ
}

### ボケる方のファイル
boke = {
    'file': open('../boke', 'rb'),         # ファイル
    'data': list()                      # データ
}
boke['data'] = boke['file'].read()
boke['data'] = list(boke['data'])
boke['length'] = len(boke['data'])

### 普通の方のファイル
hutsu = {
    'file': open('../hutsu', 'rb'),        # ファイル
    'data': list()                      # データ
}
hutsu['data'] = hutsu['file'].read()
hutsu['data'] = list(hutsu['data'])
hutsu['length'] = len(hutsu['data'])

''' ファイルの切り分け '''
for count in range(0, hutsu['length'] + boke['length'] - 1):
    if (count + 1) % 3 == 0 or '3' in str(count + 1):
        ### ボケる場合
        flag['data'] += boke['data'].pop(0).to_bytes(1, 'little')
        message = 'boke'
    else:
        ### ボケない場合
        flag['data'] += hutsu['data'].pop(0).to_bytes(1, 'little')
        message = ''

    print('{0}/{1} {2} !'.format(count + 1, hutsu['length'] + boke['length'] + 1, message))

''' ファイルの保存 '''
flag['file'].write(flag['data'])
