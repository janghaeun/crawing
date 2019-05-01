import requests
#http get방식으로 가져오기
req = requests.get('https://beomi.github.io/')
#html 소스 가져옴
html = req.text
#http header 가져오기
header = req.headers
#http status가져오기
status = req.status_code
#http정상작동 확인(true,false)
is_ok = req.ok