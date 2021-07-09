import asyncio
import time


class AmazonHub:
    def __init__(self):
        self.orders = {}
        self._items = []

    @property
    def items(self):
        return self._items

    def add(self, orders):
        self.orders = {**self.orders, **orders}

    def run(self):
        asyncio.run(self.process())

    async def _search(self, order, t):
        await asyncio.sleep(t)
        print(f'{order} - Done')

    async def process(self):
            tasks = []
            for order, t in self.orders.items():
                print(f'New order: {order}')
                tasks.append(asyncio.create_task(self._search(order, t)))
            await asyncio.gather(*tasks)


if __name__ == '__main__':
    items = {'Crime and Punishment by Fyodor Dostoevsky': 3, 'Harry Potter (all books)': 1, 'Star Wars IV': 2}
    amazon_hub = AmazonHub()
    amazon_hub.add(items)
    curr_time = time.perf_counter()
    amazon_hub.run()
    print(f'[{__file__}] executed in {(time.perf_counter() - curr_time):0.2f} seconds')

