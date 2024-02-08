import re
import requests


response = requests.get('https://shahreketabonline.com/Products/Category/199/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86')


print(response.text)