import os
import google.generativeai as genai
import constants

os.environ["API_KEY"] = constants.API_KEY

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-pro')
## Use GenerativeModel.generate_content to have the model complete some initial text.

response = model.generate_content("The opposite of hot is")
print(response.text)  # cold.

## Use GenerativeModel.start_chat to have a discussion with a model.

chat = model.start_chat()
response = chat.send_message('Hello, what should I have for dinner?')
print(response.text) #  'Here are some suggestions...'

response = chat.send_message("How do I cook the first one?")
print(response.text) #  'Here is the recipe...'