from spellcheck import check
from colors import *
import requests
import os

def refresh_xcsrf():
  with requests.Session() as client:
    client.cookies['.ROBLOSECURITY'] = os.environ['COOKIE']
    response = client.post('https://auth.roblox.com/v1/login')
    if 'X-CSRF-TOKEN' in response.headers:
      return response.headers["X-CSRF-TOKEN"]

def get_item_price(id):
  headers = {
    'Content-Type': 'application/json',
    'x-csrf-token': refresh_xcsrf()
  }
  cookies = {'.ROBLOSECURITY': os.environ['COOKIE']}
  request = requests.get(f'https://economy.roblox.com/v1/assets/{id}/resellers', headers=headers, cookies=cookies)
  return request.json()['data'][0]['price']
  
# load new limited dataset
data = requests.get('https://rolimons.com/itemapi/itemdetails').json()['items']
os.remove('items.txt')
items = []
items_list = {}
for item in data:
  items_list["".join(data[item][0].lower().split())] = [item, data[item][0], data[item][2]]
  items.append("".join(data[item][0].lower().split()))
with open('items.txt','a') as file:
  file.write('\n'.join(items))

while True:
  # checkspelling
  name = check(''.join(input().split()))
  id = items_list[name][0]

  os.system('clear')
  average = round((get_item_price(id)+items_list[name][2])/2)
  print(f'{blue}{items_list[name][1]}{white}\n\tSelling: ${"{:,}".format(get_item_price(id))}\n\tRAP: {"{:,}".format(items_list[name][2])}\n\tAverage: {green}${"{:,}".format(average)}{white}')
