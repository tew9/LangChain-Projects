import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

from agent.linkedlookup_agent import lookup

if __name__ == "__main__":
    print("Hello langChain!\n")

    # get the linkedin profile url from the linkedin lookup agent
    linkedin_profile_url = lookup(name="Eden Marco Udemy")

    # Create the summary template
    summary_template = """
        given the Linkedin information, {information} about a person, I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    # Instantiate the promptemplate which takes any argurment for the template and the template
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # Instantiate the chat model, with temperature determining how creative the model can be and model name
    openapi = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # instantiate the chain(the linker which links the chat model with our prompt)
    chain = LLMChain(llm=openapi, prompt=summary_prompt_template)

    """After testing I am not calling proxycurl api to limit my free api calls
    am calling the gist saved information in the github(gist.github.com)"""
    linked_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    print(chain.run(information=linked_data))
