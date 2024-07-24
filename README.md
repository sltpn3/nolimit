# nolimit
## Install Requirements
```bash
pip install -r requirements.txt
```
## 1. Forward Proxy
### Run forward proxy curl 1 & 2
```bash
python simple_proxy1.py
```

### Run cURL
```bash
curl -x http://localhost:9919 https://google.com/search -vvv
curl -x http://localhost:9919 https://en.wikipedia.org/wiki/Proxy_server -vvv
```

### Run forward proxy curl 3
```bash
python simple_proxy2.py
```

### Run cURL
```bash
curl -x http://localhost:9919 --cacert  ca-cert.pem https://en.wikipedia.org/wiki/Proxy_server -vvv
```