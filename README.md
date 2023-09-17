# Web Scraping with Scrapy, Flask, and MongoDB

**Overview:**
This project demonstrates a web scraping workflow using Scrapy to extract quotes from a website and store them in a MongoDB database. A Flask backend is used to receive and save the scraped data to the database.

**Prerequisites:**
- Python 3.x
- Scrapy
- Flask
- pymongo
- MongoDB

**Getting Started:**
1. **Clone the repository to your local machine:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up a MongoDB database and collection for storing the scraped data. Modify the MongoDB configuration in `app.py` with your MongoDB server details.**

3. **Start the Flask backend by running:**
    ```bash
    python app.py
    ```

4. **Run the Scrapy spider to start scraping quotes and sending them to the Flask backend:**
    ```bash
    scrapy crawl quotes
    ```

5. **The scraped quotes will be saved to your MongoDB database.**

**Project Structure:**
- `quotes_scraper/` - Contains the Scrapy spider for scraping quotes.
- `app.py` - Flask application for receiving and saving scraped quotes to MongoDB.

**Usage:**
- Customize the Scrapy spider in `quotes_scraper/quotes_scraper/spiders/quotes_spider.py` to scrape data from your desired website.
- Run the Scrapy spider to initiate the scraping process.
- The Flask backend (`app.py`) receives scraped data and saves it to MongoDB.
- Modify the MongoDB URI, database name, and collection name in `app.py` as needed.

**License:**
This project is licensed under the MIT License 

**Acknowledgments:**
- [Scrapy](https://scrapy.org/) - A powerful web scraping framework.
- [Flask](https://flask.palletsprojects.com/) - A micro web framework for Python.
- [MongoDB](https://www.mongodb.com/) - A popular NoSQL database.
