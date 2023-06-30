#!/bin/bash
#displays size of servers response body
curl -s $1 | wc -c
