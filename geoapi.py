import urllib.request, urllib.parse, json, ssl


service_url = "https://py4e-data.dr-chuck.net/opengeo?" #teachers nice tool for students

ctx  = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



uh = urllib.request.urlopen(service_url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js:
    pass
else:
    print(json.dumps(js, indent=4))

plus_code = js.get("plus_code", {}).get("global_code", "No Plus Code found")
print("plus_code:", plus_code)