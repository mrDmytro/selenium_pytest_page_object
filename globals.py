import os


"""
There are our globals variables
"""
BASE_URL = 'https://google.ua'
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))
DRIVERS = os.path.join(BASE_DIR, r'drivers')
CHROME_DRIVER = os.path.join(DRIVERS, r'chromedriver')
