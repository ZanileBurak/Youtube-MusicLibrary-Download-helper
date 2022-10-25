from __future__ import unicode_literals
from googleapiclient.discovery import build
from pprint import pprint
import yt_dlp
import youtube_dl
api_key = 'AIzaSyAVps4kRwMOiJ6LDg6Q51nKrgMveaKAlow'  #BU KISIMDA GOOGLE TARAFINDAN VERILEN API KEYINIZI GIRINIZ VE BASKALARIYLA PAYLASMAYINIZ

youtube = build('youtube','v3', developerKey=api_key)

nextPageToken=None

vid_nameAndID = {}
while True:

    playlists_request = youtube.playlistItems().list(
        part ='contentDetails,snippet',
        playlistId = 'PLwRhLdmR9KZ7J5dBqfJY0k_8zowCxx_2h', #BU KISIMDA ISTENILEN YOUTUBE PLAYLISTININ ID DEGERINI GIRINIZ
        maxResults=100,
        pageToken=nextPageToken
    )
    pl_response =playlists_request.execute()


    for idx, item in enumerate(pl_response['items']) :

        video_title = pl_response['items'][idx]['snippet']['title']
        video_Id = pl_response['items'][idx]['contentDetails']['videoId']
        vid_nameAndID[video_title] = video_Id
        nextPageToken = pl_response.get('nextPageToken')
   
    if not nextPageToken:
      counting_page_songs=1
      pprint(vid_nameAndID)
      break

ydl_opts = {
     'format': 'bestaudio/best',
     'postprocessors': [{
         'key': 'FFmpegExtractAudio',
         'preferredcodec': 'mp3',
         'preferredquality': '320',
     }],
     'ignoreerrors': True
 }
for idx,keys in  enumerate(vid_nameAndID):

     link = "https://www.youtube.com/watch?v="+vid_nameAndID.get(keys)   

     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
           
                 try: 
                     ydl.cache.remove()
                     print(f"{idx}-){keys}   Video indiriliyor...")
                     ydl.download([link])
                    
                 except youtube_dl.DownloadError as error:
                     pass

