#!/bin/bash

read -p "Enter new API key: " new_api_key
sed -i 's/"x-api-key": ".*"/"x-api-key": "'"$new_api_key"'"/g' dox.py
