from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from browser_extension import ChromeExtension


class Config:
    def __init__(self, chunk_size=256):
        chromedriver = ChromeDriverManager()
        react_dev_tools = 'https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi'
        chrome_version = chromedriver.driver.get_browser_version()
        react_dev_tools_crx_path = ChromeExtension(react_dev_tools, chrome_version).download()

        self.chunk_size = chunk_size
        self.chrome_driver_path = chromedriver.install()

        self.chrome_options = Options()
        self.chrome_options.add_extension(react_dev_tools_crx_path)
        self.chrome_options.add_argument('--auto-open-devtools-for-tabs')

        self.main_url = "https://www.neoskola.com/"
        self.logout_url = "https://www.neoskola.com/hoscakalin"
