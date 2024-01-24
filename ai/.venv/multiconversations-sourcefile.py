import os
import google.generativeai as genai
from IPython.display import Markdown
import textwrap
import constants

os.environ["API_KEY"] = constants.API_KEY

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-pro')

file1 = open("sourcefile.java", "r")
source = file1.read()

messages = [
    {'role':'user',
     'parts': [source]}
]
response = model.generate_content(messages)

messages = [
    {'role':'model',
     'parts': [response.text]}
]

messages.append({'role':'user',
                 'parts':["Provide a summary of the source code?"]})

response = model.generate_content(messages)

print(response.text)