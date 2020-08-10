import asyncio
import aiohttp
import json
from datetime import datetime


async def get_json(client, url):
    async with client.get(url) as response:
        assert response.status == 200
        return await response.read()


async def get_reddit_top(subreddit, client, num_posts):
    data = await get_json(client, 'https://www.reddit.com/r/' + subreddit +
                          '/top.json?sort=top&t=day&limit=' + str(num_posts))
    print(f"\n/r/{subreddit}:")
    items = json.loads(data.decode('utf-8'))
    for item in items["data"]["children"]:
        score = item["data"]["score"]
        title = item["data"]["title"]
        link = item["data"]["url"]
        print("score:", score, ":\t" + title, "\nlink:", link)
        print("score:", score, ":\t" + title, "\nlink:", link)


async def main():
    print(datetime.now().strftime("%A, %B %d, %I:%M %p"))
    print("===================")
    loop = asyncio.get_running_loop()
    async with aiohttp.ClientSession(loop=loop) as client:
        await asyncio.gather(
            get_reddit_top("python", client, 1),
            get_reddit_top("programming", client, 2),
            get_reddit_top("asyncio", client, 3),
            get_reddit_top("dailyprogrammer", client, 1)
        )


asyncio.run(main())
