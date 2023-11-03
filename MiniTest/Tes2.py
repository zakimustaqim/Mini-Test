import requests
import datetime

LATITUDE = "-6.200000"
LONGITUDE = "106.816666"
API_KEY = "02493c8da845259b4813f984a1b8a634"
UNITS = "metric"
Api_url = "https://api.openweathermap.org/data/2.5/forecast?lat=" + LATITUDE + "&lon=" + LONGITUDE + "&appid=" + API_KEY + "&units=" + UNITS

raw_data_dict = requests.get(Api_url).json()
status_code = raw_data_dict['cod']

if (status_code == 400):
    print(raw_data_dict['message'])
else:
    list_data = raw_data_dict['list']
    #dict_5dayforcasting = {"0" = [Date,SumTemp,LotData], ...}
    dict_5dayforcasting = {0: ['Tanggal', 0, 0]}
    count_day = 0
    count_data = 1
    for data in list_data:
        if(dict_5dayforcasting[count_day][0] == data['dt_txt'][0:10]):
            count_data += 1
            dict_5dayforcasting[count_day][1] = dict_5dayforcasting[count_day][1] + data['main']['temp']
            dict_5dayforcasting[count_day][2] = count_data
        else:
            count_data = 1
            count_day += 1
            dict_5dayforcasting[count_day] = [data['dt_txt'][0:10], data['main']['temp'], count_data]
            
    dict_5dayforcasting.pop(0)
    for day_forcasting in dict_5dayforcasting:
        dd = int(dict_5dayforcasting[day_forcasting][0][8:10])
        mm = int(dict_5dayforcasting[day_forcasting][0][5:7])
        yyyy = int(dict_5dayforcasting[day_forcasting][0][0:4])
        format_date = datetime.datetime(yyyy, mm, dd)
        str_day = format_date.strftime("%a")
        str_Month = format_date.strftime("%b")
        val_temp = dict_5dayforcasting[day_forcasting][1]/dict_5dayforcasting[day_forcasting][2]
        print("{}, {} {} {}: {:.2f} C".format(str_day, dd, str_Month, yyyy, val_temp))
