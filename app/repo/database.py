"""Init database connection"""
# -*- coding: utf-8 -*-
from databases import Database
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: load config from .env
DATABASE_URL = "postgresql+asyncpg://minhnguyen:@localhost/wallet-assets"
db = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL)

metadata = MetaData()
Base = declarative_base(metadata=metadata)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
