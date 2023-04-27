#!/bin/bash
# This script displays the size of the body of the response
curl '$1' | wc -c
