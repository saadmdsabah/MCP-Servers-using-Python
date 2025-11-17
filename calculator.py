from fastmcp import FastMCP

mcp = FastMCP(name="calculator")


@mcp.tool(
    name="multiplication",
    description="the product of the two integer numbers",
    tags={"maths", "multiplication", "arithmetics"},
)
def multiply(x: int, y: int) -> int:
    """
    multiply to integer numbers
    args: a (int): the first number
          b (int): the second number
    returns: int: the product of the two numbers
    """
    return x * y


@mcp.tool(
    name="addition",
    description="the sum of the two integer numbers",
    tags={"maths", "addition", "arithmetics"},
)
def add(x: int, y: int) -> int:
    """
    add two integer numbers
    args: x (int): the first number
          y (int): the second number
    returns: int: the sum of the two numbers
    """
    return x + y


@mcp.tool(
    name="subtraction",
    description="the difference of the two integer numbers",
    tags={"maths", "subtraction", "arithmetics"},
)
def subtract(x: int, y: int) -> int:
    """
    subtract two integer numbers
    args: x (int): the first number
          y (int): the second number
    returns: int: the difference of the two numbers
    """
    return x - y


@mcp.tool(
    name="division",
    description="the quotient of the two integer numbers",
    tags={"maths", "division", "arithmetics"},
)
def divide(x: int, y: int):
    """
    Divide two integer numbers. If the denominator is zero, returns an error message.
    Args:
        x (int): The numerator.
        y (int): The denominator.
    Returns:
        dict: {"result": float} if y != 0, otherwise {"error": "Division by zero is not allowed."}
    """
    if y == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": x / y}


if __name__ == "__main__":
    mcp.run()
