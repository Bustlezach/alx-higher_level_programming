#!/bin/bash
# This script gets the body size of a request
curl -si "$1" | grep -i content-length | cut -f2 -d' '
