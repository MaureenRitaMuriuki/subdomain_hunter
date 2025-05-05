import requests
import dns.resolver
import json
import os

# Global variables
wordlist_path = 'wordlist.txt'
vulnerable_services_path = 'vulnerable_services.json'

def load_wordlist():
    """Load subdomains from wordlist.txt"""
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def check_subdomain(subdomain, domain):
    """Check if a subdomain is valid"""
    try:
        full_domain = f"{subdomain}.{domain}"
        dns.resolver.resolve(full_domain, 'A')  # Resolving the A record for DNS
        print(f"[+] Found subdomain: {full_domain}")
        return full_domain
    except dns.resolver.NoAnswer:
        pass
    except dns.resolver.NXDOMAIN:
        pass

def main():
    # Ask for domain or default to 'uber.com'
    domain = input("Enter the target domain (default: uber.com): ") or 'uber.com'
    print(f"Scanning for subdomains on {domain}...\n")

    subdomains = load_wordlist()
    
    # Search for subdomains
    found_subdomains = []
    for subdomain in subdomains:
        full_domain = check_subdomain(subdomain, domain)
        if full_domain:
            found_subdomains.append(full_domain)

    # Output the results
    if found_subdomains:
        print("\n[+] Subdomains found:")
        for sub in found_subdomains:
            print(sub)

        # Save the results to a JSON file
        with open(vulnerable_services_path, 'w') as file:
            json.dump(found_subdomains, file, indent=4)
        print(f"[+] Subdomains saved to {vulnerable_services_path}")
    else:
        print("[!] No subdomains found")

if __name__ == "__main__":
    main()
