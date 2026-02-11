.PHONY: install run debug clean lint lint-strict package

install:
	pip install --upgrade pip
	pip install flake8 mypy build types-setuptools

run:
	python3 a_maze_ing.py config.txt

debug:
	python3 -m pdb a_maze_ing.py config.txt

clean:
	rm -rf __pycache__ .mypy_cache
	rm -rf mazegen/__pycache__
	rm -rf build dist *.egg-info
	rm -f maze.txt

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

package:
	python3 -m build
