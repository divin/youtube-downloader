import os

import gradio as gr  # type: ignore
from pytube import YouTube  # type: ignore

from .constants import DESCRIPTION


def download_from_youtube(
    url: str, file_type: str, file_name: str, resolution: str
) -> tuple[gr.Video, gr.Audio]:
    """Download a YouTube video or audio file."""
    if url == "":
        raise ValueError("Please enter a valid YouTube URL.")

    if file_name == "":
        raise ValueError("Please enter a valid file name.")

    if not file_name.endswith(".mp4"):
        file_name = f"{file_name}.mp4"

    # Download video or audio
    yt = YouTube(url)
    if file_type == "Video":
        path_to_file = yt.streams.get_by_resolution(resolution=resolution).download(
            output_path="downloads", filename=file_name
        )
    else:
        path_to_file = yt.streams.get_audio_only().download(
            output_path="downloads", filename=file_name
        )

    return (
        gr.Video(value=path_to_file, visible=file_type == "Video"),
        gr.Audio(value=path_to_file, visible=file_type == "Audio"),
    )


def get_app() -> gr.Interface:
    with gr.Blocks(title="⬇️ YouTubeDownloader") as app:
        gr.Markdown("# ⬇️ YouTube Downloader")

        with gr.Accordion("About", open=False):
            gr.Markdown(DESCRIPTION)

        with gr.Row():
            with gr.Column():
                url = gr.Textbox(lines=1, label="🔗 YouTube URL")
                file_type = gr.Dropdown(
                    value="Video", choices=["Video", "Audio"], label="File Type"
                )
                resolution = gr.Dropdown(
                    value="720p",
                    choices=["720p", "480p", "360p"],
                    label="📺 Resolution (will be ignored if downloading audio)",
                )
                file_name = gr.Textbox(label="📁 File Name (without extension)")
                download = gr.Button("⬇️ Download")

            with gr.Column():
                video_output = gr.Video(label="📺 Video", visible=True)
                audio_output = gr.Audio(label="🔈 Audio", visible=True)

        download.click(
            fn=download_from_youtube,
            inputs=[url, file_type, file_name, resolution],
            outputs=[video_output, audio_output],
        )

        return app


if __name__ == "__main__":
    # Make sure downloads directory exists
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    app = get_app()
    app.launch(show_api=False)
