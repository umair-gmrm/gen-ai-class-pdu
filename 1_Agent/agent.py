
from pydantic_ai import Agent
from pydantic_ai.models.groq import GroqModel
from pydantic_ai.providers.groq import GroqProvider

model = GroqModel(
    'llama-3.3-70b-versatile', provider=GroqProvider(
        api_key='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')
)


agent = Agent(model)

@agent.system_prompt
def system_prompt():
    return '''
    You are a helpful travel support agent. 
    Answer the user's questions about travel, flights,
    hotels, and related topics in a friendly and informative manner.
    You know only Sinhala, just response in Sinhala everytime'''


def get_agent_response(message: str , prev_messages:list = []):

    memory_limit  = 5

    if len(prev_messages) > memory_limit:
        prev_messages = prev_messages[-memory_limit:]

    agent_message = ""
    
    for msg in prev_messages:
        agent_message += f"User: {msg['user']}\nAgent: {msg['agent']}\n"
    
    agent_message += f"User: {message}\nAgent:"
    

    response = agent.run_sync(agent_message)

    return {
        "user": message,
        "agent": response.output
    }


if __name__ == "__main__":
    # Example usage
    user_message = "What is my name?"
    response = get_agent_response(user_message , [{"user": "I'm Umair", "agent": "Hello Umair, how can I assist you today?"}])
    print("User:", response["user"])
    print("Agent:", response["agent"])