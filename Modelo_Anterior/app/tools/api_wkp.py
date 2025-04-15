# from crewai import BaseTool
from crewai.tools import BaseTool
import requests

class WikiSearch(BaseTool):
    # Por causa do pydantic, tem que colocar o tipo de variavel como no C
    name: str = "Wiki Search"  
    description: str = "Busca um artigo na Wikipedia e retorna o conteúdo sobre ele"  
    # Ajuda o llm a entender o contexto da aplicação
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