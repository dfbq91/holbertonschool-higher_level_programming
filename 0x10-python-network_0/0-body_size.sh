#!/bin/bash
# Get content-lenght response of a request to an URL
curl -sI "$1" | grep -i "content-length:" | tr -d " \t" | cut -d ':' -f 2
