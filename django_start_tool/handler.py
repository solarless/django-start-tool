from pathlib import Path
import shutil

from jinja2 import Template

from django_start_tool.utils import download
from django_start_tool.utils import entity_matches_one_of_patterns
from django_start_tool.utils import generate_secret_key
from django_start_tool.utils import is_url


class TemplateHandler:
    def __init__(
        self,
        name: str,
        to_render: list[str],
        to_exclude: list[str],
    ) -> None:
        self.name = name
        self.to_render = to_render
        self.to_exclude = to_exclude
        self.template_context = {
            "project_name": name,
            "secret_key": generate_secret_key()
        }

    def run(self, source: str, destination: str) -> None:
        if source_is_url := is_url(source):
            source = download(source)

        source = Path(source)
        destination = Path(destination)
        self.handle_tree(source, destination)

        if source_is_url:
            shutil.rmtree(source)

    def handle_tree(self, source: Path, destination: Path) -> None:
        for entity in source.iterdir():
            if entity.is_dir():
                self.handle_directory(entity, destination / entity.name)

            elif entity.is_file():
                self.handle_file(entity, destination / entity.name)

    def handle_directory(self, source: Path, destination: Path) -> None:
        if entity_matches_one_of_patterns(source, self.to_exclude):
            return None

        destination = destination.with_name(
            source.name.replace("project_name", self.name)
        )
        self.handle_tree(source, destination)

    def handle_file(self, source: Path, destination: Path) -> None:
        if entity_matches_one_of_patterns(source, self.to_render):
            file_content = self.render_file(source)
        else:
            file_content = source.read_text()

        destination = destination.with_name(
            source.name.replace("-tpl", "")
        )
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.touch(exist_ok=True)
        destination.write_text(file_content)

    def render_file(self, file: Path) -> str:
        template = Template(file.read_text())
        size = file.stat().st_size
        eof = ['', '\n'][size > 0]
        return template.render(**self.template_context) + eof
