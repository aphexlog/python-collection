import whois # pip install python-whois

def whois_domain(domain):
    try:
        w = whois.whois(domain)
        return w
    except:
        return None

main = whois_domain('google.com')

if main:
    print(main)
else:
    print("Domain not found.")
