import os # Import the os module
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv module
from urllib.parse import quote
from sqlalchemy import create_engine, MetaData 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv() # Load environment variables from the .env file


DATABASE_URL = os.getenv("DATABASE_URL") # Get the DATABASE_URL environment variable
engine = create_engine(DATABASE_URL) # Create a SQLAlchemy engine
# What is an sql alchemy engine ?
# An Engine is a factory for Connection objects. It encapsulates a connection pool that minimizes the cost of connecting to the database by reusing existing connections and provides a consistent API for working with transactions.

metadata = MetaData() # Create a SQLAlchemy MetaData object

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # Create a SQLAlchemy sessionmaker object

Base = declarative_base() # Create a SQLAlchemy declarative base object