#!/usr/bin/env bash

python manage.py runserver &
id=$?
python manage.py celeryd -v 2 -B -s celery -E -l INFO
kill $id