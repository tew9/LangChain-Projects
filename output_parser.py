from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):
    summary: str = Field(..., description="The summary of the person")
    facts: List[str] = Field(..., description="The Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        ..., description="The topics of interest of the person"
    )
    ice_breakers: List[str] = Field(
        ..., description="Create ice-breakers to start a conversation with the person"
    )

    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)
