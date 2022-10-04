import asyncio
import aiohttp
import time
import requests
import re
import aiofiles

class Scraper:

	def __init__(self, username: str):
		self.username = username
		self.video_queue = None	
		self.idx = 0
		self.done = False
	
	async def start(self):
		page_url = f'https://www.aparat.com/api/fa/v1/user/video/list/username/{self.username}/page1/'
		self.session = aiohttp.ClientSession()
		self.video_queue = asyncio.Queue()
		await asyncio.gather(self.download_videos(), self.crawl(page_url))

	async def download_videos(self):
		while not (self.video_queue.empty() and self.done):
			try:
				video_url = await self.video_queue.get()
				self.idx += 1
				async with self.session.get(video_url) as response:
					if response.status == 200:
						print(f'downloading video #{self.idx}')
						f = await aiofiles.open(f'./videos/video{self.idx}.mp4', mode='wb')
						await f.write(await response.read())
						await f.close()
					else:
						print(f'error in downloading video{self.idx}')
			except Exception as e:
				print(e)


	async def crawl(self, page_url: str):
		while True:
			try:
				async with self.session.get(page_url) as response:
					response_dict = await response.json()
					for video in response_dict['included'][:-1]:
						uid = video['attributes']['uid']
						m3u8_link = f'https://www.aparat.com/video/hls/manifest/visittype/embed/videohash/{uid}/f/{uid}.m3u8' 
						async with self.session.get(m3u8_link) as m3u8_response:
							matcher = re.findall(r'https:\/\/.+', await m3u8_response.text())
							video_link = matcher[1] if len(matcher) > 1 else matcher[0]
							video_link = video_link.replace('.apt', '.mp4')
							video_link = video_link.replace('/chunk.m3u8', '')
							await self.video_queue.put(video_link)
							print(f'new video added to queue. queue size: {self.video_queue.qsize()}')
				
				has_next_page = response_dict['data'][0]['attributes']['link']
				if has_next_page is None:
					elapsed = time.time() - s
					print(elapsed)
					print(f'time elapsed: {elapsed} seconds')
					self.done = True
					break
				
				page_url = response_dict['data'][0]['attributes']['link']['next']

			except Exception as e:
				print(e)


if __name__ == '__main__':

	username = 'BornaNews'

	scraper = Scraper(username)

	s = time.time()
	asyncio.run(scraper.start())

	
