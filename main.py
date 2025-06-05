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


def get_all_boards(t_id, r_id):
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

    fen_response = get_round_info(t_id, r_id)
    rnd_info = fen_response.json()
    rnd_info = rnd_info["games"]

    games = tuple(zip(rnd_info, games[: len(rnd_info)]))

    print(f"[INFO] Number of games: {len(games)}\n")
    for r, game in games:
        fen = r["fen"]
        game = game.split("\n")

        """
        format for `game`
            [
              0.  '[Event "Norway Chess 2025"]',
              1.  '[Site "Stavanger, Norway"]',
              2.  '[Round "3.2"]',
              3.  '[White "Nakamura, Hikaru"]',
              4.  '[Black "Carlsen, Magnus"]',
              5.  '[Result "1/2-1/2"]',
              6.  '[WhiteElo "2804"]',
              7.  '[WhiteTitle "GM"]',
              8.  '[WhiteFideId "2016192"]',
              9.  '[BlackElo "2837"]',
              10.  '[BlackTitle "GM"]',
              11.  '[BlackFideId "1503014"]',
              12.  '[Variant "Standard"]',
              13.  '[ECO "C77"]',
              14.  '[Opening "Ruy Lopez: Morphy Defense, Anderssen Variation"]',
              15.  '[StudyName "Round 2"]',
              16.  '[ChapterName "Nakamura, Hikaru - Carlsen, Magnus"]',
              17.  '[UTCDate "2025.05.26"]',
              18.  '[UTCTime "13:41:30"]',
              19.  '[GameURL "https://lichess.org/broadcast/-/-/8Ma8Q5pQ"]',
              20.  '',
              21.  '1. e4 { [%clk 1:59:33] } 1... e5 (and more pgn stuff until end of game) 1/2-1/2'
            ]
        """

        info = f"{clean(game[0])}, {clean(game[1])}"
        players = f"{clean(game[2])}\t\t\t{clean(game[3])}"
        pgn = game[-1]

        print(f"[GAME INFO] \n" f"       {info}\n" f"       {players}")
        print(f"\t{fen=}\n===")

        # tmp
        print(game[20])

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
    get_all_boards(t_id, r_id)


if __name__ == "__main__":
    main()
