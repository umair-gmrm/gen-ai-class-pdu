
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider
from typing import Literal , Optional


from pydantic import BaseModel , Field
from dataclasses import dataclass



model = GroqModel(
    'llama-3.3-70b-versatile', provider=GroqProvider(
        api_key='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')
)


class DetermineSubjectOutput(BaseModel):
    subject: Optional[Literal["english", "mathematics", "science"]] = Field(description="Subject of the query", examples=["english", "mathematics", "science"])



determine_subject_agent = Agent(model , output_type=DetermineSubjectOutput,)

@determine_subject_agent.system_prompt
def system_prompt():
    return ''' You are a subject determination agent.
    Given a query, determine the subject of the query. 
    subjects must be one of the following: english, mathematics, science.

    you should return the subject of the query as a string.
    If the query is about English, return "english".
    If the query is about Mathematics, return "mathematics".
    If the query is about Science, return "science".
    If the query is about any other subject, return None.
    If the query does not belong to any of these subjects, return None.'''





def determine_subject_agent_run_sync(query: str) -> str :
    """
    Run the determine_subject_agent synchronously with the provided query.
    """

    print(f"Running determine_subject_agent with query: {query}")

    response = determine_subject_agent.run_sync(query)

  

    return response.output.subject


if __name__ == "__main__":
    # Example usage
    user_message = "What is the tense of the verb in the sentence 'She is running'?"
    
    response = determine_subject_agent_run_sync(user_message)

    print(response)
