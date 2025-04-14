from crewai import Agent
from app.tools.api_wkp import WikiSearch

# Esse agente é responsavel por pegar os dados da wikipedia
# Enquanto a tool é como a lupa que serve para enxergar, esse agente é a pessoa que usa a lupa para ler
def search_Agent():
    return Agent(
        role="Leitor de artigos",
        goal="Colete informações relevantes na Wikipedia sobre o tema.",
        backstory="Você é o responsável por buscar informações confiáveis diretamente da Wikipedia. Sua tarefa é ser a principal fonte de dados brutos para a criação dos artigos. Portanto, você deve garantir que o conteúdo extraído seja fiel e relevante ao tema proposto. Você não deve recorrer a dados externos ou inventados.",
        tools=[WikiSearch()],
        verbose=True
    )