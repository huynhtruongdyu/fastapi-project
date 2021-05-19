import requests
resp = requests.get("http://127.0.0.1:8000/hc")
if resp.status_code==200:
    print("OK :)")
else:
    print("KO :(")