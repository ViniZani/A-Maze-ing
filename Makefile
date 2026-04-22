SHELL := /bin/sh


VENV_DIR := .venv
PYTHON   := $(VENV_DIR)/bin/python
PIP      := $(VENV_DIR)/bin/pip
FLAKE8   := $(VENV_DIR)/bin/flake8
MYPY     := $(VENV_DIR)/bin/mypy
BUILD    := -m build


all: run


install:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install python-dotenv
	$(PIP) install flake8 mypy build
	$(PIP) install -e .

build:
	$(PIP) install build
	$(PYTHON) -m build

run:
	$(PYTHON) a_maze_ing.py config.txt


debug:
	$(PYTHON) -m pdb a_maze_ing.py config.txt


lint:
	$(FLAKE8) --exclude $(VENV_DIR)
	$(MYPY) . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(FLAKE8) --exclude $(VENV_DIR)
	$(MYPY) . --strict


clean:
	rm -rf __pycache__ .mypy_cache .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +


fclean: clean
	rm -rf $(VENV_DIR) dist *.egg-info build
	rm -f *.whl *.tar.gz


package: fclean
	$(PYTHON) $(BUILD)
	cp dist/*.whl .
	cp dist/*.tar.gz .

re: fclean install

.PHONY: all install run debug clean fclean lint lint-strict re package

