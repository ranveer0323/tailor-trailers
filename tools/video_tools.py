from moviepy.editor import VideoFileClip
from langchain.tools import tool


class VideoTools:

    @tool("Trim Video Clip")
    def trim_video_clip(video_path: str, start_time: float, end_time: float, output_path: str) -> str:
        """
        Useful for trimming a video clip between specified start and end times.

        Args:
            video_path (str): Path to the input video file.
            start_time (float): Start time in seconds for the clip.
            end_time (float): End time in seconds for the clip.
            output_path (str): Path to save the trimmed video.

        Returns:
            str: Path to the saved trimmed video file.
        """
        # Load the video file
        video_clip = VideoFileClip(video_path)

        # Check if end_time is within video duration
        if end_time > video_clip.duration:
            raise ValueError("End time exceeds video duration.")

        # Trim the video
        trimmed_clip = video_clip.subclip(start_time, end_time)

        # Save the trimmed video
        trimmed_clip.write_videofile(
            output_path, codec="libx264", audio_codec="aac")

        # Close resources
        video_clip.close()

        return output_path
