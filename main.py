#!/usr/bin/env python3

import json
import requests


pgn = (
    "GdK93YSo"  # https://lichess.org/api/stream/broadcast/round/{broadcastRoundId}.pgn"
)


def main() -> None:
    params: dict[str, str] = {"access_token": "lip_DRS4U0s4YIsll0dMv5h2"}
    hdr = {
        "Content-type": "application/x-chess-pgn",  # This is what you probably wanted
    }
    response = requests.get(
        f"https://lichess.org/api/broadcast/round/{pgn}.pgn",
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text

    # json_print = lambda response: print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    # print(response.json()) # , indent=2, ensure_ascii=False))
    print(text)


if __name__ == "__main__":
    main()
