import random
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile


def convert_to_camel_case(string: str) -> str:
    return string.title().replace("-", "").replace("_", "")


def download(url: str) -> None:
    content, _ = urlretrieve(url)

    with ZipFile(content) as archive:
        archive.extractall()

    return get_archive_subdirectory_name(url)


def entity_matches_one_of_patterns(entity: Path, patterns: list[str]) -> bool:
    return any(entity.match(pattern) for pattern in patterns)


def generate_secret_key() -> str:
    chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
    return "django-insecure-" + "".join(random.choice(chars) for _ in range(50))


def get_archive_subdirectory_name(url: str) -> str:
    url = url.replace("://", "").split("/")
    repo = url[2]
    branch = url[4].replace(".zip", "")
    return f"{repo}-{branch}"


def is_url(path: str) -> bool:
    return "https" in path
