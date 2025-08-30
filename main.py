from mcp.server.fastmcp import FastMCP
import time
import logging

mcp = FastMCP("add_integers")
@mcp.tool()

def add(a: int, b: int) -> int:
    '''
    ADD TWO INTEGERS AND RETURN THE RESULT.

    Args:

       a: First integer.
       b: Second integer.

    Returns:
      The sum of the a  and b.
    '''
    return a + b

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

def long_process(steps: int) -> str:
    '''
    Simulates a long-running process.
    '''
    for i in range(steps):
        print(f"Processing step {i + 1} of {steps}")
        time.sleep(0.1)
    return "Process complete!"

class MCPError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message
        super().__init__(f"[{code}] {message}")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='mcp_server.log',  # This line tells it to create and use a file
    filemode='a'  # Use 'a' to append to the file on each run, or 'w' to overwrite it
)

logger = logging.getLogger(__name__)


if __name__ == "__main__":
    mcp.run(transport='stdio')
