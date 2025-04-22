from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from messages import get_random_message
import os, pickle
import json

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate():
    creds = None
    # Check if token.pkl exists
    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as f:
            creds = pickle.load(f)
    if not creds or not creds.valid:
        raise ValueError("Token is invalid or missing. Please generate a valid token.pkl file.")
    return build('youtube', 'v3', credentials=creds)

def get_latest_videos(youtube, channel_id):
    req = youtube.search().list(
        part="snippet", channelId=channel_id,
        maxResults=1, order="date"
    )
    res = req.execute()
    return [item['id']['videoId'] for item in res['items'] if item['id']['kind'] == 'youtube#video']

def already_commented(video_id):
    if not os.path.exists('video_log.txt'):
        return False
    with open('video_log.txt', 'r') as f:
        return video_id in f.read()

def log_video(video_id):
    with open('video_log.txt', 'a') as f:
        f.write(video_id + '\n')

def post_comment(youtube, video_id, message):
    try:
        youtube.commentThreads().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {
                            "textOriginal": message
                        }
                    }
                }
            }
        ).execute()
        print(f"Commented on video: {video_id}")
    except Exception as e:
        print(f"Failed to comment on video {video_id}: {e}")

if __name__ == '__main__':
    channel_ids = [
        'UC_x5XG1OV2P6uZZ5FSM9Ttw',  # Google Developers
        'UC295-Dw_tDNtZXFeAPAW6Aw',  # Firebase
        'UCXuqSBlHAE6Xw-yeJA0Tunw',  # Linus Tech Tips
        'UCWv7vMbMWH4-V0ZXdmDpPBA',  # Programming with Mosh
        'UCxX9wt5FWQUAAz6UryhpQw',  # CS Dojo
        'UC8butISFwT-Wl7EV0hUK0BQ',  # freeCodeCamp
        'UClLXKYEEM8OBBx85DOa6-cg',  # Fireship
        'UCsBjURrPoezykLs9EqgamOA',  # Firebase
        'UC29ju8bIPH5as8OGnQzwJyA',  # Traversy Media
        'UCvjgXvBlbQiydffZU7m1_aw',  # The Coding Train
        'UCJbPGzawDH1nx5MzHoHTuuw',  # DevEd
        'UCW5YeuERMmlnqo4oq8vwUpg',  # The Net Ninja
        'UCshZ3rdoCLjDYNILXztQVdw',  # Program With Erik
        'UCVTlvUkGslCV_h-nSAId8Sw',  # LearnCode.academy
        'UCmXmlB4-HJytD7wek0Uo97A',  # JavaScript Mastery
        'UCFbNIlppjAuEX4znoulh0Cw',  # Web Dev Simplified
        'UC0e3QhIYukixgh5VVpKHH9Q',  # Code With Chris
        'UCO1cgjhGzsSYb1rsB4bFe4Q',  # Fun Fun Function
        'UClb90NQQcskPUGDIXsQEz5Q',  # Dev Ed
        'UCZUyPT9DkJWmS_DzdOi7RIA',  # Tech With Tim
        'UCm9K6rby98W8JigLoZOh6FQ',  # LevelUpTuts
        'UCVyRiMvfUNMA1UPlDPzG5Ow',  # DesignCourse
        'UC4xKdmAXFh4ACyhpiQ_3qBw',  # TechLead
        'UCAuUUnT6oDeKwE6v1NGQxug',  # TED
        'UCvtT19MZW8dq5Wwfu6B0oxw',  # Coding Phase
        'UCCktnahuRFYIBtNnKT5IYyg',  # The Futur
        'UC7eRwj8OVKbYVMGQIQ_nNJg',  # Think Media
        'UC8ENHE5xdFSwx71u3fDH5Xw',  # ThePrimeagen
        'UClFE1N_sMek7cyvwPAyVVQA',  # interviewing.io
        'UCJUmE61LxhbhudzUugHL2wQ',  # Clément Mihailescu
        'UCBwmMxybNva6P_5VmxjzwqA',  # TheCodingTech
        'UCqeTj_QAnNlmt7FwzNwHZnA',  # sentdex
        'UCWr0mx597DnSGLFk1WfvSkQ',  # Kalle Hallden
        'UC-lHCBqKhtnXbQHxiRR0k3Q',  # thenewboston
        'UCKuDLsO0Wwef53qdHPjbU2Q',  # Alex Genadinik
        'UCjREVt2ZJU8ql-NC9Gu-TJw',  # Stefan Mischook
        'UCLOAPb7ATQUs_nDs9ViLcMw',  # DevTips
        'UCV0qA-eDDICsRR9rPcnG7tw',  # Joma Tech
        'UC-91UA-Xy2Cvb98deRXuggA',  # Bootstrap
        'UCYbK_tjZ2OrIZFBvU6CCMiA',  # Academind
        'UC0tRdbXVDbhaRvZPKsRgmIg',  # Derek Banas
        'UCEBb1b_L6zDS3xTUrIALZOw',  # MIT OpenCourseWare
        'UCa5WIWAfGpRVnCJkJWVkAzg',  # Simplilearn
        'UC2WHjPDvbE6O328n17ZGcfg',  # ForrestKnight
        'UCbT68vR5gtnCHrCib8T7slw',  # Engineer Man
        'UCJZv4d5rbIKd4QHMPkcABCw',  # Kevin Powell
        'UCAjsH3UCJrd-xAfUzqnd-bw',  # Scott Hanselman
        'UC0BAd8tPlDqFvDYBemHcQPQ',  # Tech With Nader
        'UC2KJHARTj6KRpKn5iFu3GLQ',  # Tech Primers
        'UC-JTtk2nEdWPaYsKHQJvwpQ',  # Manning Publications
        'UCxQKHvKbmn-cAFb1f3TrCRw',  # Khan Academy
        'UCMZFwxv5l-XtKi693qMJptA',  # Coding Tech
        'UCapU9dIagn7pPs35e1FKKXA',  # LinkedIn Learning
    ]
    youtube = authenticate()
    
for channel_id in channel_ids:
        print(f"Processing channel: {channel_id}")
        videos = get_latest_videos(youtube, channel_id)

        for vid in videos:
            if not already_commented(vid):
                msg = get_random_message()
                post_comment(youtube, vid, msg)
                log_video(vid)
            else:
                print(f"Already commented on video: {vid}")