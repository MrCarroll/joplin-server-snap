#!/bin/bash

if [[ "$(snapctl get proxy-enabled)" -ne "1" ]]
then
	exit 0
fi

if echo "$(snapctl get base-url)" | grep localhost
then
	exit 0
fi

caddy reverse-proxy --from "$(snapctl get base-url)" --to http://localhost:"$(snapctl get joplin-port)"
