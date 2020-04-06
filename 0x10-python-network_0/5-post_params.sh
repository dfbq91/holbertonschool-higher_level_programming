#!/bin/bash
# Sends a GET request to an URL, and displays the body of the response
curl -s -X POST "$1" -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
