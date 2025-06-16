from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
import requests
loader=TextLoader('hamza_port.txt')
document=loader.load()
splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=10)
chunks=splitter.split_documents(document)
emed=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
vectorstores=Chroma.from_documents(chunks, emed)
quizz='What is your interest'
similar=vectorstores.similarity_search(quizz,k=3)
context=[main.page_content for main in similar]
import requests
api_key = "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"
url = "https://api.groq.com/openai/v1/chat/completions"
headers={
    'Authorization':f'Bearer {api_key}',
    'Content-Type':'application/json'
}
prompt=f"""Your name is Hamza and when someone ask you question you have to reply based on given context as simple as that.
Context: {context}
Quizz:{quizz}"""
payload={
    'model':'llama3-8b-8192',
    'messages':[{
        'role':'user','content':prompt
    }],
    'max_tokens':60

}
response=requests.post(url=url,headers=headers,json=payload)
data=response.json()
print(f"Hamza: {data['choices'][0]['message']['content']}")