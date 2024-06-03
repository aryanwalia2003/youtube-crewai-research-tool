from crewai_tools import YoutubeChannelSearchTool

# Initialize the tool with a specific Youtube channel handle to target your search
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@GeoHistory')


# or 

# Initialize the tool to search within any Youtube channel's content the agent learns about during its execution
# tool = YoutubeChannelSearchTool() #if you want to get all content available on youtube 
