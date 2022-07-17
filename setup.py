from setuptools import setup

setup(
    name="circles",
    version="0.0.1a",
    url="https://github.com/Kuro-Rui/Circles",
    license="GPLv3",
    author="Kuro-Rui",
    author_email="louisdominic80@gmail.com",
    description="An async osu! API v1 wrapper.",
    packages=["osu", "osu.errors", "osu.models"],
    setup_requires=["aiohttp"],
    keywords=["osu", "osu!", "osu!api"],
)