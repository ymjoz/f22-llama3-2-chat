from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm = OllamaLLM(model="llama3.2", temperature=0)
memory = ConversationBufferMemory(return_messages=True)
conversation = ConversationChain(llm=llm, memory=memory)

def get_chat_response(text: str):
    return conversation.predict(input=text)

# print(get_chat_response("告訴我，台灣的地理中心碑在那裡？"))
# print(get_chat_response("我上一個問題是什麼？"))

print(get_chat_response("hello!請先介紹一下你自己。我是Rossi。"))
# print(get_chat_response("我的名字是什麼？那麼，你的名字是什麼呢？"))
get_chat_response("我的上一個問題是什麼？")
