from app.crew import create_crew

def get_artigo(topic: str):
    crew = create_crew(topic)
    result = crew.kickoff()
    return {"artigo": result}