This is basicaly a program that connect discord api with LLM api to make a chatbot.

I'm using mixtral model with free api from groq.com.

The intteraction with AI is in separate file so I was also able to make it accesible from web (when I needed AI withou two-step verification with mobile).


To run this you first need to make your own discrd bot from their website.

Activate s virtual enviroment with .\myenv\Scripts\activate

Assign values to enviromental variables GROQ_API_KEY (AI api key) and DISC_API_KEY (discord api key)

then run di3.py. 

You will need to invite the discord bot to your discord server to acces it - this can be done from the discord website.
