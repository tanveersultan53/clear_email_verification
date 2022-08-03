from crypt import methods
import imp
from flask import Flask,request,jsonify
from requests.auth import HTTPProxyAuth
import requests

app = Flask(__name__)


proxies = {
'http':'http://asuedxxn:crl0h8hc789v@45.137.60.112:6640',
'http':'http://asuedxxn:crl0h8hc789v45.140.13.124:9137',
'http':'http://asuedxxn:crl0h8hc789v@45.140.13.112:9125',
'http':'http://asuedxxn:crl0h8hc789v@45.142.28.20:8031',
'http':'http://asuedxxn:crl0h8hc789v@45.140.13.119:9132',
'http':'http://asuedxxn:crl0h8hc789v@45.142.28.145:8156',
'http':'http://asuedxxn:crl0h8hc789v@45.142.28.187:8198',
'http':'http://asuedxxn:crl0h8hc789v@176.116.230.128:7214',
'http':'http://asuedxxn:crl0h8hc789v@176.116.230.151:7237',

# 'https':'https://asuedxxn:crl0h8hc789v@45.137.60.112:6640',
# 'https':'https://asuedxxn:crl0h8hc789v45.140.13.124:9137',
# 'https':'https://asuedxxn:crl0h8hc789v@45.140.13.112:9125',
# 'https':'https://asuedxxn:crl0h8hc789v@45.142.28.20:8031',
# 'https':'https://asuedxxn:crl0h8hc789v@45.140.13.119:9132',
# 'https':'https://asuedxxn:crl0h8hc789v@45.142.28.145:8156',
# 'https':'https://asuedxxn:crl0h8hc789v@45.142.28.187:8198',
# 'https':'https://asuedxxn:crl0h8hc789v@176.116.230.128:7214',
# 'https':'https://asuedxxn:crl0h8hc789v@176.116.230.151:7237',
}

auth = HTTPProxyAuth("asuedxxn", "crl0h8hc789v")
@app.route('/',methods=['POST'])
def home():
    try:
        request_data = request.get_json()
        if request_data:
            response = requests.get(f'https://dashboard.clearbit.com/demos/person?email={request_data["email"]}',proxies=proxies,auth=auth)
            return jsonify(response.json())
    except Exception as e:
        print(e)
        return jsonify({"data":str(e)})

if __name__ == '__main__':
    app.run(host="0.0.0.0")