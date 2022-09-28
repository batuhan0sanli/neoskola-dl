# Neoskola Course Downloader

A python based utility to download courses from Neoskola for PERSONAL offline use.

## ❗ Important Note

This is a personal project and is not affiliated with Neoskola in any way. Made for personal development and learning
purposes only. Please do not use this to download courses for commercial purposes.

Don't share your credentials. Owner of this repository is not responsible for any misuse if you share your credentials
with strangers.

## Installation

### Requirements

- Python 3.6 or above
- Chrome browser
- Neoskola credentials
- Neoskola course URL

## Usage

### Downloading a course with username and password

```python
from neoskola_dl.neoskola import NeoSkola

username = "your_username"
password = "your_password"
course_url = "https://neoskola.com/courses/your_course_url"

neoskola = NeoSkola(username, password)
neoskola.download_course(course_url)
```

### Downloading a course with token

```python
from neoskola_dl.neoskola import NeoSkola

token = "your_token"
course_url = "https://neoskola.com/courses/your_course_url"

neoskola = NeoSkola(token=token)
neoskola.download_course(course_url)
```