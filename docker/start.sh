#!/bin/bash

cd /app

# set server environment
if [ "${SERVER_ENVIRONMENT:0:3}" == "dev" ]; then
  export SERVER_ENVIRONMENT=dev
elif [ "${SERVER_ENVIRONMENT:0:4}" == "test" ]; then
  export SERVER_ENVIRONMENT=test
elif [ "${SERVER_ENVIRONMENT:0:4}" == "prod" ]; then
  export SERVER_ENVIRONMENT=prod
else
  echo "*** SERVER_ENVIRONMENT must *begin* with one of: dev, test, prod ***"
  exit 1
fi
echo "Using SERVER_ENVIRONMENT: '$SERVER_ENVIRONMENT'"

if [ "$SERVER_ENVIRONMENT" = "dev" ]; then
  exec python3 manage.py runserver 0.0.0.0:$PROJECT_PORT_INTERNAL
elif [ "$SERVER_ENVIRONMENT" = "test" ] || [ "$SERVER_ENVIRONMENT" = "prod" ]; then
  exec gunicorn \
    --bind 0.0.0.0:$PROJECT_PORT_INTERNAL \
    --workers 1 \
    --log-level DEBUG \
    --access-logfile "-" \
    --error-logfile "-" \
    $PROJECT_NAME_PYTHON.wsgi
else
  echo "*** SERVER_ENVIRONMENT must begin with one of: dev, test, prod ***"
  exit 1
fi
