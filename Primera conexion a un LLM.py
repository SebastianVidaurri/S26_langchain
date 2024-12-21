import os
from dotenv import load_dotenv, find_dotenv
#busca y carga el archivo .env
_ = load_dotenv(find_dotenv())

#cargamos chatgroq
from langchain_groq import ChatGroq

#instanciamos los modelos de llm
#TODO: Cambiar por una funcion
llamaChatModel = ChatGroq(
    model="llama3-70b-8192"
)

mistralChatModel = ChatGroq(
    model="mixtral-8x7b-32768"
)

#creamos un Chatprompt template
from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an {profession} expert on {topic}."),
        ("human", "Hello, Mr. {profession}, can you please answer a question?"),
        ("ai", "Sure!"),
        ("human", "{user_input}"),
    ]
)

messages = chat_template.format_messages(
    profession="Historian",
    topic="The Kennedy family",
    #la siguiente linea es el input del usuario
    user_input="How many grandchildren had Joseph P. Kennedy?"
)

response = llamaChatModel.invoke(messages)

print(response)