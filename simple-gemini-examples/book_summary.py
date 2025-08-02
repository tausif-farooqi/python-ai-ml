import google.generativeai as genai
import os
import utils.api_keys as keys

api_key = keys.read_gemini_api_key();

genai.configure(api_key=api_key)

# Choose a model
model = genai.GenerativeModel('gemini-2.0-flash')

# Send a simple text prompt
prompt = "Give me a 100 word summary of the book 'The Hitchhiker's Guide to the Galaxy'."
response = model.generate_content(prompt)

# Print the model's response
print(response.text)