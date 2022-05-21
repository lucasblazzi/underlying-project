import os
from elasticsearch import AsyncElasticsearch
from elasticsearch.helpers import async_bulk

ES_HOST = os.environ.get("ES_HOST", "https://search-underlying-zpfrcbjukmsi3otoeaohoemdu4.us-east-1.es.amazonaws.com")


class ES:
    def __init__(self, index):
        self.session = None
        self.index = index

    async def __aenter__(self):
        self.session = AsyncElasticsearch(ES_HOST, port=443)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def bulk(self, data):
        parsed = [{"_index": self.index, "doc": d} for d in data]
        await async_bulk(self.session, parsed)

    async def query(self, query, size=10):
        resp = await self.session.search(
            index=self.index,
            body=query,
            size=size,
        )
        return resp

