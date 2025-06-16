import google.generativeai as genai
import configparser
import os

def read_api_key():
    config = configparser.ConfigParser()
    try:
        config.read("keys.txt")
    except Exception as e:
        raise FileNotFoundError(f"Config file 'keys.txt. not found. Error: {e}")
    
    return config['API_Keys']['GEMINI_API_KEY']

api_key = read_api_key();

genai.configure(api_key=api_key)

# Choose a model
model = genai.GenerativeModel('gemini-2.0-flash')

# Send a simple text prompt
prompt = "Give me a 100 word summary of the book 'The Hitchhiker's Guide to the Galaxy."
response = model.generate_content(prompt)

# Print the model's response
print(response.text)