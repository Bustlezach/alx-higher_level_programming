#bin/bash
# Display all HTTP methods the server will accept
curl -sI X OPTIONS "$1"
