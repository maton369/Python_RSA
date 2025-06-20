#!/bin/bash

# openssl genrsa 2048 > secret_2048.key | tee output.log
# openssl rsa -text < secret_2048.key | tee output.log

openssl rsa -pubout < secret_2048.key > public_2048.key
cat public_2048.key | tee output.log