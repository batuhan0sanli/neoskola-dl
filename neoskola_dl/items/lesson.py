from neoskola_dl.core.download import Downloader
from neoskola_dl.core.save_file import SaveFile
from neoskola_dl.config import DOWNLOAD_OPTION


class Video:
    def __init__(self, **kwargs):
        self.duration = kwargs['durationSeconds']

        self.url_mp3 = kwargs['mp3Url']
        self.url_360p = kwargs['url360p']
        self.url_540p = kwargs['url540p']
        self.url_720p = kwargs['url720p']
        self.url_1080p = kwargs['url1080p']
        self.url_live_stream = kwargs['urlLiveStreaming']

    def download(self, pre_path):
        for option in DOWNLOAD_OPTION:
            extension = 'mp3' if option == 'mp3' else 'mp4'
            downloader = Downloader(getattr(self, f'url_{option}'), f'{pre_path}.{extension}')
            downloader.download()


class Quiz:
    def __init__(self, **kwargs):
        self.questions = kwargs['questions']

    def download(self, pre_path):
        content = ''
        for question_obj in self.questions:
            question = question_obj.pop('question')
            correct_option = question_obj.pop('correctOption')

            options = question_obj.values()
            correct_answer = question_obj[correct_option]
            content += f'{question}\n'
            for option in options:
                content += f'\t{option}\n'
            content += f'\tCorrect answer: {correct_answer}\n\n'
        SaveFile(f'{pre_path}.txt', content).save()


class Lesson:
    def __init__(self, **kwargs):
        self.id = kwargs['_id']
        self.name = kwargs['title']
        self.type = 'video' if 'durationSeconds' in kwargs else 'quiz'
        self.lesson = Video(**kwargs) if self.type == 'video' else Quiz(**kwargs)

    def download(self, pre_path):
        pre_path = f'{pre_path}/{self.name}'
        self.lesson.download(pre_path)
