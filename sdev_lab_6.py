'''
@author: Natalie Vogel
         SDEV 300
         9/18/2023

         References:
                    - 
         
'''
from flask import Flask, render_template, request
import json
import urllib.request

app = Flask(__name__)

@app.route('/', methods =['POST', 'GET'])
    
def web_page():
	if request.method == 'POST':
        city = request.form['city']
    else:
        # for default name mathura
        city = 'mathura'
  
    # your API key will come here
    api = api_key_here
  
    # source contain json data from api
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q =' + city + '&appid =' + api).read()
  
    # converting JSON data to a dictionary
    list_of_data = json.loads(source)
  
    # data for variable list_of_data
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' ' 
                    + str(list_of_data['coord']['lat']),
        "temp": str(list_of_data['main']['temp']) + 'k',
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
    }
    print(data)
    return render_template('index.html', data = data)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
#---------------------------------------------------------------------------------------------------
def main():
    '''
    This program will read csv files and calculate statistics
    Other requirements:
                    1. Validate all user inputs
                    2. Read columns to lists
                    3. Loop selection menus
                    4. Use numpy and matplotlib to get stats and display graph
    '''
#---------------------------------------------------------------------------------------------------
# define functions ...
# main file menu function ...
def file_menu():
    ''' displays menu selection on screen '''
    print('''\n\nSelect the file you want to analyze:
                [1]\tPopulation Data
                [2]\tHousing Data
                [3]\tExit the program''')
#---------------------------------------------------------------------------------------------------
# run program ...
main()
