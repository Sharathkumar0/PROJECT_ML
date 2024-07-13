import setuptools

__version__ = "0.0.0"

REPO_NAME = "END-TO-END-ML-PROJECT"
AUTHOR_USER_NAME = "sharathkumar0"
SRC_REPO = "MLPROJECT"
AUTHOR_EMAIL = "sharath_0@yahoo.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)