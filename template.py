from tortoise.backends.base.client import BaseDBAsyncClient


async def upgrade(conn: BaseDBAsyncClient):
    pass


async def downgrade(conn: BaseDBAsyncClient):
    pass
