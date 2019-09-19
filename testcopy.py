import requests
import math
from bs4 import BeautifulSoup
import urllib.request

# LẤY THÔNG TIN TỪNG TRANG
# for i in range(29331,29334)

# LẤY LINK TỪNG DỰ ÁN
url = "https://lendwithcare.org/loans/36240"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# for da in soup.find_all("h3"):

# du_an = soup.find("div",{"class":"wrapper"})
# for da in du_an:
#     link_du_an = da.get('href')
#     ten = da.find('h3')
#     ten1 = ten.text
# print(ten1)    
# du_an = soup.find("div")
# du_an = soup.find_all('p')
print(soup)
# print(du_an)
# print(link_du_an)
        # # THÊM THÔNG TIN DỰ ÁN VÀO LIST THEO GROUP
        # if tt == '$1,500':
        #         quyquy1500.append({"ten":ten1,"luot binh chon":bc,"muc tai tro":tt})
        # elif tt == '$3,000':
        #         quyquy3000.append({"ten":ten1,"luot binh chon":bc,"muc tai tro":tt})
        # elif tt == '$5,000':
        #         quyquy5000.append({"ten":ten1,"luot binh chon":bc,"muc tai tro":tt})

# print(ten1)