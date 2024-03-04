import requests
import json

url = "http://127.0.0.1:8081/books/123549"

payload = json.dumps({
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTA4NDUyNywiaWF0IjoxNjk4OTk4MTI3LCJqdGkiOiI5YzJhZGE2ZDY5NGY0ZGY2YWY1MDFkZDE4YTA0ZWE5OSIsInVzZXJfaWQiOjN9.VDj0T61KR9fOOr-EmwfyafR0XLmRgm7SLNSMi7wcb8Y"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
