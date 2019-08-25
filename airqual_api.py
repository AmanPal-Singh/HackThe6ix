import json
import requests

#r = requests.get('https://tiles.waqi.info/tiles/usepa-aqi/100/100/100.png?token=b0e6185f723c21da3275680c7efcf17db44a0aad').json()
r_2= requests.get('https://api.waqi.info/feed/toronto/?token=b0e6185f723c21da3275680c7efcf17db44a0aad').json()
air_quality = r_2['data']['aqi']

api_token = 'b0e6185f723c21da3275680c7efcf17db44a0aad'

print(air_quality)
