import argparse
import requests


class SmhiParser:
    """
    Class to handle communication with and extract data from the SMHI Open API.
    """
    BASE_URL = "https://opendata-download-metobs.smhi.se/api"

    def __init__(self, suffix=".json"):
        self.suffix = suffix

    def _make_request(self, path=""):
        full_path = self.BASE_URL + path + self.suffix
        r = requests.get(full_path)
        return r

    def check_connection(self):
        r = self._make_request()
        return r.status_code


def main():
    parser = argparse.ArgumentParser(
        description="""Script to extract data from SMHI's Open API"""
    )
    parser.add_argument("--parameters", help="Parameters to download data for")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
