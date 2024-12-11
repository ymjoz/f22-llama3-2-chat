from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = OllamaLLM(model="llama3.2", temperature=0)

def get_chat_response(text: str, memory):
    conversation = ConversationChain(llm=llm, memory=memory)
    return conversation.predict(input=text)

# memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("台灣的地理中心碑在那裡？", memory))
# print(get_chat_response("我上一個問題是什麼？", memory))

