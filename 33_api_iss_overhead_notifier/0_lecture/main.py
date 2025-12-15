import constants as cons
import requests

res = requests.get(url=cons.API_ISS_CUR_LOC)
res.raise_for_status()
# print(res)  # <Response [200]>
# print(res.status_code, type(res.status_code)) # 200 <class 'int'>
data = res.json()
iss_location = (
    data["iss_position"]["longitude"],
    data["iss_position"]["latitude"],
)
print(iss_location)
