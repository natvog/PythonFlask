'''
@author: Natalie Vogel
         SDEV 300
         9/18/2023

         References:
                    - 
         
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
    
def index():
	return 'Hello, Flask!'

if __name__ == '__main__':
	app.run(debug=True)
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
# population file menu function ...
def pop_menu():
    ''' displays menu selection on screen '''
#---------------------------------------------------------------------------------------------------
# housing file menu function ...
def hous_menu():
    ''' displays menu selection on screen'''
#---------------------------------------------------------------------------------------------------
# statistics function ...
def stats(data):
    ''' calculates stats on user's chosen column from files '''
#---------------------------------------------------------------------------------------------------
# run program ...
main()
