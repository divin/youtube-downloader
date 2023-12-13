import unittest
from unittest.mock import MagicMock
from unittest.mock import patch

from pytube import YouTube  # type: ignore

from youtube_downloader.__main__ import download_from_youtube


class TestDownloadFromYoutube(unittest.TestCase):
    @patch.object(YouTube, "streams")
    def test_invalid_url(self, _: MagicMock) -> None:
        with self.assertRaises(ValueError):
            download_from_youtube("", "mp4", "test", "720p")

    @patch.object(YouTube, "streams")
    def test_invalid_file_name(self, _: MagicMock) -> None:
        with self.assertRaises(ValueError):
            download_from_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ", "mp4", "", "720p")


if __name__ == "__main__":
    unittest.main()
