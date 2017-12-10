.PHONY: all help refresh test clean collect update_pip deploy update_db

LOCALPATH := ./web
PYTHONPATH := ${LOCALPATH}/
PYTHON_BIN := $(VIRTUAL_ENV)/bin/python

PROJECT := codeproject
DJANGO_SETTINGS_MODULE=${PROJECT}.settings
DJANGO_TEST_SETTINGS_MODULE=${PROJECT}.test_settings
DJANGO_POSTFIX := --settings=$(DJANGO_SETTINGS_MODULE)
DJANGO_TEST_POSTFIX := --settings=$(DJANGO_TEST_SETTINGS_MODULE)
VIRTUALENV_ACTIVATE := source venv/bin/activate;

# target: all - Default target. Does nothing.
all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: translate - calls the "makemessages" django command
#translate:
#	cd {{ project_name }} && django-admin.py makemessages --settings=$(SETTINGS) -i "static/*" -a --no-location

# target: clean - Removes pyc, htmlcov, .coverage and egg-info files.
clean:
	find ${LOCALPATH} -name "*.pyc" -print0 | xargs -0 rm -rf
	rm -rf ${LOCALPATH}/htmlcov
	rm -rf ${LOCALPATH}/.coverage
	-rm -rf ${LOCALPATH}/*.egg-info

# target: test - calls the "test" django command
test: clean
	(\
	${VIRTUALENV_ACTIVATE}\
	cd ${LOCALPATH}; \
	python manage.py test ${DJANGO_TEST_POSTFIX}\
	)

# target: coverage - Runs the tests with coverage reports.
coverage: clean
	( \
	${VIRTUALENV_ACTIVATE} \
	cd ${LOCALPATH}; \
	coverage run --source='.' manage.py test ${DJANGO_TEST_POSTFIX}; \
	coverage report; \
	)

# target: refresh - Touches the wsgi file to reload the server.
refresh:
	touch ${LOCALPATH}/$(PROJECT)/*wsgi.py

# target: update_pip - install (and update) pip requirements
update_pip:
	(\
	${VIRTUALENV_ACTIVATE}\
	pip install -U -r requirements.txt\
	)

# target: collect - Collects all the static files.
collect:
	mkdir -p $(LOCALPATH)/static
	(\
	${VIRTUALENV_ACTIVATE}\
	cd ${LOCALPATH}; \
	python manage.py collectstatic -c --noinput $(DJANGO_POSTFIX) \
	)

# target: deploy - Updates pip, collects the static files and touches the wsgi.py.
deploy: update_pip collect refresh

# target: update_db - Generates the migration files and migrates.
update_db:
	(\
	${VIRTUALENV_ACTIVATE}\
	cd ${LOCALPATH}; \
	python manage.py makemigrations --noinput $(DJANGO_POSTFIX); \
	python manage.py migrate --noinput $(DJANGO_POSTFIX); \
	)