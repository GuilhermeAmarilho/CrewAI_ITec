import sys
from crew import Crew

def run():
    inputs = {
        'topic': 'Teclado gamer com led'
    }    
    try:
        Crew().crew().kickoff(inputs=inputs)        
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar o Crew: {e}")