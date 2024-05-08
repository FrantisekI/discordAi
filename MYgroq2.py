import os
from dotenv import load_dotenv
from groq import Groq


load_dotenv()

def respondToDiscordMessage(message):
        
    Groq_key = os.environ.get("GROQ_API_KEY")
    Gclient = Groq(
        api_key=Groq_key,
    )

    chat_completion = Gclient.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "respond"
                #"content": "jsi česky mluvící, milý a přátelský chat bot ženského pohlaví, jménem Patrice"
            },
            {
                "role": "user",
                "content": message
            }
        ],
        model="mixtral-8x7b-32768", 
        #model='gemma-7b-it',



        temperature=0.5,


        max_tokens=2048,

        top_p=1,


        stop=None,


        stream=False,
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":


    print(respondToDiscordMessage("kdo jsi?"))