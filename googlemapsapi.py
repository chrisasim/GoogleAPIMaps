import googlemaps
import pandas as pd
import time

def miles_to_meters(miles):
 try:
   return miles * 1,609.344
 except:
   return 0


API_KEY = open('API_KEY.txt', 'r').read()
map_client = googlemaps.Client(API_KEY)
location = (37.779803615891, -122.43864142750198)
search_string = "ramen"
distance = miles_to_meters(15)
business_list = []
response = map_client.places_nearby(
location = location, 
keyword = search_string, 
name = 'rame shop',
radius = distance
)

business_list.extend(response.get('results'))
print(response.keys())
next_page_token = response.get('next_page_token')
while next_page_token:
 time.sleep(2)
 response = map.client.places_nearby(
 Locaton = location, 
 keyword = search_string, 
 name = 'ramen shop',
 radius = distance, 
 page_token = next_page_token
)
business_list.extend(response.get('results'))
next_page_token = response.get('next_page_token')
df = pd.DataFrame(business_list)
df['url'] = 'https://www.google.com/maps/place/?q=place_id'+ df['place_id']
df.to_excel('ramen shop list.xlsx', index=False)
