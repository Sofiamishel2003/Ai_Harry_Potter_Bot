from dotenv import load_dotenv
import os
import sys
import io

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from consts import INDEX_NAME
from firecrawl import FirecrawlApp
from langchain.schema import Document
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

def ingest_docs2()-> None:
    app = FirecrawlApp(api_key=os.environ['FIRE_CRAWL_API_KEY'])
    url = "https://harrypotter.fandom.com/es/wiki/Harry_Potter"
    page_content = app.scrape_url(url=url,
                                  params={
                                     "onlyMainContent": True
                                  })
    print(page_content)
    doc=Document(page_content=str(page_content), metadata={"source": url})
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    docs=text_splitter.split_documents([doc])
    PineconeVectorStore.from_documents(
        docs, embeddings, index_name=INDEX_NAME
    )

def ingest_docs():
    loader = ReadTheDocsLoader("langchain-docs/api.python.langchain.com/en/latest", encoding='utf-8')
    raw_documents = loader.load()
    print(f"Loaded {len(raw_documents)} raw documents")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
    documents = text_splitter.split_documents(raw_documents)
    print(f"Loaded {len(documents)} documents")
    for doc in documents:
        new_url = doc.metadata["source"]
        new_url = new_url.replace("langchain-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embedding=embeddings, index_name=INDEX_NAME
    )


if __name__ == "__main__":
    ingest_docs2()