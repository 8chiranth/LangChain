from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """You are a passionate learner and aspiring machine learning engineer with a strong foundation in Python, data analysis, and backend development. Over time, youve built skills in working with libraries such as Pandas, NumPy, and scikit-learn, and youve also explored modern frameworks like FastAPI and LangChain to develop practical AI-driven applications. You enjoy combining creativity with problem-solving, which is why you often take on projects that challenge you to integrate APIs, voice interfaces, and advanced ML models. With a keen interest in building intelligent assistants and automation tools, you are constantly pushing yourself to bridge the gap between theoretical knowledge and real-world implementation.

Beyond technical expertise, you are highly curious and motivated, always eager to learn new technologies and refine your problem-solving mindset. You have a clear vision of working at top tech companies, and you are building your portfolio through projects ranging from EDA and backend APIs to AI assistants like JARVIS. Your dedication to continuous improvement, combined with your ability to adapt quickly, makes you stand out as someone who is not just learning for the sake of knowledge but for the purpose of creating impactful solutions."""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0

)


chunk = splitter.split_text(text)

print(len(chunk))
print(chunk)






























