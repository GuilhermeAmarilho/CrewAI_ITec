from crewai import Crew, Task, LLM
from app.agents.api_search import search_Agent
from app.agents.api_write import writer_Agent
import os
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    provider="gemini",
    model="gemini-pro",
    api_key=os.getenv("LITELLM_API_KEY"),
    api_base=os.getenv("LITELLM_API_BASE")
)


# Se eu avisar no env que o LLM é o gemini, não precisa configurar manualmente
def create_crew(topic: str) -> Crew:
    search_task = Task(
        description=f"Buscar informações na Wikipedia sobre o tema: {topic}",
        expected_output="Texto informativo com base na Wikipedia.",
        agent=search_Agent()
    )
    write_task = Task(
        description="Escrever artigo de no mínimo 300 palavras baseado nas informações coletadas.",
        expected_output="Artigo com introdução, desenvolvimento e conclusão.",
        agent=writer_Agent(),
        context=[search_task]
    )
    crew = Crew(
        agents=[search_Agent(), writer_Agent()],
        tasks=[search_task, write_task],
        verbose=True,
        llm=llm
    )
    return crew