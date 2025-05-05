import requests
import dns.resolver
import json

wordlist_file = "wordlist.txt"
output_file = "vulnerable_services.json"

def load_wordlist():
    with open(wordlist_file, "r") as f:
        return [line.strip() for line in f if line.strip()]

def is_alive(subdomain):
    try:
        dns.resolver.resolve(subdomain, 'A')
        return True
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.resolver.Timeout):
        return False

def main():
    target = input("Enter a real target domain (e.g., uber.com): ").strip()
    subdomains = load_wordlist()
    discovered = []

    for sub in subdomains:
        subdomain = f"{sub}.{target}"
        print(f"Checking {subdomain}...")
        if is_alive(subdomain):
            discovered.append(subdomain)
            print(f"{subdomain} is live!")
        else:
            print(f"{subdomain} is dead.")

    if discovered:
        with open(output_file, "w") as f:
            json.dump(discovered, f, indent=4)
        print(f"Discovered subdomains saved to {output_file}")
    else:
        print("No subdomains were discovered.")

if __name__ == "__main__":
    main()

