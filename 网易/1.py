import requests
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import json






i = 'fEDB6BMSMieRrrcP'
aa = '010001'
bb = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
cc = '0CoJUm6Qyw8W8jud'
rawdata = {
    'csrf_token': "",
    'cursor': '-1',
    'offset': '0',
    'orderType': '1',
    'pageNo': '1',
    'pageSize': '20',
    'rid': "R_SO_4_2635505693",
    'threadId': "R_SO_4_2635505693",
}

def geti():
    c = ''
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    nu=0
    while nu < 16:
        e = random.randint(0,len(string)-1)
        c += string[e]
        nu += 1
    return c

#def getenctext(d,e,f,g):


class encobj():
    def __init__(self,d,e,f,g):#(rawdata,aa,bb,cc)
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        #self.i = geti()
        self.i = 'fEDB6BMSMieRrrcP'
        self.t = self.getAEStext(self.d, self.g)
        self.text = self.getAEStext(self.t, self.i)
        self.key = self.getRSAkey()

    def getAEStext(self, a, b):
        iv = "0102030405060708"
#        a = pad(json.dumps(a).encode('utf-8'), AES.block_size)
        a = pad(a.encode('utf-8'), AES.block_size)
        print(a)
        cipher = AES.new(key=b.encode('utf-8'), mode=AES.MODE_CBC, IV=iv.encode('utf-8'))
        ciphertext = cipher.encrypt(a)
        #print(ciphertext)
        return str(base64.b64encode(ciphertext), 'utf-8')
    def getRSAkey(self):
        e = int(self.e,16)#公钥
        f = int(self.f,16)#模
        public_key = RSA.construct((f, e))
        cipher = PKCS1_OAEP.new(public_key)
        # 加密消息
        encrypted_message = cipher.encrypt(self.i.encode('utf-8'))
        # 返回 Base64 编码的密文
        return encrypted_message.hex()

#    base64.b64encode(encrypted_message).decode('utf-8')
#print(cc)

rawdata = json.dumps(rawdata)
th = encobj(rawdata,aa,bb,cc)
print('-------')
print(th.text)
#print(th.key)
data = {
    'params':th.text,
    'encSecKey': th.key
}
header = {
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0'
}
url = 'https://music.163.com/weapi/comment/resource/comments/get?'
res = requests.post(url, data=data)
res.encoding='utf-8'
print(res.text)
#with open('test.json', 'w') as f:
#    json.dump(res.json(), f)
print(res.status_code)






