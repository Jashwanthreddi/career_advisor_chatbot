import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from current directory
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")
