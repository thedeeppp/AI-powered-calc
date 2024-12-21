import os
from dotenv import load_dotenv

load_dotenv()

# Configuration with environment variables and fallbacks
SERVER_URL = os.getenv('HOST', '0.0.0.0')  # Changed from localhost for container compatibility
PORT = int(os.getenv('PORT', 8900))
ENV = os.getenv('ENV', 'dev')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_API_KEY and ENV == 'prod':
    raise ValueError("GEMINI_API_KEY must be set in production environment")