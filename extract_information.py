from pymongo import MongoClient
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_community.document_loaders import DirectoryLoader
#from langchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_param

client = MongoClient(key_param.MONGO_URL)
dbName = "longchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]
 