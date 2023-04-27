#bin/bash
# Display all HTTP methods the server will accept
curl -sI "$1" | grep -i "ALLOW" | cut d''
