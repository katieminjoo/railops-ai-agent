import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

class Decision(BaseModel):
    status : str
    recommended_action : str
    reason : str

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

if api_key:
    print('API key loaded successfully!')
else:
    print('API key not found.')

client = OpenAI(api_key = api_key)

response = client.responses.parse(
    model = 'gpt-5.4-mini',
    input = 'The 08:30 train from Woking to London has been cancelled. What should the passenger do?',
    text_format= Decision
)

decision = response.output_parsed

print(decision)
print('Status :', decision.status)
print('Action :', decision.recommended_action)
print('Reason :', decision.reason)