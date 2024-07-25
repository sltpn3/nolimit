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
untuk mengubah *response_content* perlu menggunakan ca certificate untuk melakukan TLS Interception


## 2. Wikipedia Scraper
Untuk menggunakan bash script, ubah lokasi variabel **scraper_path** dan **python_path** dalam run_scraper.sh

```bash
./run_scraper.sh "michael jackson"
./run_scraper.sh "michael jackson" "http://localhost:9919"
```

## 3. Wikipedia Scraper 2
```bash
python wikipedia_scraper2.py -u https://en.wikipedia.org/wiki/Proxy_server
```
Scraper ini terbatas hanya pada halaman wiki Wikipedia.
Scraper lebih baik bila melakukan subscribe pada suatu MQ sehingga dapat dimonitor task yang sedang dilakukan serta berapa task yang tersisa. 