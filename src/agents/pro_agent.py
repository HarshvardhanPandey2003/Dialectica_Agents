from crewai import Agent

class ProAgent:
    def __init__(self, llm):
        self.agent = Agent(
            role='Pro Debater',
            goal='Present strong arguments supporting the given position',
            backstory='''You are an experienced debater who excels at finding 
            compelling evidence and logical arguments to support your assigned position. 
            You present clear, well-structured arguments with evidence.''',
            verbose=True,
            allow_delegation=False,
            llm=llm
        )
    
    def get_agent(self):
        return self.agent
