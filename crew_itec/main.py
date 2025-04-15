import sys
from crew_itec.crew import CrewItec

def run():
    inputs = {
        'topic': 'Teclado gamer com led'
    }    
    try:
        CrewItec().crew().kickoff(inputs=inputs)        
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar o Crew: {e}")