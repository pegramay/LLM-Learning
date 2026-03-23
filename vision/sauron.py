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
        full_path = os.path.join(os.getcwd(), "IMIGES", image_path) #os.getcwd() gets current working directory
        print(full_path)

        # Uses PIL to open image file
        img = Image.open(full_path) #<===== Doesn't really need to be PIL image
        if img:
            print("Pil opened the image file")
        else:
            print("PIL didnt work")
        img.save("monkey.jpg", format="JPEG") #build new path with new file name <==== This is the problem


        """
        A DIFFERENT METHOD USED HERE:
        found here: https://www.reddit.com/r/PythonProjects2/comments/1gdhayi/how_to_convert_image_to_base64_in_python/
        #opens the image file that we want to convert (this uses a url) "rb" means in binary mode
        =======================================================================
        with open(image_path, "rb") as image_file: 
        
        Opens file using binary read mode
        Reads raw bytes (MAIN DIFF)
        """
        #Read content of BytesIO as bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format="JPEG")
        img_byte_arr.seek(0)
        img_bytes = img_byte_arr.read()
        if img_bytes:
            print("Contents read successfully")
        else:
            print("Contents failed to read")
        #base64.b64encode(): Encodes the binary data to Base64 format.
        #.decode('utf-8'): Converts the byte-like object into a readable string.
        base64_string = base64.b64encode(img_bytes).decode('utf-8')
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

"""
If img_to_base64 is able to convert into base64 string then it will feed a prompt along with the image_url 
to the model
"""
def image_url_to_prompt(image_url):
    return f"Describe the image at this URL: {image_url}.  Focus on key details and any notable features."




