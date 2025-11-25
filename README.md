For this project, following librries need to be installed
pip install langchain pymongo bs4 openai tiktoken gradio requests lxml argparse unstructured
pip install langchain pymongo bs4 openai tiktoken gradio requests lxml argparse unstructured langchain-openai langchain-mongodb langchain-community

OR
pip install -r requirements.txt

# How to create python virtual environment
python3 -m venv .venv
# How to activate
source .venv/Scripts/activate or source .venv/bin/activate
# how to deactivate:
simply type: deactivate

# 1- Run all embedding and load them into collection_of_text_blobs
python3 load_data.py