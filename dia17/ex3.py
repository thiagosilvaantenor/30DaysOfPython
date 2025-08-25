#!/usr/bin/env python3
# 3) Print the following dictionary using the format method and ** unpacking.
country = {
"name": "Germany",
"population": "83 million",
"capital": "Berlin",
"currency": "Euro"
}

print('{name} - {population} - {capital} - {currency}'.format(**country))

