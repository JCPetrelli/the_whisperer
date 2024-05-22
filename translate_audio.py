import subprocess
import argparse
from gtts import gTTS
import os

def transcribe_and_translate(audio_file):
    # Transcribe and translate the audio using Whisper
    # whisper_command = [
    #     'whisper', audio_file, '--language', 'Polish', '--task', 'translate', '--model', 'medium'
    # ]
    # subprocess.run(whisper_command)

    # Remove the extension from audio_file
    audio_file_base = os.path.splitext(audio_file)[0]
    
    # Read the translated text from Whisper's output file
    translated_text_file = f"{audio_file_base}.txt"
    with open(translated_text_file, 'r', encoding='utf-8') as file:
        translated_text = file.read()
    
    # Generate the audio file from the translated text
    tts = gTTS(text=translated_text, lang='en')
    translated_audio_file = f"{audio_file}_translated.mp3"
    tts.save(translated_audio_file)
    
    print(f"Translated audio saved as {translated_audio_file}")

def main():
    parser = argparse.ArgumentParser(description="Transcribe and translate Polish audio to English and generate an audio file.")
    parser.add_argument('audio_file', type=str, help='The path to the audio file to transcribe and translate.')
    
    args = parser.parse_args()
    transcribe_and_translate(args.audio_file)

if __name__ == "__main__":
    main()
