import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SERP_API_KEY = os.getenv('API_KEY_SERP', 'your_serp_api_key')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your_openai_secret_key')

config = Config()
