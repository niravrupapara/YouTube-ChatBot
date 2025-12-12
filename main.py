print("jay shree ram")

from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_id: str):
    try:
        # returns a list of dicts: [{'text': '...', 'start': 0.0, 'duration': 5.1}, ...]
        transcript_data = YouTubeTranscriptApi

        # Merge text
        full_text = " ".join([t["text"] for t in transcript_data])
        return full_text

    except Exception as e:
        print("Error while fetching transcript:", e)
        return None


# Example
video_id = "dQw4w9WgXcQ"
print(get_transcript(video_id))
