#!/bin/bash

if ! echo "$(snapctl get base-url)" | grep localhost > /dev/null 2>&1
then
	export APP_BASE_URL="$(snapctl get base-url)"
else
	export APP_BASE_URL="$(snapctl get base-url):"$(snapctl get joplin-port)""
fi

export APP_PORT="$(snapctl get joplin-port)"
export SQLITE_DATABASE=${SNAP_DATA}/db.sqlite

cd $SNAP/packages/server
node dist/app.js
