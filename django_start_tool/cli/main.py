import argparse
from pathlib import Path

from django_start_tool import __version__
from django_start_tool.handler import TemplateHandler


DEFAULT_TEMPLATE = str(Path(__file__).parent.parent / "template")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="django-start",
        description="A full-featured CLI for quickly creating django projects.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
    )
    parser.add_argument(
        "name",
        nargs="?",
        default="config",
        help="Name of the project. "
             "Defaults to \"config\"",
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Optional destination directory. "
             "Defaults to \".\"",
    )
    parser.add_argument(
        "-t", "--template",
        default=DEFAULT_TEMPLATE,
        help="The path or URL to load the template from. "
             "Supports only GitHub URLs.",
    )
    parser.add_argument(
        "-r", "--render",
        action="extend",
        default=["*-tpl"],
        type=str.split,
        help="The file glob pattern(s) to render. "
             "Separate multiple patterns with spaces. "
             "In addition to \"*-tpl\"",
        dest="to_render",
    )
    parser.add_argument(
        "-x", "--exclude",
        action="extend",
        default=[".git", "__pycache__"],
        type=str.split,
        help="The directory glob pattern(s) to exclude. "
             "Separate multiple patterns with spaces. "
             "In addition to \".git\" and \"__pycache__\"",
        dest="to_exclude",
    )

    args = parser.parse_args()

    handler = TemplateHandler(
        name=args.name,
        to_render=args.to_render,
        to_exclude=args.to_exclude,
    )
    handler.run(args.template, args.directory)
