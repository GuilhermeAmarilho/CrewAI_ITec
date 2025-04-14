#!/usr/bin/env python
import sys
from crew_itec.crew import CrewItec

def run(topic):
    inputs = {
        'topic': topic
    }    
    try:
        CrewItec().crew().kickoff(inputs=inputs)        
    except Exception as e:
        raise Exception(f"Ocorreu um erro ao executar o Crew: {e}")
