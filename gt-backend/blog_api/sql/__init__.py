from pathlib import Path

class _SQLCommands:
    def __getattr__(self, name):
        path = Path(__file__).parent / f"{name}.sql"
        if not path.exists():
            raise AttributeError(f"Command '{name}.sql' does not exist.")
        return path.read_text()

commands = _SQLCommands()