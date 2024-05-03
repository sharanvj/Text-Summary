import setuptools

with open("README.md","r", encoding="utf-8") as f:
    description = f.read()

__version__="0.0.0"

REPO_NAME = "Text-Summary"
AUTHOR = "sharanvj"
AUTHOR_MAIL = "sharan11vijay@gmail.com"
SRC_REPO = "TextSummary"

setuptools.setup(name=SRC_REPO,
                 version=__version__,
                 author=AUTHOR,
                 author_email=AUTHOR_MAIL,
                 description="Text Summarization - NLP App", 
                 long_description= description,
                 long_description_content_type="text/markdown",
                 url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
                 project_urls = { "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",},
                 package_dir={"":"src"},
                 packages=setuptools.find_packages(where="src")
                 )