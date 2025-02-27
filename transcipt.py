from youtube_transcript_api import YouTubeTranscriptApi

video_id = "dQw4w9WgXcQ"  # Replace with your video ID
transcript = YouTubeTranscriptApi.get_transcript(video_id)

for line in transcript:
    print(f"{line['text']} ({line['start']}s)")
