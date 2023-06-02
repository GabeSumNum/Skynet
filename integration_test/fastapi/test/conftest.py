import os
import time

import httpx
import pytest
import pytest_asyncio

url = os.getenv("TEST_URL", default="http://localhost:5000")


@pytest.fixture(scope="session", autouse=True)
def fixture():
    time.sleep(30)


@pytest_asyncio.fixture
async def client():
    async with httpx.AsyncClient(base_url=url) as client:
        print(url)
        yield client


@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.text == '{"status":"up"}'
