import configparser

def read_gemini_api_key():
    config = configparser.ConfigParser()
    try:
        config.read("keys.txt")
    except Exception as e:
        raise FileNotFoundError(f"Config file 'keys.txt. not found. Error: {e}")
    
    return config['API_Keys']['GEMINI_API_KEY']