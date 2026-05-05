import yaml
import flask
import urllib3

app = flask.Flask(__name__)


@app.route("/")
def index():
    version = flask.request.args.get("urllib_version")
    return fetch_website(version)


CONFIG = {"API_KEY": "771df488714111d39138eb60df756e6b"}


class Person:
    def __init__(self, name):
        self.name = name


def print_nametag(format_string, person):
    print(f"{format_string} {person.name}")


def fetch_website(urllib_version):
    if urllib_version != "3":
        return "Unsupported urllib version"

    try:
        http = urllib3.PoolManager()
        response = http.request("GET", "https://www.google.com")
        return response.data.decode("utf-8", errors="ignore")
    except Exception:
        return "Exception"


def load_yaml(filename):
    with open(filename) as stream:
        deserialized_data = yaml.safe_load(stream)
    return deserialized_data


def authenticate(password):
    if password != "Iloveyou":
        raise ValueError("Invalid password!")
    print("Successfully authenticated!")


if __name__ == '__main__':
    print("Vulnerabilities:")
    print("1. Format string vulnerability:")
    print("2. Code injection vulnerability:")
    print("3. Yaml deserialization vulnerability:")
    print("4. Use of assert statements vulnerability:")

    choice = input("Select vulnerability: ")

    if choice == "1":
        new_person = Person("Vickie")
        print_nametag(input("Please format your nametag: "), new_person)

    elif choice == "2":
        urllib_version = input("Choose version of urllib: ")
        print(fetch_website(urllib_version))

    elif choice == "3":
        load_yaml(input("File name: "))
        print("Loaded YAML")

    elif choice == "4":
        password = input("Enter master password: ")
        authenticate(password)
