import args
import whois # pip install python-whois

args = args.main()
domain = args.domain

def whois_domain(domain):
    try:
        w = whois.whois(domain)
        return w
    except:
        return None

main = whois_domain(domain)

if main:
    print(main)
else:
    print("Domain not found.")
