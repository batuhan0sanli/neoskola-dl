from neoskola_dl.items.lesson import Lesson


class Section:
    def __init__(self, **kwargs):
        self.name = kwargs['sectionTitle']
        self.lessons = [Lesson(**lesson) for lesson in kwargs['items']]

    def download(self, pre_path, section_number):
        pre_path = f'{pre_path}/{section_number} - {self.name}'
        for lesson in self.lessons:
            lesson.download(pre_path)
