from langchain_text_splitters import CharacterTextSplitter

text = '''
Cricket is a complex sport that combines physical skill, strategy, statistics, psychology, and teamwork. Its different formats provide unique challenges, ranging from the patience and endurance required in Test cricket to the rapid decision-making required in Twenty20 cricket.

Batting, bowling, fielding, and captaincy all contribute to the outcome of a match. Modern cricket has also become increasingly dependent on technology and data analysis, with teams using video analysis, performance statistics, ball-tracking systems, and advanced analytics to improve decision-making.

The continued evolution of cricket demonstrates its ability to preserve traditional elements while adapting to changing audiences and technology. From five-day Test matches to high-intensity T20 competitions, cricket remains a sport with extraordinary tactical depth and global cultural significance.
'''

splitter = CharacterTextSplitter(
    chunk_size=30, 
    chunk_overlap=0,
    separator=""
)

result = splitter.split_text(text)

print(result)