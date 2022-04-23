import pyshorteners

url = input("Enter a URL: ")

def shorten(url):
    print(pyshorteners.Shortener().tinyurl.short(url))

if __name__ == '__main__':
    shorten(url)
