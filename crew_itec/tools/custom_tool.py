from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests

class WikiSearchInput(BaseModel):
    topic: str = Field(..., description="Artigo que vai ser pesquisado na Wikipedia.")

class WikiSearch(BaseTool):
    name: str = "Wiki Search"
    description: str = "Busca um artigo na Wikipedia e retorna o conteúdo sobre ele."
    args_schema: Type[BaseModel] = WikiSearchInput

    def _run(self, topic: str) -> str:
        url = "https://pt.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "prop": "extracts",
            "exlimit": 1,
            "explaintext": 1,
            "titles": topic,
            "format": "json",
            "utf8": 1,
            "redirects": 1
        }
        response = requests.get(url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        return page.get("extract", "Nenhuma informação encontrada.")