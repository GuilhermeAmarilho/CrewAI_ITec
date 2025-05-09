from crewai import Agent, Crew, Process, Task # type: ignore
from crewai.project import CrewBase, agent, crew, task # type: ignore

@CrewBase
class Crew():
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'
    # Configura os agents usando a engenharia de prompt passada no config, tanto os agentes quanto as tasks
    @agent
    def reader(self) -> Agent:
        return Agent(
            config=self.agents_config['reader'],
            verbose=True
        )
    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'],
            verbose=True
        )
    @task
    def reader_task(self) -> Task:
        return Task(
            config=self.tasks_config['reader_task'],
        )
    @task
    def writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['writer_task'],
            context=[self.reader_task()],
            output_file='results/report.txt'
        )
    @crew
    def crew(self) -> Crew:
        return Crew(
            # É criado automáticamente por causa do @agent
            agents=self.agents,
            # É criado automáticamente por causa do @task
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
