from urllib.request import Request, urlopen
import json
from selenium import webdriver
import time

def look_for_new_video():
    api_key = "AIzaSyB6wcymMF1doilibsm-ae-TEXXqf8E_pY4"
    channel_id = "UCeoU2maQX8JiQ9DTuhOVz5g"

    base_url = "https://www.cowin.gov.in/home"
    base_search_url = "https://www.googleapis.com/youtube/v3/search?"
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=376&date=13-05-2021"
    req = Request('https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=376&date=14-05-2021', headers={'User-Agent': 'Mozilla/5.0'})
    imp = urlopen(req)
    res = json.load(imp)
    # driver = webdriver.Firefox(executable_path='E:\\Setups\\geckodriver.exe')
    # driver.get(url='https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=376&date=13-05-2021')

    for key in range(len(res['centers'])):
       sess_len = len(res['centers'][key]['sessions'])
       # sess_len = sess_len-1
       for sess_id in range(sess_len):
        capacity = res['centers'][key]['sessions'][sess_id]['available_capacity']
        # print(res['centers'][key]['block_name']) #block_name
        # print("Available Slots ", capacity)
        if capacity > 0:
            print(res['centers'][key]['block_name'])  # block_name
            print("Available Slots ", capacity)
            block_name = res['centers'][key]['block_name']
            print(block_name.find('Phaltan'))
            if(block_name.find('Phaltan')==-1 and block_name.find('Karad')==-1 ):
                driver = webdriver.Firefox(executable_path='E:\\Setups\\geckodriver.exe')
                driver.get(url=base_url)
    # print(res)
    # print("Total Centers ", len(res['centers']))


    video_exists=False
    #driver = webdriver.Firefox(executable_path='E:\\Setups\\geckodriver.exe')
    #driver = webdriver.Chrome(executable_path='E:\\Setups\\chromedriver.exe')
    #driver.get(url=base_video_url)
    video_exists = True








try:
    while True:
        look_for_new_video()
        time.sleep(5)
except KeyboardInterrupt:
    print("stopping")






