#!/bin/bash
# This script displays the size of the body of the response
curl -si  https://example.com | grep -i content-length | cut -f2 -d' '
