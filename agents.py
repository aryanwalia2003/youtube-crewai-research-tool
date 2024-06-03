from crewai import Agent
from tools import yt_tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-3.5-turbo"
my_llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.5)

blog_researcher=Agent(
    role='Blog and Content Research Expert',
    goal='Extract all the transcripts on the topic {topic} from whatever content is present on youtube channel',
    verboe=True,
    llm=my_llm,  # Optional
    memory=True,
    backstory=(
       "Expert in efficient video transcript extraction and a historian with a zeal to study varying types of history"
       "recognize the importance of accessible content and the time-consuming nature of manual transcription." 
    ),
    tools=[yt_tool],
    max_iter=4,
    allow_delegation=True
)

## creating a senior blog writer agent with YT tool

blog_writer=Agent(
    role='Blog Writer',
    goal='Write an interesting blog and tell amazing ,exciting stories on the topic {topic} from whatever is available on youtube channel must including the historical facts',
    verbose=True,
    memory=True,
    backstory=(
        "With the passion for storytelling, the pursuit of knowledge, and the desire to engage and inspire readers"
        "Write an informative blog which has a human like flow and interesting to read but should carry all the historical details"
    ),
    tools=[yt_tool],
    llm=my_llm,  # Optional
    max_iter=15,
    allow_delegation=False


)


# blog_researcher= Agent(
#   role='Blog and Content Research Expert',
#   goal='Extract all the transcripts on the topic {topic} from the given youtube channel to provide for efficient blog creation '
#   backstory="""Expert in efficient video transcript extraction and a historian with a zeal to study varying types of history,recognize the importance of accessible content and the time-consuming nature of manual transcription.""",
#   tools=[],
#   max_iter=4,  # Optional
# #   max_rpm=None, # request per min
#   verbose=True,  # Optional
#   allow_delegation=True,  # Optional
#   cache=True 
# )


# blog_writter = Agent(
#   role='Senior Blog Writter',
#   goal='Write an interesting blog and tell amazing ,exciting stories on the topic {topic} for the youtube channel',
#   backstory=""" With the passion for storytelling, the pursuit of knowledge, and the desire to engage and inspire readers.Write an informative blog which has a human like flow and interesting to read""",
#   tools=[],  # Optional, defaults to an empty list
  
#   max_iter=15,  # Optional
# #   max_rpm=None, # Optional
#   verbose=True,  # Optional
#   allow_delegation=False,  # Optional
#   cache=True  # Optional
# )
