# chatbot-API
An interactive, CLI-based chatbot. This chatbot informs users on all things astrology including zodiac signs and daily horoscope readings

# Technical detials
This chatbot was created using uvicorn and FastAPI. Including in this repository is a folder titled "app" which includes the "main.py" -- a python file where the API is created from the FastAPI package. It also includes a Dockerfile which builds a container image from the "tiangolo/uvicorn-gunicorn-fastapi:python3.7-alpine3.8" base image. The repository also contains a file "requirements.txt" which the Dockerfile interacts with to install everything needed for the container image to be complete.

# The endpoints
The atrology chatbox includes several different endpoints from which the user can obtain information from.
  
### / 
This initial endpoint gives the user a short introduction and some endpoints to try out
  
## /signs 
This endpoint lists all the zodiac signs and what range of dates they match up with
  
## /signs/{sign} 
This endpoint gives more specific information about the particular sign entered. For example, "/signs/aquarius" will provide the user with information about the Aquarius Zodiac sign including some characteristics and the signs Ruler.
   
### /horoscope 
This endpoint reads the user it's daily horoscope. This endpoint requires two query string parameters: sign and when. Sign can be any of the twelvezodiac signs (capitilization does not matter) and when can either be "today," "tomorrow," or "yesterday" (again, capitilization does not matter). If the user forgets to include one or both of the query string parameters, the chatbot will communicate this with the user.

## /signs/{sign}/learnmore
This endpoint displays a webpage where the user can get more information about the specific sign they enter. HTML is utilized for this endpoint to display the HTML code from a webpage based on a URL.

## /signs/{sign}/image
This endpoint returns a link that leads to an image of the specific sign entered. 
                 
      
