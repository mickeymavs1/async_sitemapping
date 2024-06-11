import aiohttp
import asyncio
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import re
import time


class WebScraper:
    """
    A class to scrape and clean web pages from a sitemap URL.
    """

    def __init__(self, url, n):
        """
        Initializes the WebScraper with the sitemap URL and the number of pages to scrape.
        """
        self.url = url
        self.n = n
        self.data = {}

    async def _fetch_sitemap(self, session):
        """
        Asynchronously fetches the sitemap XML content.
        """
        async with session.get(self.url) as response:
            return await response.text()

    async def _fetch_page(self, session, url):
        """
        Asynchronously fetches the HTML content of a given page URL.
        """
        async with session.get(url) as response:
            return await response.text()

    def _parse_sitemap(self, sitemap_xml):
        """
        Parses the sitemap XML to extract URLs of the first `n` pages.
        """
        root = ET.fromstring(sitemap_xml)
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [url_elem.text for url_elem in root.findall('ns:url/ns:loc', namespaces=namespace)]
        return urls[:self.n]

    async def _clean_text(self, html):
        """
        Cleans the HTML content to remove unnecessary elements and extract text.
        """
        soup = BeautifulSoup(html, 'html.parser')

        # Remove menu bar, header, and footer (common tags, adjust as needed)
        for element in soup.select('header, footer, nav'):
            element.decompose()

        # Remove hyperlinks but keep the text
        for a in soup.find_all('a', href=True):
            a.unwrap()

        # Remove scripts and styles
        for script in soup.find_all('script'):
            script.decompose()
        for style in soup.find_all('style'):
            style.decompose()

        # Extract title
        title = soup.title.string if soup.title else 'No Title'
        # Get text and remove extra whitespace
        text = soup.get_text(separator=' ', strip=True)
        text = re.sub(r'\s+', ' ', text).strip()
        return title, text

    async def scrap(self):
        """
        Asynchronously performs the scraping process.
        """
        async with aiohttp.ClientSession() as session:
            sitemap_xml = await self._fetch_sitemap(session)
            urls = self._parse_sitemap(sitemap_xml)

            tasks = [self._fetch_page(session, url) for url in urls]
            pages_content = await asyncio.gather(*tasks)

            tasks = [self._clean_text(content) for content in pages_content]
            cleaned_texts = await asyncio.gather(*tasks)

            for i, (title, text) in enumerate(cleaned_texts):
                self.data[i + 1] = {
                    'Page_content': text
                }

    def print_data(self):
        """
        Prints the cleaned data to the terminal.
        """
        for page_number, page_content in self.data.items():
            print("================================================================")
            print(f"Page Number: {page_number}")
            print(f"Page Content: {page_content['Page_content']}")
            print("\n\n")
        return self.data


async def main():
    """
    The main function to orchestrate the scraping process.
    """
    start_time = time.time()
    sitemap_url = 'https://www.samsung.com/us/consumer_sitemap.xml'
    num_pages = 7
    scraper = WebScraper(sitemap_url, num_pages)
    await scraper.scrap()
    scraper.print_data()
    end_time = time.time()

    print(f"Scraping completed in {end_time - start_time} seconds")


if __name__ == "__main__":
    asyncio.run(main())