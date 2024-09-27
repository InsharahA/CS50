import sys
import requests
def main():
    try:
        n=float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit()
    except IndexError:
        print("Command-line argument missing")
        sys.exit()
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        res=r.json()
        rate=float(res.get("bpi").get("USD").get("rate_float"))
        amount=n*rate
        print(f"${amount:,.4f}")

    except requests.RequestException:
        print("Bad response")
        sys.exit()
main()