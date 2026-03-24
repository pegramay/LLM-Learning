#Basic python read into binary array (async buffer reader)
#Convert to base64 to be fed into model
#Use PIL 
# Have to turn into img url (turns into one long string)
# Open AI has img url 
# using openai SDK
# how to send image and prompt to model using openAI SDK in Python
# how to feed it just a url and feed it with prompt

import os

from openai import OpenAI
import base64
from PIL import Image
import io 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get BASE_PATH from environment variable
BASE_PATH = os.environ.get('BASE_PATH')
"""
Crucial tool since the ai yaps too much need to distinguish a little easier
"""
def help_me_read(x):
    print("=================================================================================")
    print(x)
    print("=================================================================================")

"""
Uses PIL (pillow) its a library used primarily for image manipulation

The purpose of converting it into base 64 is to get around file limitations on format from the model

Trade off of base64 though is that it increases the file size by around 33%
"""

#Load bytes into image as byte array how do I open binary file to be into a byte array 
#Need to know the mime type need to know what byte array is
def img_to_base64(image_path):
    try: 
        # Construct the full path to the image.  This is crucial.
        full_path = os.path.join(BASE_PATH, "IMIGES", image_path) #os.getcwd() gets current working directory
        print(full_path)

        # Uses PIL to open image file
        img = Image.open(full_path) #<===== Doesn't really need to be PIL image
        if img:
            print("Pil opened the image file")
        else:
            print("PIL didnt work")
        if img.mode == "RGBA": #PNG has transparency capabilities 'A' so has to be stripped to just be RGB
            img = img.convert("RGB")
        bytearray = io.BytesIO()
        img.save(bytearray, format="JPEG") #build new path with new file name <==== This is the problem
        converted_img = bytearray.getvalue()
        base64_string = base64.b64encode(converted_img).decode('utf-8')
        """
        A DIFFERENT METHOD USED HERE:
        found here: https://www.reddit.com/r/PythonProjects2/comments/1gdhayi/how_to_convert_image_to_base64_in_python/
        #opens the image file that we want to convert (this uses a url) "rb" means in binary mode
        =======================================================================
        with open(image_path, "rb") as image_file: 
        
        Opens file using binary read mode
        Reads raw bytes (MAIN DIFF)
        """
        if base64_string:
            print("Image converted succesfully")
        else:
            print("Failed to read or convert the image")
        return(base64_string)


    except FileNotFoundError:
        help_me_read(f"File not found here {image_path}")
        return None
    except Exception as e:
        help_me_read(f"A general error occurred {e}")
        return None

#loaded byte array want to conver to PIL img and convert pile 
def img_to_base64_2(image_path):
    # path_to_file can be a string, pathlib.Path, etc.
    full_path = os.path.join(BASE_PATH, "IMIGES", image_path)
    with open(full_path, "rb") as f:      # <-- binary mode
        data = bytearray(f.read())    #<=== From here conver to PIL image then in memory convert into jpg image
    base_64_result = base64.b64encode(data).decode('utf-8')      # read entire file into memory
    return base_64_result
    


"""
If img_to_base64 is able to convert into base64 string then it will feed a prompt along with the image_url 
to the model
"""
def image_url_to_prompt(image_url):
    return f"Describe the image at this URL: {image_url}.  Focus on key details and any notable features."




