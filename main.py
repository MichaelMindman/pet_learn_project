import requests


def main():
    response = requests.get("https://api.github.com")
    print(f"Status: {response.status_code}")
    print("Hello from virtual enviroment!")


if __name__ == "__main__":
    main()
