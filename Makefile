
up_require:
	pip install -r mirrors/requirements.txt

up_dev_require:
	pip install -r mirrors/requirements-dev.txt

test:
	CODE_ENV=test pytest --rootdir ./tests -s

run:
	uvicorn main:app --reload
