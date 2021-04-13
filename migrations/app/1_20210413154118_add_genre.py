import urllib.request
import json

from tortoise.backends.base.client import BaseDBAsyncClient


def get_genres():
    url = "https://raw.githubusercontent.com/voltraco/genres/master/genres.json"
    req = urllib.request.Request(url)
    return json.load(urllib.request.urlopen(req))


async def upgrade(conn: BaseDBAsyncClient):
    genres = get_genres()

    await conn.execute_many("""
        INSERT INTO "genre" ("name")
        VALUES ($1)
    """, [[g] for g in genres])


async def downgrade(conn: BaseDBAsyncClient):
    genres = get_genres()

    await conn.execute_query("""
        DELETE FROM "genre"
        WHERE "name" = ANY($1::text[])
    """, [genres])
