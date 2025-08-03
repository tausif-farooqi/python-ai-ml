# Run from the root of the project
# python -m simple_gemini_examples.english_spanish_translator

import google.generativeai as genai
import os
import time
import utils.api_keys as keys

api_key = keys.read_gemini_api_key()
genai.configure(api_key=api_key)
# Choose a model
model = genai.GenerativeModel('gemini-2.0-flash')

def translate_to_spanish(english_input):
    """
    Translates English text to Spanish using the Gemini model.
    
    Args:
        english_input (str): The English text to translate.
    
    Returns:
        str: The translated Spanish text.
    """
    try:
        prompt=f"Translate the following English text to Spanish:\n\n{english_input}"
        response = model.generate_content(prompt)

        return response.text.strip()
    except Exception as e:
        print(f"Error during translation: {e}")
        return None
    
def main():
    print("\n--- English to Spanish Translator ---")
    print("Type 'exit' to quit.")

    # Main loop for user input
    while True:
        user_input = input("\nEnter English text to translate: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting translator. Goodbye!")
            break

        if not user_input:
            print("Please enter some text.")
            continue

        print(f"Translating: '{user_input}'")

        spanish_translation = translate_to_spanish(user_input)
        if spanish_translation:
            print(f"Spanish Translation: {spanish_translation}")

        else:
            print("Translation failed.")

        time.sleep(1)  # To avoid hitting rate limits

if __name__ == "__main__":
    main()    
