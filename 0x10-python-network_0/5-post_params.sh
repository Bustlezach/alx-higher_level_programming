#!/bin/bash
# POSTs request to  URL,displays the body of the response
email=test@gmail.com
subject=I will always be here for PLD
curl -s -d "email=$email&subject=$subject" "$1"email='test@gmail.com'
