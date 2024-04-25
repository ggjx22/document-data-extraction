from dotenv import load_dotenv
load_dotenv()

import os
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader

from src.user_query import get_parser_instructions

llama_cloud_api_key = os.getenv('LLAMA_CLOUD_API_KEY')


def parse_docs(result_format, document_dir):
    # instantiate parser
    parser = LlamaParse(
        api_key=llama_cloud_api_key,
        result_type=result_format,
        verbose=True,
        parsing_instruction=get_parser_instructions()
    )
    
    document_extractor = {'.pdf': parser}
    
    document = SimpleDirectoryReader(
        input_dir=document_dir,
        file_extractor=document_extractor
    )
    
    try:
        return document.load_data()
    except Exception as e:
        print(f'Parsing error: {e}')