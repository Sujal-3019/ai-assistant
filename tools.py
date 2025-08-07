import logging
from livekit.agents import function_tool, RunContext
import requests
from langchain_community.tools import DuckDuckGoSearchRun
import webbrowser

@function_tool()
async def get_weather(
        context: RunContext,
        city: str, ctx: RunContext
        ) -> str:
        """
        Get the current weather for a given city.
        """
        try:
            response = requests.get(
                  f"https://wttr.in/{city}?format=3")
            if response.status_code == 200:
                  logging.info(f"Weather in {city}: {response.text.strip()}")
                  return response.text.strip()
            else:
                  logging.error(f"Failed to get weather for {city}: {response.status_code}")
                  return f"Could not retrieve weather for {city}."
        except Exception as e:
            logging.error(f"Error retrieving weather for {city}: {str(e)}")
            return f"An error occurred while retrieving weather for {city}."

@function_tool()        
async def search_web(
        context: RunContext,
        query: str, ctx: RunContext
        ) -> str:
        """       
        Search the web for a given query using DuckDuckGo.
        """
        try:
            results = DuckDuckGoSearchRun().run(tool_input=query)
            logging.info(f"Search results for '{query}': {results}")
            return results
        except Exception as e:
            logging.error(f"Error searching the web for '{query}': {str(e)}")
            return f"An error occurred while searching the web for '{query}'."
@function_tool()        
async def open_website(url: str) -> str:
    try:
        webbrowser.open(url)
        return f"Opening {url}."
    except Exception as e:
        return f"Failed to open {url}: {e}"