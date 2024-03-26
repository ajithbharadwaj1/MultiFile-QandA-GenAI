from utils.YouTube_Helpers import yt_transcribe
from langchain.docstore.document import Document

def summarize_YouTube_Video(link:str)-> str:
    embed , text = yt_transcribe(link)
    document = Document(page_content=text, metadata={"source": f"YouTube_Video{link}"})
    return document


