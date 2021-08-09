#!/usr/bin/env sh

set -e

celery -A app.worker worker -l DEBUG -c 4 -Q main-queue -n worker@localhost --logfile=logs/%p.log
