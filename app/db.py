import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pymongo import MongoClient
import redis

load_dotenv()

pg_engine = create_engine(os.environ['DATABASE_URL'])
mongo_db = MongoClient(os.environ['MONGO_URL']) [os.environ.get('MONGO', 'opspilot')]
redis_client = redis.Redis.from_url(
    os.environ['REDIS_URL'],
    decode_response=True
    )

