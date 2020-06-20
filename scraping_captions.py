from youtube_transcript_api import YouTubeTranscriptApi
# provide the video id- the part after v=...
video_id = r'VUW2pIjDpEk'
# provide the naem of output file in quotes
filename = "wsl2"

captions = YouTubeTranscriptApi.get_transcript(video_id)
total_caption = ""

for word in captions:
    total_caption = total_caption + word['text'] + "\n"
    #print(word['text'])


text_file = open(filename+".txt", "w")
text_file.write(total_caption)
text_file.close()