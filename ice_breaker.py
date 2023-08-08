import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_linkedin_profile

# from third_parties.twitter import scrape_user_tweets
from third_parties.twitter_with_stubs import scrape_user_tweets

from agent.linkedlookup_agent import lookup
from agent.twitterlookup_agent import lookup as twitter_username_lookup
from output_parser import person_intel_parser


def ice_break(name: str) -> tuple[person_intel_parser, str]:
    # get the linkedin profile url from the linkedin lookup agent
    linkedin_profile_url = lookup(name=name)
    """After testing I am not going to be calling proxycurl api to limit my free api calls
    am calling the gist saved information in the github(gist.github.com)
    If you want to change it visit the third_parties/linkedin.py and change the url to the linkedin profile url"""
    linked_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)

    twitter_username = twitter_username_lookup(name=name)
    tweets = scrape_user_tweets(username=twitter_username, num_tweets=1)

    # Create the summary template
    summary_template = """
        given the Linkedin information {linked_information} and a twitter information {twitter_information} about a person, I want you to create:
        1. a short summary
        2. two interesting facts about them
        \n{format_instructions}
    """

    # Instantiate the promptemplate which takes any argurment for the template and the template
    summary_prompt_template = PromptTemplate(
        input_variables=["linked_information", "twitter_information"],
        template=summary_template,
        partial_variables={
            "format_instructions": person_intel_parser.get_format_instructions()
        },
    )

    # Instantiate the chat model, with temperature determining how creative the model can be and model name
    openapi = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    # instantiate the chain(the linker which links the chat model with our prompt)
    chain = LLMChain(llm=openapi, prompt=summary_prompt_template)

    result = chain.run(linked_information=linked_data, twitter_information=tweets)

    return (person_intel_parser.parse(result), linked_data.get("profile_pic_url"))


# if __name__ == "__main__":
#     print("Hello langChain!\n")

#     name = "Eden Marco Udemy"

#     print(ice_break(name=name))
