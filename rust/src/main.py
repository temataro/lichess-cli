#!/usr/bin/env python3

import requests


def main() -> None:
    params: dict[str, str] = {"access_token": "lip_DRS4U0s4YIsll0dMv5h2"}

    response = requests.get(
        "https://lichess.org/api/broadcast",
        headers={"Content-type": "application/json"},
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text

    print(text.split(","), end="\n")


if __name__ == "__main__":
    main()
