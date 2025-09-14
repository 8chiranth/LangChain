from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)


# load
docs = loader.load()
for doc in docs:
    print(doc.metadata)

# lazy load

doc = loader.lazy_load()
for docs in doc:
    print(docs.metadata)