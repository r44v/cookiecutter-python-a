import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="a", format="%(asctime)s\t%(name)s\t%(levelname)s\t%(pathname)s|%(lineno)d\t%(message)s")
logger = logging.getLogger("{{cookiecutter.package_name}}Logger")

def start():
	print("Hello World!")

start()
