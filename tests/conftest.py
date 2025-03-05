import os

import pytest

from zipfile import ZipFile


CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
CURRENT_PROJECT_PATH = os.path.dirname(CURRENT_DIR)
SRC_PATH = os.path.join(CURRENT_PROJECT_PATH, "src")
ARCHIVE_FILE_PATH = os.path.join(SRC_PATH, "archive.zip")


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    with ZipFile(ARCHIVE_FILE_PATH, 'w') as zip_file:
        for file in os.listdir(SRC_PATH):
            zip_file.write(os.path.join(SRC_PATH, file), file)

    yield

    if os.path.exists(ARCHIVE_FILE_PATH):
        os.remove(ARCHIVE_FILE_PATH)