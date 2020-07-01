"""This script accepts a YouTube Video id,
and stores the available captions (if any) in a file at current working directory"""

from youtube_transcript_api import YouTubeTranscriptApi

# provide the video id- the part after v=...
VIDEO_ID = r'PPD8lER8ju4&list=PLH2l6uzC4UEW3iJO4T0qUeUEp_X-f1U7S&index=23'

# provide the name of output file in quotes
FILE_NAME = r"/mnt/c/Users/rahul/Documents/Tutorials/Probability and Statistics/CrashCourseStatistics_21-P-Value Problems"

CAPTIONS = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
TOTAL_CAPTIONS = "URL = https://www.youtube.com/watch?v="+VIDEO_ID+"\n"

for word in CAPTIONS:
	TOTAL_CAPTIONS = TOTAL_CAPTIONS + word['text'] + "\n"


TEXT_FILE = open(FILE_NAME+".txt", "w")
TEXT_FILE.write(TOTAL_CAPTIONS)
TEXT_FILE.close()

with open("video.csv")