from setuptools import find_packages  # type: ignore
from setuptools import setup  # type: ignore

if __name__ == "__main__":
    name = "youtube-downloader"
    version = "0.1.0"
    python_requires = ">=3.10,<3.11"
    description = "A simple app to download YouTube videos in different formats."
    packages = find_packages(include=["youtube_downloader", "youtube_downloader.*"])
    install_requires = [
        "pytube",
        "gradio",
    ]
    extras_require = {
        "development": ["isort", "mypy", "black", "Flake8-pyproject", "pytest", "pytest-cov"]
    }

    setup(
        name=name,
        version=version,
        description=description,
        python_requires=python_requires,
        packages=packages,
        install_requires=install_requires,
        extras_require=extras_require,
        entry_points={},  # Define here any scripts you want to run from the command line
    )
