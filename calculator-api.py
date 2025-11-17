from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(title="Calculator Tool API")


@app.get("/")
def home():
    return "Hello World!"


@app.post("/multiply")
def multiply(a: int, b: int):
    """
    Multiply two integer numbers.
    Args:
        a (int): the first number
        b (int): the second number
    Returns:
        int: the product of the two numbers
    """
    return {"result": a * b}


@app.post("/add")
def add(a: int, b: int):
    """
    Add two integer numbers.
    Args:
        a (int): the first number
        b (int): the second number
    Returns:
        int: the sum of the two numbers
    """
    return {"result": a + b}


@app.post("/subtract")
def subtract(a: int, b: int):
    """
    Subtract two integer numbers.
    Args:
        a (int): the first number
        b (int): the second number
    Returns:
        int: the difference of the two numbers
    """
    return {"result": a - b}


@app.post("/divide")
def divide(a: int, b: int):
    """
    Divide two integer numbers. If the denominator is zero, returns an error message.
    Args:
        a (int): The numerator.
        b (int): The denominator.
    Returns:
        dict: {"result": float} if b != 0, otherwise {"error": "Division by zero is not allowed."}
    """
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}


mcp = FastApiMCP(app, name="Calculator Tool API")
mcp.mount_http()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
