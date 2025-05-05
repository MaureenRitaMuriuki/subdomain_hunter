# Subdomain Hunter

This project is designed to identify subdomains of a given domain. It uses a wordlist and performs DNS lookups to check if the subdomains are valid.

## Features

- Load subdomains from a wordlist.
- Check if subdomains exist via DNS lookup.
- Save the found subdomains in a JSON file.

## Usage

1. Edit the `wordlist.txt` file to include your target subdomains.
2. Run `subdomain_hunter.py` and input the target domain.
3. The found subdomains will be saved in `vulnerable_services.json`.

## Requirements

- `dnspython` (for DNS lookups)
- `requests` (for HTTP requests)
- `colorama` (for colorful output)
# subdomain_hunter
