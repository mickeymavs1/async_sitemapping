## async_sitemapping
# WebScraper

WebScraper is a Python project designed to scrape and clean web pages from a given sitemap URL. Utilizing asynchronous programming, it efficiently fetches and processes multiple pages concurrently. This tool is particularly useful for extracting text content from websites by removing unnecessary HTML elements like headers, footers, navigation bars, scripts, and styles.

## Features

- **Sitemap Parsing**: Extracts URLs from a provided sitemap XML file.
- **Asynchronous Downloads**: Fetches HTML content of specified pages concurrently using asynchronous HTTP requests.
- **HTML Cleaning**: Cleans the fetched HTML content by removing unwanted elements, retaining only the main textual content.
- **Text Extraction**: Extracts and processes text content, removing extra whitespace and unnecessary HTML tags.
- **Data Printing**: Prints the cleaned text content of the pages to the terminal.

## Requirements

- **Python Version**: Python 3.6 or higher is required to run this project.
- **Dependencies**:
  - `aiohttp`: For making asynchronous HTTP requests.
  - `beautifulsoup4`: For parsing and cleaning HTML content.
  - `lxml`: As the parser for BeautifulSoup.

## Installation

1. **Clone the Repository**:
   - Clone the project repository to your local machine using Git.

2. **Virtual Environment**:
   - It is recommended to create and activate a virtual environment to manage dependencies.
   
3. **Install Dependencies**:
   - Install the required Python packages using `pip`.

## Usage

1. **Configure Parameters**:
   - Open the main script file and modify the `sitemap_url` variable to point to your desired sitemap XML URL.
   - Set the `num_pages` variable to specify the number of pages you want to scrape from the sitemap.

2. **Run the Script**:
   - Execute the script to start the scraping process. The script will fetch, clean, and print the text content of the specified pages.

## Example

To use the WebScraper, initialize it with the sitemap URL and the number of pages you want to scrape. Then, call the scraping function to perform the entire process. The cleaned data will be printed to the terminal, showing the text content of each scraped page.

## Project Structure

- **Main Script**: Contains the `WebScraper` class and the orchestration function.
  - **Initialization**: Sets up the WebScraper with the sitemap URL and the number of pages.
  - **Fetching Sitemap**: Downloads the sitemap XML content asynchronously.
  - **Parsing Sitemap**: Extracts the URLs from the sitemap XML.
  - **Fetching Pages**: Downloads the HTML content of the extracted URLs concurrently.
  - **Cleaning Text**: Processes the HTML content to remove unwanted elements and extract the main text.
  - **Printing Data**: Outputs the cleaned text content of each page to the terminal.

## License

WebScraper is licensed under the MIT License. This license allows for permissive reuse of the code, provided proper attribution is given.

## Contributing

Contributions to WebScraper are welcome! If you have any suggestions for improvements or find any bugs, please open an issue or submit a pull request. Contributions can range from bug fixes and feature additions to documentation improvements.

## Acknowledgements

WebScraper leverages several open-source libraries:
- **aiohttp**: For handling asynchronous HTTP requests.
- **BeautifulSoup**: For parsing and cleaning HTML content.
- **lxml**: Used as the parser for BeautifulSoup to efficiently process XML and HTML content.

Feel free to customize this overview based on the specifics of your project and additional features you might want to highlight.
