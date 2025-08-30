from mcp.server.fastmcp import FastMCP

mcp = FastMCP("add_integers")

@mcp.tool()
def add(a: int, b: int) -> int:
    '''
    ADD TWO INTEGERS AND RETURN THE RESULT.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum of the a and b.
    '''
    return a + b

if __name__ == "__main__":
    mcp.run(transport='stdio')
