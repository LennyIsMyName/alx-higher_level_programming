#!/usr/bin/bash
# displays size of server response body
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
