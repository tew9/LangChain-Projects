from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str):
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    template = """given the full name {name_of_person} I want you to find the link to their twitter profile page, 
                and extract the username from it. 
                Your answer should only contain only the person's username."""

    tool_for_agent = [
        Tool(
            name="Extract username from the url",
            func=get_profile_url,
            description="Useful for when you need to get Twitter information online",
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
    twitter_user_name = agent.run(prompt_template.format_prompt(name_of_person=name))
    return twitter_user_name
