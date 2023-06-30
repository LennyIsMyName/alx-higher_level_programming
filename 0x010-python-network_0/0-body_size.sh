#!/bin/bash
# displays size of servers response body
echo $(curl -s -o /dev/null -w "%{size_download}" "$1")
