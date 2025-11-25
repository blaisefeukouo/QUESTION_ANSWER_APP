from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr
from gradio.themes.base import Base
import key_param

client = MongoClient(key_param.MONGO_URL)
dbName = "longchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

loader = DirectoryLoader("./sample_files", glob="./*.txt", show_progress=True)
data = loader.load()
embeddings = OpenAIEmbeddings(openai_api_key=key_param.open_api_key)
#Initialize the vector store. 
#Vectorize the text from the documents using the specified Embeddings model and insert them into the specified mongodb collection
vector_store = MongoDBAtlasVectorSearch.from_documents(data, embeddings, collection=collection, index_name="vector_index")
