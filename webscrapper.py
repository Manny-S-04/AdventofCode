import requests
from bs4 import BeautifulSoup
import numpy as np
from credentials import User
from os.path import exists
import time


def login(day: int):
    """ 
    
        Method to retrieve Advent of Code data
    
        Login method will take in the day number which is an integer which will be concatenated to the url to
        retrieve the associated data
        
        The method works by making a session and getting the login url by GitHub
        
        It then parses the html and searches for the forms where it will send a username and password 
        
        It the posts the data 
        
        If the login was successful then it gets the advent of code data
    
    
    """
    session = requests.Session()

    response = session.get(
        "https://github.com/login?client_id=7bb0a7ec13388aa67963&return_to=%2Flogin%2Foauth%2Fauthorize%3Fclient_id"
        "%3D7bb0a7ec13388aa67963%26duration%3Dtemporary%26redirect_uri%3Dhttps%253A%252F%252Fadventofcode.com"
        "%252Fauth%252Fgithub%252Fcallback%26response_type%3Dcode%26scope%3D%26state%3Dx")

    soup = BeautifulSoup(response.text, 'html.parser')

    form = soup.find('form')

    inputs = form.find_all('input')
    form_data = {input_field.get('name'): input_field.get('value') for input_field in inputs}

    form_data['login'] = User.username
    form_data['password'] = User.password

    response = session.post("https://github.com/session", data=form_data)

    if response.status_code == 200:

        page_response = session.get(f"https://adventofcode.com/2022/day/{day}/input")

        if page_response.status_code == 200:

            return page_response.text.splitlines()
        else:
            return "Failed to retrieve the page."
    else:
        print("Login failed.")


def savetotext(aocinput):
    inputtoarray = np.array(aocinput, dtype="U")

    np.savetxt("day2.txt", inputtoarray, fmt="%s", delimiter='\n')

    time.sleep(5)

    if (exists("day2.txt")):
        print("Done")
    else:
        print("File was not created")





savetotext(login(2))
