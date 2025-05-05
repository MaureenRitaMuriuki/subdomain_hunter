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
        full_domain = f"{sub}.{target}"
        print(f"Testing: {full_domain}")
        if is_alive(full_domain):
            print(f"[+] Found: {full_domain}")
            discovered.append(full_domain)

    if discovered:
        with open(output_file, "w") as f:
            json.dump(discovered, f, indent=2)
        print(f"\n[+] Results saved to {output_file}")
    else:
        print("\n[-] No subdomains found.")

if __name__ == "__main__":
    main()
