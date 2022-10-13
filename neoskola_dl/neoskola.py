from neoskola_dl.core import Auth
from neoskola_dl.items import Course


class NeoSkola:
    def __init__(self, token=None, email=None, password=None):
        self.auth = Auth(token=token, email=email, password=password)
        self.auth.login()

    def download_course(self, course_url):
        course = Course(course_url, self.auth)
        course.download()
