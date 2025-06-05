#!/usr/bin/env python3

import json
import requests

from pprint import pprint


# ---
params: dict[str, str] = {"access_token": "lip_DRS4U0s4YIsll0dMv5h2"}
hdr = {
    "Content-type": "application/x-ndjson",  # This is what you probably wanted
}

t_id = "KR9KTNuj"
r_id = "NmUtGXny"  # parsed from the info in /api/broadcast/{t_id}
# ---

clean = lambda txt: txt.replace("'", "").replace("[", "").replace("]", "")


def get_all_pgns(t_id, r_id):
    """
    Each game is a chess pgn separated by three new lines.
    """
    response = requests.get(
        f"https://lichess.org/api/broadcast/round/{r_id}.pgn",
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text
    games = text.split("\n\n\n")

    print(f"[INFO] Number of games: {len(games)}\n")
    for game in games:
        game = game.split("\n")
        if len(game) < 22:
            continue
        info = f"{clean(game[0])}, {clean(game[1])}"
        players = f"{clean(game[2])}\t\t\t{clean(game[3])}"
        print(f"[GAME INFO] \n" f"       {info}\n" f"       {players}")

    return response


def get_round_info(t_id, r_id):
    # hdr = { "Content-type": "application/json", }
    response = requests.get(
        f"https://lichess.org/api/broadcast/-/-/{r_id}",
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text
    pprint(response.text)

    return response


def get_broadcast_info(t_id):
    response = requests.get(
        f"https://lichess.org/api/broadcast/{t_id}",
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text
    pprint(response.text)

    return response


def get_all_official_broadcasts(top_broadcasts_only: bool = False):
    if top_broadcasts_only:
        request = f"https://lichess.org/api/broadcast/top"
    else:
        request = f"https://lichess.org/api/broadcast"

    response = requests.get(
        request,
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text
    pprint(response.text)

    return response


def get_game_stream(pgn):
    response = requests.get(
        f"https://lichess.org/api/broadcast/round/{pgn}.pgn",
        headers=hdr,
        params=params,
    )
    response.encoding = "utf-8"
    text = response.text
    pprint(response.text)

    return response


def main() -> None:
    pgn = "GdK93YSo"  # https://lichess.org/api/stream/broadcast/round/{broadcastRoundId}.pgn"
    # get_all_official_broadcasts()
    # get_round_info(t_id, r_id)
    get_all_pgns(t_id, r_id)


if __name__ == "__main__":
    main()
