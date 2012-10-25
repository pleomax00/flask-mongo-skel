#! /usr/bin/env sh
spawning -d --stderr="`pwd`/logs/stderr.log" --stdout="`pwd`/logs/stdout.log" wsgi.application --port 8765 -s 5 -t 0 --deadman=20 --reload=dev --max-age=30
