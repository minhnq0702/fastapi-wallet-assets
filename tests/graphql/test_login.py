import pytest
from fastapi.testclient import TestClient

from app.graphql import schema
from app.main import fastapiApp


@pytest.mark.asyncio
async def test_login():
    client = TestClient(fastapiApp)
    query = """
        mutation Login {
            login(payload: { username: "testtest", password: "teststest" }) {
                ... on LoginFailType {
                msg
                }
                ... on LoginSuccessType {
                user {
                    id
                    username
                    password
                    email
                    createdDate
                    updatedDate
                } 
                token
                }
            }
        }
    """
    # res = client.post("/graphql", json={
    #     "operationName": "Login",
    #     "query": query
    # })
    result = await schema._schema.execute(query=query)
    assert result.errors is None
    print("hahaha===>", result)
    assert isinstance(result.data["login"], dict)
    # print("==>", res.content)
    # assert 0 == 1
