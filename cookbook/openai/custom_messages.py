from phi.assistant import Assistant
from phi.llm.openai import OpenAIChat

assistant = Assistant(
    llm=OpenAIChat(model="gpt-4-turbo-preview"), debug_mode=True, system_prompt=None, format_messages=False
)
assistant.print_response(
    [
        {"role": "system", "content": "Reply with haikus."},
        {"role": "user", "content": "What is the capital of France?"},
    ],
)
