# -*- coding: utf-8 -*-
# pylint: disable=unused-argument
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel

from app.graphql import GraphQLRoute
from app.repo.database import engine, init_models

os.environ['TZ'] = 'UTC'


@asynccontextmanager
async def lifespan(fastapp: FastAPI):
    """
    Init database connection.
    """
    # TODO do something on life-cycle
    # async with engine.begin() as conn:
    #     await conn.run_sync(SQLModel.metadata.create_all)
    await init_models()
    yield
    # await db.disconnect()

fastapiApp = FastAPI(lifespan=lifespan)
fastapiApp.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
fastapiApp.include_router(GraphQLRoute, prefix="/graphql", tags=["graphql"])


@fastapiApp.get("/")
async def hello_world() -> dict:
    """
    Returns a dictionary with a greeting message.

    Returns:
        dict: A dictionary with the greeting message.
    """
    return {"Hello": "Worlds"}
