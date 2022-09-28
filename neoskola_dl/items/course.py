import time
from neoskola_dl.utils.course_utils import get_course_info
from neoskola_dl.items.extra_content import ExtraContent
from neoskola_dl.items.section import Section
from neoskola_dl.config import DOWNLOAD_PATH


class Course:
    def __init__(self, course_url, auth):
        self.id = None
        self.name = None
        self.course_url = course_url
        self.first_lesson_url = f'{course_url}/dersler-ve-bolumler/izle/ders-1-bolum-1'
        self.driver = auth.driver

        self.sections = []
        self.extra_contents = []

        self.get_course_info()

    def get_course_info(self):
        with self.driver as driver:
            driver.get(self.first_lesson_url)
            time.sleep(5)
            course_info = get_course_info(driver)['data']
        # import json
        # with open('test.json', 'r') as f:
        #     course_info = json.load(f)['data']
        self.id = course_info['course']['_id']
        self.name = course_info['course']['seoTitle']
        self.extra_contents = [ExtraContent(**extra_content) for extra_content in course_info['course']['extraContent']]
        self.sections = [Section(**section) for section in course_info['content']]

    def download(self):
        pre_path = f'{DOWNLOAD_PATH}/{self.name}'
        # Download extra contents
        for index_number, extra_content in enumerate(self.extra_contents):
            index_number += 1
            extra_content.download(f'{pre_path}/extra_contents', index_number)
        # Download sections
        for index_number, section in enumerate(self.sections):
            index_number += 1
            section.download(pre_path, index_number)
