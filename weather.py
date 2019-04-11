import requests, time

def print_temp():
    try:                             #returns a JSON object with current weather info for the given zipcode
        zipcode = int(input("What is your zipcode?\n"))
        country = "za"                                 #set country so South Africa
        api_key = "yourapikey"   #From home.openweathermap.org/api_keys
        # create a JSON object from a call to the generated API URL:
        resp = requests.get("http://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}".format(zipcode, country, api_key))
        json_object = resp.json()
        city = json_object['name']
        temp_k = json_object['main']['temp']
        temp_c = temp_k - 273.15
        return ".\nIt is currently {} degrees Celsius in {}".format(temp_c, city)
    except:
        print("Please ensure that you're entering a valid ZA zipcode")
        print_temp()        #re-run function in case of error


print(print_temp() + "\n.\n.\n.\nclosing in 15 seconds")
time.sleep(15)
