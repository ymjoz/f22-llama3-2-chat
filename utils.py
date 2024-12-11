from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3.2", temperature=0)

def get_chat_response(text: str):
  return llm.invoke(text)

print(get_chat_response("嗨, 用中文回答，請介紹一下你自己。接著，告訴我，台灣的地理中心碑在那裡？"))
print(get_chat_response("我上一個問題是什麼？"))