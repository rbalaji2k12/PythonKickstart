import os
import google.generativeai as genai
from IPython.display import Markdown
import textwrap
import constants

os.environ["API_KEY"] = constants.API_KEY

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-pro')

messages = [
    {'role':'user',
     'parts': ["Briefly explain how a computer works to a young child."]}
]
response = model.generate_content(messages)

def to_markdown(text):
  text = text.replace('•', '  *')
  print(text)
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

to_markdown(response.text)

messages.append({'role':'model',
                 'parts':[response.text]})

messages.append({'role':'user',
                 'parts':["Okay, how about a more detailed explanation to a high school student?"]})

response = model.generate_content(messages)

to_markdown(response.text)