from pymongo import MongoClient
from longchain.embeddings.openai import OpenAIEmbeddings
from longchain.vectorstores import MongoDBAtlasVectorSearch
from longchain.document_loaders import DirectoryLoader
from longchain.llms.openai import OpenAI
from longchain.chains import RetrievalQA
import gradio as gr
from gradio.themes.base import Base
import key_param

client = MongoClient(key_param.MONGO_URL)
dbName = "longchain_demo"
collectionName = "collection_of_text_blobs"
collection = client[dbName][collectionName]

loader = DirectoryLoader(
    "./sample_files",
    glob="./*.txt",
    show_progress=True
)
data = loader.load()
embeddings = OpenAIEmbeddings(openai_api_key=key_param.open_api_key)
#Initialize the vector store. 
#Vectorize the text from the documents using the specified Embeddings model and insert them into the specified mongodb collection
vector_store = MongoDBAtlasVectorSearch.from_documents(
    data,
    embeddings,
    collection=collection
)
