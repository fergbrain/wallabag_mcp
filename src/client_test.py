import asyncio
import json

from dotenv import load_dotenv
from wallabag_client import WallabagClient, GetSingleArticleRequest, Article


async def main():
    load_dotenv()

    client = WallabagClient()

    await client.authenticate()
    print("Authenticated successfully.")

    request = GetSingleArticleRequest(id=59)

    article = await client.get_single_article(request)
    print(f"Fetched article: [{article.id}] {article.title} ({article.url})")


if __name__ == "__main__":
    asyncio.run(main())
