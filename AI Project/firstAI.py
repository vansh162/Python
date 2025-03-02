# Creating an GEMINI based AI in terminal. 
import google.generativeai as ai
ai.configure(api_key="AIzaSyCHC8x_nJxGjKyCfxouRgT2KcvyTBxkvfM")
model = ai.GenerativeModel("gemini-2.0-flash")
promty = input("Enter prompt: ")
response = model.generate_content(promty, stream=True)
for chunk in response:
    print(chunk.text)