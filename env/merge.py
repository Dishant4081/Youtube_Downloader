import os
import subprocess

#merge video and audio separately
def merge_video_and_audio(audio_path, video_path, output_path):
        print(f"Video file exists: {os.path.exists(video_path)}")
        print(f"Audio file exists: {os.path.exists(audio_path)}")
        print(f"Files in video directory: {os.listdir(os.path.dirname(video_path))}")
        print(f"Files in audio directory: {os.listdir(os.path.dirname(audio_path))}")
        print(f"Video path before condition: {os.path.abspath(video_path)}")
        print(f"Audio path before condition: {os.path.abspath(audio_path)}")

        try:
            video_exists = os.path.exists(video_path)
            audio_exists = os.path.exists(audio_path)
            if video_exists and audio_exists:
                print("Inside the 'if' block.")
                print(f"Video path: {os.path.abspath(video_path)}")
                print(f"Audio path: {os.path.abspath(audio_path)}")

                subprocess.run([
                'ffmpeg',
                '-i', audio_path,
                '-i', video_path,
                '-c:v', 'copy',
                '-c:a', 'copy',
                output_path
                ])
                print(f"Merged video and audio saved at {os.path.abspath(output_path)}.")
            else:
                print("Video or audio file not found.")
        except Exception as e:
            print(f"An error occurred during file existence check: {str(e)}")