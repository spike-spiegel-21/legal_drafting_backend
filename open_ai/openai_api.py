import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

class OpenAI:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")

    def get_response(self, message):
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            temperature=1.0,
            max_tokens=350,
            messages=[
                {"role": "system", "content": "You are the narrator who will write professionally about the experience"},
                {"role": "user", "content": "Write the following in 5-7 detailed points.\n"+message}
            ]
        )
        return str(completion.choices[0].message.content)

#print(type(OpenAI().get_response("I have taken the cultfit play pass member ship which charged me around 10000 rs for 3 months. In this memebership I was allowed to play in any of their play centers. At the time of memebership I was using their service for sector 23 which have 3 facaliteis of sports (incl. Badminton, Table Tennis and Lawn Tennis) After having there for around 3 weeks they are shutting down this place due to some reason. When I sad them for the refund the remaining amount they said you can use the service that is available in othr centere which is very far from my current residence. They said that the amound is not refundable.")))
