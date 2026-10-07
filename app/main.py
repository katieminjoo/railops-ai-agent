import os
from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from rail_data import get_trains
import json

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

# response = client.responses.parse(
#     model = 'gpt-5.4-mini',
#     input = 'The 08:30 train from Woking to London has been cancelled. What should the passenger do?',
#     text_format= Decision
# )

# decision = response.output_parsed

# print(decision)
# print('Status :', decision.status)
# print('Action :', decision.recommended_action)
# print('Reason :', decision.reason)

tools = [
    {
        "type" : "function",
        "name" : "get_trains",
        "description" : "Get live train services from a UK railway station to a destination.",
        "parameters" : {
            "type" : "object",
            "properties" : {
                "crs": {
                    "type" : "string"
                },
                "destination_name" : {
                    "type" : "string"
                }
            },
            "required" : ["crs", "destination_name"]
        }
    }
]

response = client.responses.create(
    model = "gpt-5.4-mini",
    input = "What are the next trains from Woking to London Waterloo?",
    tools = tools
)

tool_call = response.output[0]

arguments_json = tool_call.arguments
arguments = json.loads(arguments_json)

crs = arguments['crs']
destination = arguments['destination_name']

train_results = get_trains(crs, destination)
# print(train_results)

call_id = tool_call.call_id
train_results_json = json.dumps(train_results)

# Back to LLM
final_response = client.responses.create(
    model = 'gpt-5.4-mini',
    previous_response_id= response.id,
    input = [
        {
            'type' : 'function_call_output',
            'call_id' : call_id,
            'output' : train_results_json,
        }
    ],
    tools = tools
)

print(final_response.output_text)