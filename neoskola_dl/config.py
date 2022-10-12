import os

# Path to the directory where the downloaded files will be saved
# If the directory does not exist, it will be created
# If the directory is not specified, the current directory will be used
DOWNLOAD_PATH = os.path.join(os.path.expanduser('~'), 'Downloads', 'Neoskola')
CHUNK_SIZE = 256 * 1024  # 256 KB
DOWNLOAD_OPTION = ['1080p', 'mp3']  # '1080p' or '720p' or '540p' or '240p' or 'mp3'
