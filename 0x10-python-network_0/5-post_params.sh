#!/bin/bash
# POSTs request to URL, displays the body of the response
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
