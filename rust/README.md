# Lichess CLI

So you can watch chess broadcasts from your terminal without your boss
noticing.

---

Basic functionality to implement:

  - Get a [list of all live broadcasts happening on
  lichess.](https://lichess.org/api#tag/Arena-tournaments/operation/apiTournamentUpdate)
  `GET /api/broadcast`
  `GET /api/broadcast/top`
  - Take fen from return json and format into a live updating cli application with extra information
  to visualize a chess board, last player time, who to move, castle yes/no, ...
  - TUI to make browsing nice
    - Colors!

