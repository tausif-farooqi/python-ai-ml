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
        response = model.generate_text(
            prompt=f"Translate the following English text to Spanish:\n\n{english_input}",
            temperature=0.2,
            max_output_tokens=100
        )

        return response.text.strip()
    except Exception as e:
        print(f"Error during translation: {e}")
        return None
    
def main():
    english_text = "Hello, how are you?"
    print(f"Translating: {english_text}")
    spanish_translation = translate_to_spanish(english_text)
    if spanish_translation:
        print(f"Spanish Translation: {spanish_translation}")

    else:
        print("Translation failed.")

    time.sleep(1)  # To avoid hitting rate limits

if __name__ == "__main__":
    main()    
