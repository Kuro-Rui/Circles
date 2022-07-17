from datetime import datetime, timezone
from typing import Dict


class User:
    def __init__(self, data: Dict):
        self.username = data["username"]
        self.user_id = int(data["user_id"])
        self.join_date = (
            datetime.strptime(data["join_date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        )
        self.count_300 = int(data["count300"]) if data["count300"] else 0
        self.count_100 = int(data["count100"]) if data["count100"] else 0
        self.count_50 = int(data["count50"]) if data["count50"] else 0
        self.playcount = int(data["playcount"]) if data["playcount"] else 0
        self.ranked_score = int(data["ranked_score"]) if data["ranked_score"] else 0
        self.total_score = int(data["total_score"]) if data["total_score"] else 0
        self.rank = int(data["pp_rank"]) if data["pp_rank"] else "Unknown"
        self.level = float(data["level"]) if data["level"] else 0
        self.pp = float(data["pp_raw"]) if data["pp_raw"] else 0
        self.accuracy = float(data["accuracy"]) if data["accuracy"] else 0
        self.ssh_count = int(data["count_rank_ssh"]) if data["count_rank_ssh"] else 0
        self.ss_count = int(data["count_rank_ss"]) if data["count_rank_ss"] else 0
        self.sh_count = int(data["count_rank_sh"]) if data["count_rank_sh"] else 0
        self.s_count = int(data["count_rank_s"]) if data["count_rank_s"] else 0
        self.a_count = int(data["count_rank_a"]) if data["count_rank_a"] else 0
        self.country = data["country"]
        self.seconds_played = (
            int(data["total_seconds_played"]) if data["total_seconds_played"] else 0
        )
        self.country_rank = int(data["pp_country_rank"]) if data["pp_country_rank"] else "Unknown"
        self.events = [Event(event) for event in data["events"]]

class Event:
    def __init__(self, data):
        self.display_html = data["display_html"]
        self.beatmap_id = int(data["beatmap_id"])
        self.beatmapset_id = int(data["beatmapset_id"])
        self.date = (
            datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc)
        )
        self.epic_factor = int(data["epicfactor"])