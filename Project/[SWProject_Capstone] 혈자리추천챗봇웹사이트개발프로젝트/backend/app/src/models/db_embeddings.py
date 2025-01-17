from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path = 'backend/app/.env.local') # 환경 변수 load

api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

text = "안녕~! 나는 대양이야."
query_result = embeddings.embed_query(text)

print(query_result[:3])