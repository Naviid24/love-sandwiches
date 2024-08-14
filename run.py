#Install it first by using terminal
#We can access any function, class or method in it
import gspread
#Import just Credentials class which is part of the service account function from the google auth library
from google.oauth2.service_account import Credentials
 #The scope lists the APIs that the program should access in order to run.
 #scope vriable will not change,so it's known as constant and in Python we write const variable namess in capitals
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

#
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

#Access data in our sales worksheet
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)


