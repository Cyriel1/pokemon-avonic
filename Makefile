SHELL:=/bin/bash
terminal_venv:=source venv/Scripts/activate

create_venv:
	python -m venv ./venv

create_data:
	python ./app/data/fixtures.py

update_dependencies:
	$(terminal_venv); \
	pip freeze > requirements.txt

install_dependencies:
	$(terminal_venv); \
	pip install -r requirements.txt

test_runner:
	python -m unittest discover -v tests

executable:
	$(terminal_venv); \
	pyinstaller -y ./pokemon_avonic_app.spec

package:
	$(terminal_venv); \
	python setup.py sdist bdist

clean:
	rm -rf __pycache__
	rm -rf venv
