from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to get me a link to their linkedin profile. 
                  Your answer should only contain only the URL and make sure it looks like https://www.linkedin.com/in/
                """
    tool_for_agent = [
        Tool(
            name="Crawl Google 4 Linkedin profile page",
            func=get_profile_url,
            description="Useful for getting Linkedin information online",
        )
    ]

    agent = initialize_agent(
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        tools=tool_for_agent,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    linkedlin_profile_url = agent.run(
        prompt_template.format_prompt(name_of_person=name)
    )
    return linkedlin_profile_url
