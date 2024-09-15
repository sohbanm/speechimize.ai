# speechimize.ai
from dotenv import load_dotenv
import os
import requests
import io
import cohere

load_dotenv()

cohere_key = os.getenv('COHERE_API')

print("--- Welcome to Speechimize.ai! ---\n\nHere you can upload an mp4 file and retrieve a summary of the video. \nNote that currently the application is only limited to 59s videos.\n")

videoPath = input("Please enter the absolute file path of the MP4 file. (Please use '/' instead of '\\'): ")
print("\n")


cohere_client = cohere.Client(cohere_key)


def transcribe(file_path):
 
    url = "https://symphoniclabs--symphonet-vsr-modal-htn-model-upload-static-htn.modal.run"

    with open(file_path, 'rb') as video_file:
        video = io.BytesIO(video_file.read())

    response = requests.post(url, files={'video': ('input.mp4', video, 'video/mp4')})

    return(response.text)


text = transcribe(videoPath)

response = cohere_client.summarize(text=text)
print(response.summary)