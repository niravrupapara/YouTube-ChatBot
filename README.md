# YouTube-ChatBot
RAG-powered chatbot for answering questions from YouTube video transcripts.

## 📊 YouTube RAG ChatBot Pipeline

## 📝 Project Description
This YouTube RAG ChatBot takes any YouTube link, fetches the transcript, 
splits it into chunks, converts them into embeddings, stores them in a vector database, 
and retrieves the most relevant chunks when the user asks a question.  
These retrieved chunks are combined with the user query and passed to an LLM 
to generate the final meaningful answer.

![YouTube RAG ChatBot Pipeline](./yt-flowchart.png)
