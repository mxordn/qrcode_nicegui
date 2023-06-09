#!/usr/bin/env bash

# use path of this example as working directory; enables starting this script from anywhere
cd "$(dirname "$0")"

if [ "$1" = "prod" ]; then
    echo "Starting Uvicorn server in production mode..."
    # we also use a single worker in production mode so socket.io connections are always handled by the same worker
    uvicorn qrcode_api:qrcode_app --workers 1 --log-level info --root-path='/qrcode' --host 0.0.0.0 --port 8080
elif [ "$1" = "dev" ]; then
    echo "Starting Uvicorn server in development mode..."
    # reload implies workers = 1
    uvicorn qrcode_api:qrcode_app --reload --log-level debug --root-path='/qrcode' --host 0.0.0.0 --port 8080
else
    echo "Invalid parameter. Use 'prod' or 'dev'."
    exit 1
fi
