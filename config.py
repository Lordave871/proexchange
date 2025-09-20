import os
from dotenv import load_dotenv


load_dotenv()
class Config:
    DATABASE_NAME=os.getenv('DATABASE_NAME')
    DATABASE_HOST=os.getenv('DATABASE_HOST')
    DATABASE_USER=os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
    DATABASE_PORT=int(os.getenv('DATABASE_PORT'))
    AT_API_KEY=os.getenv('AT_API_KEY')


    SECRET_KEY=os.getenv('SECRET_KEY','default_secrete_key')
    
    
    
