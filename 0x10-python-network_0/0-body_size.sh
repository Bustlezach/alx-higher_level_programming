#!/bin/bash
# This script displays the size of the body of the response
curl -si '$1' | grep -i content-length | cut -f2 -d' '
