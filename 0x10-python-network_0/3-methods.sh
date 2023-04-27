#!/bin/bash
# This script display all HTTP methods the server will accept
curl -Is "$1" | grep -i Allow | cut -c 8-
