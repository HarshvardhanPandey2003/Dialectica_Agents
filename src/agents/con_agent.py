from crewai import Agent

class ConAgent:
    def __init__(self, llm):
        self.agent = Agent(
            role='Con Debater',
            goal='Present strong arguments opposing the given position',
            backstory='''You are a skilled debater who excels at identifying 
            weaknesses in arguments and presenting compelling counter-arguments. 
            You challenge ideas with logic, evidence, and critical thinking.''',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def get_agent(self):
        return self.agent
