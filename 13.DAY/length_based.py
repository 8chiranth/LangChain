from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('books/Final NSS RePORT.pdf')

# text = "Chiranth C is a passionate Machine Learning student from India with a strong ambition to break into big tech. With hands-on experience in Python, FastAPI, React, and advanced ML libraries, Chiranth actively builds projects ranging from exploratory data analysis and YOLO-based computer vision to AI assistants powered by LangChain and Cohere. Always curious and driven, Chiranth blends creativity with technical expertise, developing intelligent systems that not only solve problems but also inspire innovation. His journey reflects both discipline and imagination, making him a promising future engineer in the AI/ML space."

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap = 0,
    separator =""
)

result = splitter.split_documents(docs)
print(result[1].page_content)




