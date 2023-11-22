
from googleapiclient.discovery import build
import os

# Set up YouTube API key
api_key = 'AIzaSyC2zDcvZ2WRU9EedHt4shxynO3VlcXp8LU'  # Replace with your own API key
youtube = build('youtube', 'v3', developerKey=api_key)

def get_top_2023_afrobeat_songs(max_results):
    request = youtube.search().list(
        q='Afrobeats',              # Search query
        part='snippet',            # Part of the data to be retrieved
        maxResults=max_results,    # Number of results to return
        order='viewCount',         # Order by view count
        type='video',              # Look for videos
        videoCategoryId='10',      # Category ID for Music
        publishedAfter='2023-10-01T00:00:00Z', # Videos published after this date
        publishedBefore='2023-12-31T23:59:59Z', # Videos published before this date
    )
    response = request.execute()

    for item in response['items']:
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        print(f'{title} - https://www.youtube.com/watch?v={video_id}')

# Example usage
get_top_2023_afrobeat_songs(40)
