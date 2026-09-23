import requests


def train_hot_key():

    print("train_hot_keys")
    print("train_hot_keys")
    print("train_hot_keys")


def main():
    response = requests.get("https://api.github.com")
    print(f"Status: {response.status_code}")
    print("Hello from virtual enviroment!")

    train_hot_key()


if __name__ == "__main__":
    main()
