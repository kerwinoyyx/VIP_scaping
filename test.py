import  bs4
import  requests
import  re
import time
start=time.time()
url='http://ugcsochy.tcdn.qq.com/vwecam.tc.qq.com/1097_3c14f71941eb46b3b4f179e1616fdbbb.f0.mp4?vkey=A0E365D37187BC8B7ACBA333B4F791CF52FB55B5E88DD7FFF9564B4BDE1F81B200BC9D2C0D546B64436D3073A3D6EF95B6B2D222577D06F6&rf=mobile.qzone.qq.com&ocid=1437865388&ocid=1437865388'
kv = {'user-agent': 'Mozilla/5.0'}
r=requests.get(url,stream=True)
f=open('C:/Users/kerwi/Desktop/电影/龙牌之迷.mp4','wb')
for chunk in r.iter_content(chunk_size=512):
    if chunk:
        f.write(chunk)
end=time.time()
print(end-start)