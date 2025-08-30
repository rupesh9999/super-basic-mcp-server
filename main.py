from mcp.server.fastmcp import FastMCP

mcp = FastMCP("add_integers")

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"code={code}, message={message}")
@mcp.tool()
def divide(a: int, b: int) -> float:
    '''
    ADD TWO INTEGERS AND RETURN THE RESULT.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division.
    '''
    if b == 0:
        raise MCPError(code=400, message="Division by zero is not allowed.")
    return a / b