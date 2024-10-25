from moviepy.editor import VideoFileClip, concatenate_videoclips
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

    @tool("Merge Video Clips")
    def merge_video_clips(clip_paths: list, output_path: str) -> str:
        """
        Useful for merging multiple video clips into a single video trailer.

        Args:
            clip_paths (list): List of file paths for the individual video clips.
            output_path (str): Path to save the merged video trailer.

        Returns:
            str: Path to the saved merged video file.
        """
        # Load each video clip from provided paths
        video_clips = [VideoFileClip(path) for path in clip_paths]

        # Concatenate the video clips
        merged_clip = concatenate_videoclips(video_clips, method="compose")

        # Save the merged video
        merged_clip.write_videofile(
            output_path, codec="libx264", audio_codec="aac")

        # Close resources
        for clip in video_clips:
            clip.close()

        return output_path
