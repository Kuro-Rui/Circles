import aiohttp
import asyncio
import logging
import time
from typing import Dict, Literal, Optional

from osu.errors import InvalidKey, UserNotFound
from osu.models import User

log = logging.getLogger(__name__)


class Circles:
    """
    An async osu! API v1 wrapper.

    Attributes
    ----------
    api_key: str
        The API key to use for requests.
        This is required and can be get from https://osu.ppy.sh/p/api/

    session: Optional[aiohttp.ClientSession]
        The client session used to make requests to the osu! API.
    """

    BASE_URL = "https://osu.ppy.sh/api/"
    ENDPOINT = Literal[
        "get_beatmaps",
        "get_match",
        "get_replay",
        "get_user",
        "get_user_best",
        "get_user_recent",
        "get_scores",
    ]
    MAX_REQUESTS, MAX_REQUESTS_PERIOD = 1200, 60
    MODE = Literal["Standard", "Taiko", "Catch The Beat", "Mania"]
    MODES = {"Standard": 0, "Taiko": 1, "Catch The Beat": 2, "Mania": 3}

    def __init__(self, api_key: str, *, session: Optional[aiohttp.ClientSession] = None):
        self.key = api_key
        self.requests = []
        self.session = session or aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def check_ratelimit(self):
        while len(self.requests) > self.MAX_REQUESTS:
            self.requests = [
                request
                for request in self.requests
                if time.time() - request < self.MAX_REQUESTS_PERIOD
            ]
            if len(self.requests) > self.MAX_REQUESTS:
                await self.wait_until_ratelimit_reset()

    async def wait_until_ratelimit_reset(self):
        wait_time = self.MAX_REQUESTS_PERIOD - (time.time() - min(self.requests))
        log.warning(f"We are being ratelimited, waiting for {round(wait_time)} seconds.")
        await asyncio.sleep(wait_time)

    async def request(self, endpoint: ENDPOINT, *, params: Dict = {}) -> Dict:
        await self.check_ratelimit()
        params["k"] = self.key
        async with self.session.request(
            method="POST", url=self.BASE_URL + endpoint, params=params
        ) as response:
            self.requests.append(time.time())
            result = await response.json()
            if response.status != 200:
                raise InvalidKey()
            if not result:
                raise UserNotFound()
            return result

    async def get_user(self, username: str, *, mode: MODE) -> User:
        users = await self.request("get_user", params={"u": username, "m": self.MODES[mode]})
        if not users:
            raise UserNotFound()
        return User(users[0])
