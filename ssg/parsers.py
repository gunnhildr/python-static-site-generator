import shutil
from typing import List, AnyStr
from pathlib import Path


class Parse:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError

    def read(self, path: Path):
        with path.open("r") as file:
            return file.read()

    def write(self,  path: Path, dest: Path, content: AnyStr):
        full_path = dest / path.with_suffix("ext").name
        with full_path.open("w") as file:
            file.write(content)

    def copy(self, path: Path, source: Path, dest: Path):
        shutil.copy2(path, dest / path.relative_to(source))


class ResourceParser(Parse):
    extensions = [".jpg", ".png", ".gif", ".css",  ".html"]

    def parse(self, path: Path, source: Path, dest: Path):
        self.copy(path, source, dest)

