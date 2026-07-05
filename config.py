import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# LLM Model
MODEL_NAME = os.getenv("MODEL_NAME")

# Vector Database Path
CHROMA_DB_PATH = os.getenv("CHROMA_DB_PATH")