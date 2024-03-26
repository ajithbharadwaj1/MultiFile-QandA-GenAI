from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_transformers import Html2TextTransformer
from typing import Union, List

def webparser(links: Union[str, List[str]])-> List:
    loader = WebBaseLoader(links)
    data = loader.load()
    html2text = Html2TextTransformer()
    docs_transformed = html2text.transform_documents(data)
    return docs_transformed






    

