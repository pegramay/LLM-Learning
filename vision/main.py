from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv
import sauron

def main():
    load_dotenv(find_dotenv())
    client = OpenAI(base_url=os.getenv('LLM_URL'), api_key="lm-studio")
    while True:
        x = input("Enter image name: ")
        if x == "quit" or x =='q':
            break
        base_64_img = sauron.img_to_base64(x)
        if base_64_img:
            print("img to url to prompt called")
            #x = sauron.image_url_to_prompt(base_64_img)
            completion = client.responses.create(
            model = os.getenv('LLM_MODEL'),
            input=[
                {"role": "user", 
                 "content": [
                    { "type": "input_text", "text": "what's in this image?" },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base_64_img}", #Creating url that says its a jpeg (could change if its img/png or jpg)
                },
                ],
                }
            ], #possible tweak this to look at objects instead of JSON format
            # temperature=0.7, #Lower numbers more predictable, higher gives more creativity
            # reasoning_effort="high",) 
            )
            print(completion.output_text)
        else:
            print("Failure")


if __name__ == "__main__":
    main()
