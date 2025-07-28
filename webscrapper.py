# This app scrap data from booking.com

"""



hotel name
price
location
ratings
reviews
link
save

"""

import requests
from bs4 import BeautifulSoup
import lxml
import csv
import time

# url_text = 'https://www.booking.com/searchresults.en-gb.html?ss=Port+Elizabeth&ssne=Port+Elizabeth&ssne_untouched=Port+Elizabeth&efdco=1&label=en-za-booking-desktop-6vl3YhHpuvNniarrGnwKowS652796016207%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-51481728%3Alp1028624%3Ali%3Adec%3Adm&aid=2311236&lang=en-gb&sb=1&src_elem=sb&src=index&dest_id=-1273448&dest_type=city&checkin=2025-08-01&checkout=2025-08-04&group_adults=2&no_rooms=1&group_children=0'


def web_scrapper(web_url, f_name):
   
   # greetings
   print('Thank you for sharing url and file name!\nReading the content!')

   #processing
   time.sleep(5)


   header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'}


   response = requests.get(web_url, headers= header)


   if response.status_code == 200:
   
    print('Connected to the Website!')
    html_content = response.text

    
    # creating soup
    soup = BeautifulSoup(html_content, 'lxml')

    #print(soup.prettify())

    #main container
    hotel_divs = soup.find_all('div', role='listitem')

    with open(f'{f_name}.csv', 'w', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)

        # adding header
        writer.writerow(['hotel_name', 'locality', 'price', 'rating', 'score', 'review', 'link'])

        for hotel in hotel_divs:
            hotel_name = hotel.find('div', class_="b87c397a13 a3e0b4ffd1").text.strip()
            hotel_name if hotel_name else 'NA'

            location = hotel.find('span', class_="d823fbbeed f9b3563dd4").text.strip()
            location if location else 'NA'

                # price
            price = hotel.find('span', class_="b87c397a13 f2f358d1de ab607752a2").text.strip().replace('ZARÂ', '')
            if price: 
                price
            else:
                'NA'
                

            rating = hotel.find('div', class_="f63b14ab7a f546354b44 becbee2f63").text.strip()
            rating if rating else 'NA'

            score = hotel.find('div', class_="f63b14ab7a dff2e52086").text.strip()
            score if score else 'NA'

            review = hotel.find('div', class_="fff1944c52 fb14de7f14 eaa8455879").text.strip()
            review if review else 'NA'

                # getting the link
            link = hotel.find('a', href=True).get('href')
            link if link else 'NA'
                

                # saving the file into csv
            writer.writerow([hotel_name, location, price, rating, score, review, link])


        #print(hotel_name)
        #print(location)
        #print(price)
        #print(rating)
        #print(score)
        #print(review)
        #print(link)
        #print('')





   else:
    print(f'Connection failed{response.status_code}')



# if using this script then below task will be executed
if __name__ == '__main__':
   
   url = input('Please enter url! :')
   fn = input('Please give file name! :')

   # calling the function
   web_scrapper(url, fn)











