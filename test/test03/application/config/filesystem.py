from pathlib import Path

module_path = Path(__file__).parent.parent
templates_path = module_path.joinpath("templates")

project_path = Path(__file__).parent.parent.parent
db_path = project_path.joinpath("db_test")
