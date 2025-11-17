import requests
from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Weather Tool")


@app.get("/")
def home():
    return {"message": "Hello World"}


@app.get("/weather/{city}")
def getWeather(city: str):
    """
    name: "get_weather"
    description: "Get current weather information for the specified city."
    tags: {"weather", "city", "forecast", "temperature", "conditions"}
    Args:
        city (str): The name of the city to query the weather for.
    Returns:
        dict: The current weather details for the city in JSON format.
    """
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()


mcp = FastApiMCP(app)
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8080)
