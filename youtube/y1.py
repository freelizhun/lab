# -*- coding: utf-8 -*-
#!/usr/bin/python
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import dl 

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyCsYuzqsU6fHdjJadjRsS62jOtxBdNTvmM"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
BaseURL='https://www.youtube.com/watch?v='
def youtube_search(options, search_index):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  #options.q = u'三國'
  #options.q = u'新三國演義 2010 DVD 01'
  options.q = search_index
  #print options.q 
  search_response = youtube.search().list(
    #q=options.q,
    q=search_index,
    part="id,snippet",
    maxResults=50#options.max_results,
    #start-index=100
    #pageToken='CDIQAA'
  ).execute()

  videos = []
  channels = []
  playlists = []

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  #print search_response
  #print search_response
  for search_result in search_response.get("items", []):
    if search_result['snippet']['title']==options.q:
        linkurl = BaseURL + search_result['id']['videoId']
        print linkurl
        print 'got it'
        dl.download(linkurl)
        break;
    else:
        continue
  print ' cannot find the video: %s '%options.q
"""
print search_result['snippet']['title']
try:
    print search_result["id"]["videoId"]
    print 
    linkurl = BaseURL + search_result['id']['videoId']
    print linkurl
    print '--------------------'
except:
    print 'not found'
"""
"""
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                 search_result["id"]["videoId"]))
    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  print "Videos:\n", "\n".join(videos), "\n"
  print "Channels:\n", "\n".join(channels), "\n"
  print "Playlists:\n", "\n".join(playlists), "\n"
  """


if __name__ == "__main__":
  #argparser.add_argument("--q", help="Search term", default="Google")
  argparser.add_argument("--q", help="Search term", default="三國")
  argparser.add_argument("--max-results", help="Max results", default=50)
  #argparser.add_argument("--start-index", help="start index", default=49)
  args = argparser.parse_args()
  print args
  for loop in range(1,100):
      if loop <10:
         search_index=u'新三國演義 2010 DVD 0%s'%loop
      else:
         search_index=u'新三國演義 2010 DVD %s'%loop
     
      print 'search %s'%search_index
      try:
        youtube_search(args, search_index)
      except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
