import {{cookiecutter.project_name}}
from pathlib import Path

import tomlkit


def test_package_version_equal_poetry():
    toml_path = Path(Path(__file__).parent.parent, "pyproject.toml")
    with toml_path.open(encoding="utf-8") as toml_file:
        poetry_version = tomlkit.loads(toml_file.read())["tool"]["poetry"]["version"]  # type: ignore
        assert {{cookiecutter.project_name}}.__version__ == poetry_version