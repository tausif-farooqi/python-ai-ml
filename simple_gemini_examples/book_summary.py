# Run from the root of the project
# python -m simple_gemini_examples.book_summary

import google.generativeai as genai
import os
import time
import utils.api_keys as keys

api_key = keys.read_gemini_api_key();

genai.configure(api_key=api_key)

# Choose a model
model = genai.GenerativeModel('gemini-2.0-flash')

# Send a simple text prompt
#prompt = "Give me a 100 word summary of the book 'The drama llama'."
#response = model.generate_content(prompt)

# Print the model's response
#print(response.text)

# This script uses the Google Generative AI API to summarize a book.
def book_summary(book_name):
    """
    Returns a 100 word summary of a book using the Gemini model.
    
    Args:
        book_name (str): The book name to summarize.
    
    Returns:
        str: The book summary.
    """
               
    print(f"Generating summary for: '{book_name}'")

    # Send the book name to the model for summarization
    # The prompt is designed to ask for a 100-word summary of the book
    prompt = f"Give me a 100 word summary of the book '{book_name}'."
    response = model.generate_content(prompt)  
    
    return response.text.strip()

def main():
    print("\n--- Book Summarizer ---")
    print("Type 'exit' to quit.")

    # Main loop for user input
    while True:
        user_input = input("\nEnter the book name to summarize: ").strip()

        if user_input.lower() == 'exit':
            print("Exiting. Goodbye!")
            break

        if not user_input:
            print("Please a valid book name.")
            continue

        response = book_summary(user_input)        

        if response:
            print(f"The book summary: {response}")

        else:
            print("Translation failed.")

        time.sleep(1)  # To avoid hitting rate limits    


if __name__ == "__main__":
    main()
