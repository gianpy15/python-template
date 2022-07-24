SRC_DIR		= src
TEST_DIR	= tests
CHECK_DIRS = $(SRC_DIR) $(TEST_DIR)
DOCS_DIR 	= docs

.PHONY: install
install: poetry run pip install --upgrade pip
	poetry install -v

.PHONY: check
check: format-check lint type-check test ## Launch all the checks (formatting, linting, type checking)

.PHONY: update
update: ## Update python dependencies
	poetry update

.PHONY: format
format: ## Format repository code
	poetry run black $(CHECK_DIRS)
	poetry run isort $(CHECK_DIRS)

.PHONY: check
format-check: ## Check the code format with no actual side effects
	poetry run black --check $(CHECK_DIRS)
	poetry run isort --check $(CHECK_DIRS)

.PHONY: lint
lint: ## Launch the linting tool
	poetry run pylint -j 0 $(SRC_DIR).{{cookiecutter.project_name}}
	poetry run pylint -j 0 -d missing-function-docstring $(TEST_DIR)

.PHONY: type-check
type-check: ## Launch the type checking tool
	poetry run mypy --ignore-missing-imports $(CHECK_DIRS)

.PHONY: test
test: ## Launch the tests
	poetry run pytest -vv tests

.PHONY: clean
clean: ## Clean the repository
	rm -rf dist
	rm -rf *.egg-info

.PHONY: help
help: ## Show the available commands
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

