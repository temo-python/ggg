import requests
import json
response = requests.get("https://openweathermap.org/api/one-call-3")
print(response.content)
print(response.status_code)
print(response.headers)