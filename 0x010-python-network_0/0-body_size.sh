#!/usr/bin/bash
# displays size of server response body
echo $(curl -s -0 /dev/null -w "%size_download}" "$1")
