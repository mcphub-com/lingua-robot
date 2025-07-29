import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/rokish/api/lingua-robot'

mcp = FastMCP('lingua-robot')

@mcp.tool()
def entry(entry: Annotated[str, Field(description='Entry (word, phrasal verb etc., case-sensitive)')]) -> dict: 
    '''Retrieve data related to the specified entry, such as word or phrasal verb. The data includes meanings, pronunciations, lemmas, normalized lemmas etc.'''
    url = 'https://lingua-robot.p.rapidapi.com/language/v1/entries/en/example'
    headers = {'x-rapidapi-host': 'lingua-robot.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'entry': entry,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
