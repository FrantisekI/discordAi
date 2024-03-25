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
                #"content": "you are Czech speaking, nice and friendly chat bot, named Patrice and Czech speaking"
                "content": "jsi česky mluvící, milý a přátelský chat bot, jménem Patrice"
            },
            {
                "role": "user",
                "content": message
            }
        ],
        model="mixtral-8x7b-32768",
        # Controls randomness: lowering results in less random completions.
        # As the temperature approaches zero, the model will become deterministic
        # and repetitive.
        temperature=0.5,

        # The maximum number of tokens to generate. Requests can use up to
        # 32,768 tokens shared between prompt and completion.
        max_tokens=1024,

        # Controls diversity via nucleus sampling: 0.5 means half of all
        # likelihood-weighted options are considered.
        top_p=1,

        # A stop sequence is a predefined or user-specified text string that
        # signals an AI to stop generating content, ensuring its responses
        # remain focused and concise. Examples include punctuation marks and
        # markers like "[end]".
        stop=None,

        # If set, partial message deltas will be sent.
        stream=False,
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":


    print(respondToDiscordMessage("kdo jsi?"))