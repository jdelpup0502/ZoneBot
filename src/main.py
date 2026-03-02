import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Warning: OPENAI_API_KEY not found in .env file.")
    else:
        print("OPENAI_API_KEY loaded successfully.")

    print("Welcome to ZoneBot! 🏗️🗺️")
    print("Project structure initialized. Ready for development.")

if __name__ == "__main__":
    main()
