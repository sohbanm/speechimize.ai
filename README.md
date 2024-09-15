# Speechimize.ai

Welcome to Speechimize.ai! This project was conceived during Hack the North 2024. Given the time constraints, we developed a foundational prototype with a promising concept. 

## Project Overview

**Speechimize.ai** is designed to streamline the process of transcribing and summarizing video content, such as lectures, seminars, and meetings. Our solution leverages two key technologies:

1. **Symphonic API**: Used to transcribe video content into text through lip reading.
2. **Cohere**: Employed to generate concise summaries of the transcribed text.

The primary goal of Speechimize.ai is to provide an efficient way to summarize and digest important information from videos. This is particularly useful for individuals who were unable to attend a meeting or lecture, allowing them to quickly catch up on the content.

## Limitations

We encountered a notable limitation with the Symphonic API: videos longer than 60 seconds could not be processed effectively. This constraint currently limits the functionality of the application, as longer videos exceed the API’s processing capabilities.

## Future Enhancements

We envision several exciting features for Speechimize.ai, including:

- **Interactive Q&A**: Allow users to ask questions about the video content and retrieve specific information.
- **Enhanced Summarization Options**: Offer various summary lengths and formats to suit different needs.
- **Integration with Additional Platforms**: Expand compatibility with other video and transcription services.

## How It Works

1. **Transcription**: Upload a video, and Speechimize.ai uses the Symphonic API to convert the audio into text.
2. **Summarization**: The transcribed text is then processed by Cohere to generate a summary.
3. **Output**: Receive a concise summary of the video, providing an overview of the key points covered.
