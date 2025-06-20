#!/bin/bash

# openssl genrsa 2048 > secret_2048.key | tee output.log
# openssl rsa -text < secret_2048.key | tee output.log

# openssl rsa -pubout < secret_2048.key > public_2048.key
# cat public_2048.key | tee output.log
echo -n "112233445566778899aabbccddeeff00" \
| xxd -pr -r \
| openssl pkeyutl -encrypt -pubin -inkey public_2048.key \
| hexdump -Cv | tee output.log