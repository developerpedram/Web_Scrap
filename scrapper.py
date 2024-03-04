# import re
# import requests

# response = requests.get('https://qoqnoos.ir/Fa/%D8%AC%D8%AF%DB%8C%D8%AF%D8%AA%D8%B1%DB%8C%D9%86-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%87%D8%A7%DB%8C-%D9%87%DB%8C%D9%84%D8%A7')

# print(response.text)

#.............................................................

# import re
# import requests

# response = requests.get('https://qoqnoos.ir/Fa/%D8%AC%D8%AF%DB%8C%D8%AF%D8%AA%D8%B1%DB%8C%D9%86-%DA%A9%D8%AA%D8%A7%D8%A8-%D9%87%D8%A7%DB%8C-%D9%87%DB%8C%D9%84%D8%A7')
# tex = response.text
# result_1 = re.search('>.*</a>',tex)
# print(result_1.group(0))

#.............................................................

# import re
# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://qoqnoosp.com/search#!&Group-74&GroupName-%D9%83%D9%88%D8%AF%D9%83%20%D9%88%20%D9%86%D9%88%D8%AC%D9%88%D8%A7%D9%86')
# tex = response.text
# # result_1 = re.findall('>(.*?)</a>',tex)
# # print(result_1)

# soup = BeautifulSoup(tex, 'html.parser')
# # title = soup.find('title').text
# # print(title)

# for name in soup.find_all('div', class_='title'):
#     print(name.text)

#.............................................................

# import requests

# cookies = {
#     '_gid': 'GA1.2.1717584473.1708100103',
#     'Kes.customer': 'b147f254-3db4-4029-b704-1d9de72598d6',
#     '_ga': 'GA1.1.1225915013.1708100086',
#     '_ga_K7K480QGHT': 'GS1.1.1708100085.1.1.1708100430.59.0.0',
# }

# headers = {
#     'authority': 'qoqnoosp.com',
#     'accept': '*/*',
#     'accept-language': 'en-US,en;q=0.9,de;q=0.8',
#     'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # 'cookie': '_gid=GA1.2.1717584473.1708100103; Kes.customer=b147f254-3db4-4029-b704-1d9de72598d6; _ga=GA1.1.1225915013.1708100086; _ga_K7K480QGHT=GS1.1.1708100085.1.1.1708100430.59.0.0',
#     'origin': 'https://qoqnoosp.com',
#     'referer': 'https://qoqnoosp.com/search',
#     'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Linux"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
#     'x-requested-with': 'XMLHttpRequest',
# }

# data = {
#     'Group': '74',
#     'GroupName': 'كودك و نوجوان',
#     'PriceMin': '',
#     'PriceMax': '',
#     'SortType': '0',
#     'PageIndex': '0',
#     'PageSize': '32',
#     'GoodTemplateTypeId': '20',
#     'Equality': 'false',
#     'ShowInActives': 'false',
# }

# response = requests.post(
#     'https://qoqnoosp.com/api/NAFAjaxCatalog/LoadAjaxCatalogList/LoadAjaxCatalogList',
#     cookies=cookies,
#     headers=headers,
#     data=data,
# ).json()

# for name  in response['Products']:
#     x = (name['Name'])

#     add = open('namhhha.txt', 'a')
#     add.write(str(x)+'\n')
#     add.close()

#.............................................................
# Exersice: shahreketabonline.com

# import re
# import requests
# from bs4 import BeautifulSoup
# اول تیتر اصلی رو واکشی میکنیم
# به قسمت محصولات سایت شهر کتاب رفتم و لینکشو گرفتم
# response  = requests.get('https://shahreketabonline.com/Products/Category/199/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86')
# beacuase html format / change to text
# tex = response.text
# soup = BeautifulSoup(tex,'html.parser')
# از توی سایت چک کردم-تیتر اصلیش title است
# تهش دات تکست مینویسم که دیگه اون تگهای اچ تی ام ال حذف بشه
# title = soup.find('title').text
# print(title)

#.............................................................
# Now Scraping Name of Books at Shahreketab
import re
import requests
from bs4 import BeautifulSoup

import requests

cookies = {
    'CS': '[%22132737-BestSelling%22]',
    '.AspNetCore.Session': 'CfDJ8G%2B0ZTMLxvVGsAjsH0a3JofniOBxBbboV20RNMqvqfJP0BMKQd2607BulVGAQIdDU270A1I9NeQ1fmWApS57mQ91ZoF7%2BCNpT93x0X5M8%2FEGeE2JGWh%2BGpjAIOBGIiTSKde9vr5jS5qu7%2FQYmyzr1RSgP%2Fp9j3zEPDati96XvnAj',
    '_gid': 'GA1.2.770077664.1708702641',
    '_gat_gtag_UA_37489221_1': '1',
    '_ga_2HXG6NTYDY': 'GS1.1.1708776612.10.1.1708776616.56.0.0',
    '_ga': 'GA1.1.345972207.1707155575',
}

headers = {
    'authority': 'shahreketabonline.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,de;q=0.8',
    # 'cookie': 'CS=[%22132737-BestSelling%22]; .AspNetCore.Session=CfDJ8G%2B0ZTMLxvVGsAjsH0a3JofniOBxBbboV20RNMqvqfJP0BMKQd2607BulVGAQIdDU270A1I9NeQ1fmWApS57mQ91ZoF7%2BCNpT93x0X5M8%2FEGeE2JGWh%2BGpjAIOBGIiTSKde9vr5jS5qu7%2FQYmyzr1RSgP%2Fp9j3zEPDati96XvnAj; _gid=GA1.2.770077664.1708702641; _gat_gtag_UA_37489221_1=1; _ga_2HXG6NTYDY=GS1.1.1708776612.10.1.1708776616.56.0.0; _ga=GA1.1.345972207.1707155575',
    'referer': 'https://shahreketabonline.com/Products/Category/199/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
def getdata(page):
    params = {
        'ValueID': '',
        'AttributeDescriptionID': '',
        'PackageID': '',
        'CategoryID': '199',
        'ProductTypeID': '',
        'TagID': '',
        'Page': str(page),
        'ShowCase': 'False',
        'Name': '',
        'Attrs[0].AttributeOrder': '1',
        'Attrs[1].AttributeOrder': '3',
        'Attrs[2].AttributeOrder': '2',
        'Available': '',
        'SortColumn': 'CreatedOn',
        'DirectionText': 'DESC',
    }

    response = requests.get('https://shahreketabonline.com/Products', params=params, cookies=cookies, headers=headers)

    soup = BeautifulSoup(response.text,'html.parser')

    for book in soup.find_all('div',class_ = 'body'):
        try:
            name = book.find('div', class_='book-wrap')['title']
            price = str(book.find('div', class_='price').text).strip()
            img = 'https://shahreketabonline.com' + str(book.find('img')['data-src'])
            id = str(img.split('/')[-1]).replace('.jpg', '').replace('.png', '')
            
            add = open('books.csv', 'a', encoding='utf-8')
            add.write(f'{id};{name};{price};{img}\n')
            add.close()
        except:
            print(book.text)

for x in range(2, 100):
    getdata((x))

    
# response = requests('https://shahreketabonline.com/Products/Category/199/%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86')
# tex = response.text
# soup = BeautifulSoup(tex,'html.pareser')
# for name in soup.find_all('div',class_ = 'text'):
#     print(name)
# view page source => text/javascript
# Transaction to transfor data from server to client by Ajax => We can not track Ajax
# Transaction is in Network Tab (Header)
# اما اینجا ایجکس هم نیست بلکه جیسون هست  => json
# Fetch / XHR => Collect => Preview => empty! (no product and data)















