# Lilleth Snavely (lls4abt)

from fastapi import FastAPI, HTTPException
from typing import Optional
import boto3
import requests
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse





app = FastAPI()

###intro to the chatbox
@app.get("/")  # zone apex
def read_root():
    return "Welcome to the astrology chatbox. Here you can learn about the twelve zodiac signs and read your daily horoscope. Try the following endpoints to get started: /signs, /signs/aquarius, /signs/aquarius/image, /signs/aquarius/learnmore, /horoscope?sign=aquarius&when=today, and try replacing aquarius with any sign of your choice."
    
    ###explain different commands

###lists out all the signs
@app.get("/signs")
def read_all_signs():
    return {"January 20 - February 18": "Aquarius",
            "February 19 - March 20": "Pisces",
            "March 21 - April 19": "Aries",
            "April 20 - May 20": "Taurus",
            "May 21 - June 20": "Gemini",
            "June 21 - July 22": "Cancer",
            "July 23 - August 22": "Leo",
            "August 23 - September 22": "Virgo",
            "September 23 - October 22": "Libra",
            "October 23 - November 21": "Scorpio",
            "November 22 - December 21": "Sagittarius",
            "December 22 - January 19": "Capricorn"}

@app.get("/signs/{sign}")
def read_sign(sign: str):
    if (sign == "aquarius" or sign == "Aqaurius"):
        return {"Element": "Air", "Color": "Light-blue/Silver", "Ruler": "Uranus", "Traits": "Independent, Original, Unemotional"}
    elif (sign == "pisces" or sign == "Pisces"):
        return {"Element": "Water", "Color": "Mauve/Lilc", "Ruler": "Neptune/Jupiter", "Traits": "Compassionate, Artistic, Overly Trusting"}
    elif (sign == "aries" or sign == "Aries"):
        return {"Element": "Fire", "Color": "Red", "Ruler": "Mars", "Traits": "Moody, Passionate, Courageous"}
    elif (sign == "taurus" or sign == "Taurus"):
        return {"Element": "Water", "Earth": "Green/Pink", "Ruler": "Venus", "Traits": "Reliable, Stubborn, Patient"}
    elif (sign == "gemini" or sign == "Gemini"):
        return {"Element": "Air", "Color": "Light-green/Yellow", "Ruler": "Mercury", "Traits": "Curious, Affectionate, Inconsistent"}
    elif (sign == "cancer" or sign == "Cancer"):
        return {"Element": "Water", "Color": "White", "Ruler": "Moon", "Traits": "Emotional, Loyal, Tenacious"}
    elif (sign == "leo" or sign == "Leo"):
        return {"Element": "Fire", "Color": "Gold/Yellow/Orange", "Ruler": "Sun", "Traits": "Creative, Arrogant, Humourous"}
    elif (sign == "virgo" or sign == "Virgo"):
        return {"Element": "Earth", "Color": "Grey/Beige/Pale-yellow", "Ruler": "Mercury", "Traits": "Analytical, Shy, Hard-working"}
    elif (sign == "libra" or sign == "Libra"):
        return {"Element": "Air", "Color": "Pink/Green", "Ruler": "Venus", "Traits": "Diplomatic, Indecisive, Cooperative"}
    elif (sign == "scorpio" or sign == "Scorpio"):
        return {"Element": "Water", "Color": "Scarlet/Red/Rust", "Ruler": "Pluto/Mars", "Traits": "Brave, Stubborn, Secretive"}
    elif (sign == "sagittarius" or sign == "Saggitarius"):
        return {"Element": "Fire", "Color": "Blue", "Ruler": "Jupiter", "Traits": "Generous, Idealistic, Impatient"}
    elif (sign == "capricorn" or sign == "Capricorn"):
        return {"Element": "Earth", "Color": "Brown/Black", "Ruler": "Saturn", "Traits": "Responsible, Condescending, Disciplined"}
    else:
        return "Thats not a valid sign, please enter one of the following: Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Saggitarius, Capricorn"
        
@app.get("/horoscope")
def get_horoscope(sign:str=None, when:str=None):
    if (sign == None and when == None):
        return "Enter a zodiac sign as query string paramter 'sign' and either yesterday, today, or tomorrow as query string parameter 'when' to read your daily horoscope"
        
    elif (sign == None):
        return "Enter a zodiac sign as query string parameter 'sign' to read your daily horoscope"
        
    elif (when == None):
        return "Enter either yesterday, today, or tomorrow as query string parameter 'when' to read your daily horoscope"
    
    elif (sign == "aquarius" or sign == "Aquarius"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'aquarius'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'aquarius'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'aquarius'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "pisces" or sign == "Pisces"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'pisces'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'pisces'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'pisces'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "aries" or sign == "Aries"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'aries'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'aries'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'aries'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "taurus" or sign == "Taurus"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'taurus'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'taurus'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'taurus'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "gemini" or sign == "Gemini"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'gemini'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'gemini'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'gemini'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "cancer" or sign == "Cancer"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'cancer'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'cancer'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'cancer'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "leo" or sign == "Leo"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'leo'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'leo'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'leo'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "virgo" or sign == "Virgo"):
        if (when == "virgo" or when == "virgo"):
            params = (
            ('sign', 'aquarius'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'virgo'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'virgo'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "libra" or sign == "Libra"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'libra'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'libra'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'libra'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "scorpio" or sign == "Scorpio"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'scorpio'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'scorpio'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'scorpio'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "sagittarius" or sign == "Sagittarius"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'sagittarius'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'sagittarius'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'sagittarius'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
    elif (sign == "capricorn" or sign == "Capricorn"):
        if (when == "today" or when == "Today"):
            params = (
            ('sign', 'capricorn'),
            ('day', 'today'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        
        elif (when == "tommorow" or when == "Tomorrow"):
            params = (
            ('sign', 'capricorn'),
            ('day', 'tomorrow'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
        elif (when =="yesterday" or when == "Yesterday"):
            params = (
            ('sign', 'capricorn'),
            ('day', 'yesterday'),
            )

            response = requests.post('https://aztro.sameerkumar.website/', params=params)
            return response.json()['description']
            
@app.get("/signs/{sign}/learnmore")
def get_sign_image(sign: str):
    sign = sign.lower()
    if (sign == "aquarius" or sign == "pisces" or sign == "aries" or sign == "tarus" or sign == "gemini" or sign == "cancer" or sign == "leo" or sign == "virgo" or sign == "libra" or sign == "scorpio" or sign == "sagittarius" or sign == "capricorn"):
    
        url = "https://www.horoscope.com/zodiac-signs/"+sign
        
      
        url2 = requests.get(url)
        htmltext = url2.text
        
        return HTMLResponse(content=htmltext, status_code=200)
    else:
        return "Thats not a valid sign, please enter one of the following: Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Saggitarius, Capricorn"
        
@app.get("/signs/{sign}/image")
def get_sign_image(sign: str):
    sign = sign.lower()
    if (sign == "aquarius" or sign == "pisces" or sign == "aries" or sign == "tarus" or sign == "gemini" or sign == "cancer" or sign == "leo" or sign == "virgo" or sign == "libra" or sign == "scorpio" or sign == "sagittarius" or sign == "capricorn"):
        
        return "https://cdn.shopify.com/s/files/1/1325/0879/articles/headers-zodiac-sign-astrology-personality-positives-negatives-cheat-sheet-"+sign+"_1024x1024.png?v=1517258109"
    else:
        return "Thats not a valid sign, please enter one of the following: Aquarius, Pisces, Aries, Taurus, Gemini, Cancer, Leo, Virgo, Libra, Scorpio, Saggitarius, Capricorn"
        
@app.get('/{path:path}', include_in_schema=False)
async def raise_404(path):
    raise HTTPException(status_code=400, detail='This endpoint does not exist. Try one of the following: /signs, /signs/aquarius, /signs/aquarius/image, /signs/aquarius/learnmore, /horoscope?sign=aquarius&when=today, and try replacing aquarius with any sign of your choice.')

        
       
    

            
            
    
    
        
        
        









