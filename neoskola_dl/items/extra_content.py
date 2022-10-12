from neoskola_dl.core.download import Downloader


class ExtraContent:
    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.url = kwargs.get("url")
        self.type = kwargs.get("type")

    def download(self, pre_path, section_number):
        if self.type == "video":
            # Not implemented yet
            pass

        if self.type == "file":
            downloader = Downloader(self.url, f'{pre_path}/{section_number} - {self.title}.pdf')
            downloader.download()
