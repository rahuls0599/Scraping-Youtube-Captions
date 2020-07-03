"""This script accepts a YouTube Video id from a collection of Video IDs read from a file,
and stores the available captions for each video (if any) in a file at current working directory"""

# provide the name of output file in quotes
# importing the libraries 
from youtube_transcript_api import YouTubeTranscriptApi
import os

PLAYLIST_ID = 'PLVHgQku8Z934EjJNuMRnCgVF0Uf2kTX9y'
PLAYLIST_URL = 'https://www.youtube.com/playlist?list=' + PLAYLIST_ID
CREATE_URL_FILE_CMD = 'youtube-dl -i --get-id ' + PLAYLIST_URL + '> ./video_urls.csv'
os.system(CREATE_URL_FILE_CMD)
PLAYLIST_NAME = "Simplilearn Linux"
FILE_NAME = r"/mnt/c/Users/rahul/Documents/Tutorials/" + PLAYLIST_NAME

TOTAL_CAPTIONS = ""
with open("video_urls.csv") as video_id_list:
    for VIDEO_ID in video_id_list:
        
        '''if ( i%2 == 0):
            TOTAL_CAPTIONS = "TITLE = " + VIDEO_ID + "\n"
            i = i + 1
            continue '''
            
        #Forming the complete url of the video
        URL = "https://www.youtube.com/watch?v="+VIDEO_ID
        
        #getting the captions
        CAPTIONS = YouTubeTranscriptApi.get_transcript(VIDEO_ID)
        
        #desired file name for storing the captions
        # FILE_NAME = r"/mnt/c/Users/rahul/Documents/" + "CrashCourseStatistics"
        
        #storing the name of video and its url as initials
        TOTAL_CAPTIONS = "URL = " + URL + "\n"  

        for word in CAPTIONS:
            TOTAL_CAPTIONS = TOTAL_CAPTIONS + word['text'] + "\n"
        
        TEXT_FILE = open(FILE_NAME+".txt", "a")
        TEXT_FILE.write(TOTAL_CAPTIONS)
        TEXT_FILE.close()
