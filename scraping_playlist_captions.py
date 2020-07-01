"""This script accepts a YouTube Video id from a collection of Video IDs read from a file,
and stores the available captions for each video (if any) in a file at current working directory"""

# provide the name of output file in quotes
# importing the libraries 
from youtube_transcript_api import YouTubeTranscriptApi
from bs4 import BeautifulSoup 
import requests 

PLAYLIST_NAME = "CrashCourseStatistics"
FILE_NAME = r"/mnt/c/Users/rahul/Documents/Tutorials/Probability and Statistics/" + PLAYLIST_NAME

with open("video_ids.csv") as video_id_list:
    for VIDEO_ID in video_id_list:
    
        #Forming the complete url of the video
        URL = "https://www.youtube.com/watch?v="+VIDEO_ID
        
        #getting the captions
        CAPTIONS = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
        
        # getting the request from url 
        # FLAG_R = requests.get(URL) 
	
        # converting the text 
        # FLAG_S = BeautifulSoup(FLAG_R.text, "html.parser") 
	
        # finding meta info for title 
        # TITLE = FLAG_S.find("h1", class_="style-scope ytd-video-primary-info-renderer").children[0].text.replace("\n", "") 
        
        #desired file name for storing the captions
        # FILE_NAME = r"/mnt/c/Users/rahul/Documents/" + "CrashCourseStatistics"
        
        #storing the name of video and its url as initials
        TOTAL_CAPTIONS = "URL = " + URL + "\n"  # + "TITLE = " + TITLE + "\n" 
        
        
        for word in CAPTIONS:
            TOTAL_CAPTIONS = TOTAL_CAPTIONS + word['text'] + "\n"
        
        TEXT_FILE = open(FILE_NAME+".txt", "a")
        TEXT_FILE.write(TOTAL_CAPTIONS)
        TEXT_FILE.close()
