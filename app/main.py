# -*- coding: utf-8 -*-
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.graphql import schema
from app.repo.database import db


@asynccontextmanager
# pylint: disable=unused-argument
async def lifespan(fastapp: FastAPI):
    """
    Init database connection.
    """
    await db.connect()
    print('=====>lifespan: Connect to database')
    yield
    await db.disconnect()

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(schema.GraphQL_App, prefix="/graphql", tags=["graphql"])


@app.get("/")
async def hello_world() -> dict:
    """
    Returns a dictionary with a greeting message.

    Returns:
        dict: A dictionary with the greeting message.
    """
    return {"Hello": "Worlds"}
