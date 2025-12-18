import re
from youtube_transcript_api import YouTubeTranscriptApi

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K = 3


 
def extract_video_id(youtube_url: str) -> str:
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, youtube_url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)




def load_youtube_transcript(video_id: str) -> str:
    api_object = YouTubeTranscriptApi()
    transcript_list = api_object.fetch(video_id)
    

    transcript_text =" ".join(item.text for item in transcript_list)

    return transcript_text



def split_text(text: str):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    return splitter.create_documents([text])


def create_vector_store(documents):
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME
    )
    texts = [doc.page_content for doc in documents]
    vector_store =  FAISS.from_texts(texts, embeddings)
    return vector_store


def get_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": TOP_K}
    )


def load_llm():
    llm_endpoint = HuggingFaceEndpoint(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        temperature=0,
        max_new_tokens=512
    )

    chat_model = ChatHuggingFace(llm=llm_endpoint)
    return chat_model



def generate_prompt(retrieved_docs , question):
    context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    template = PromptTemplate(
        template="""
    You are a helpful assistant.
    Answer the question using ONLY the context below.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    , input_variables=['context', 'question']
    )

    prompt = template.invoke({'context':context , 'question':question})
    return prompt



def generate_response(llm, prompt):
   

    response = llm.invoke(prompt)
    return response


def generate_transcript_summary(transcript_text: str):
    llm = load_llm()

    summary_prompt = f"""
You are a helpful assistant.
Summarize the following YouTube video transcript in a clear and concise way.

Transcript:
{transcript_text}

Summary:
"""

    response = llm.invoke(summary_prompt)
    return response.content






def get_video_transcript(url : str) -> str:
    """
   Extracts video ID and returns full transcript text
    """

    video_id = extract_video_id(url)
    transcript_text = load_youtube_transcript(video_id)

    return transcript_text


def answer_from_transcript(transcript_text : str , question : str) -> str:

    documents = split_text(transcript_text)

    vector_store = create_vector_store(documents)

    retriever = get_retriever(vector_store)

    retrieved_docs = retriever.invoke(question)

    prompt = generate_prompt(retrieved_docs , question)

    model = load_llm()

    response = generate_response(model , prompt)

    answer = response.content
    

    return ans
