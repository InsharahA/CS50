import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    match =re.search(r'<iframe[^>]*\s+src=["\'](https?://(?:www\.)?youtube\.com/embed/[^"\']+)["\'][^>]*></iframe>', s)
    
    if match:   
        return (match.group(1))
    else:
        return match


if __name__ == "__main__":
    main()