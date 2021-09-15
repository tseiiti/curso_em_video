import requests
import m3u8

url = 'https://secure.brightcove.com/services/mobile/streaming/index/master.m3u8?videoId=5790241186001&pubId=3588749423001&secure=true'
req = requests.get(url)
# print(req.text)
m3u8_master = m3u8.loads(req.text)
# print(type(m3u8_master))
print(m3u8_master.data)
