# cop-scraper
A scraper built using Scrapy+Python that can quickly get a list of most law enforcement agencies in the US using the PoliceOne.com directory.

## Usage

1) First create a virtual environment with either `virtualenv`, `virtualenvwrapper`, `Anaconda`, etc.
2) Once you've created your virtual environment, do `pip install -r requirements.txt` to ensure that all required libraries are installed.
3) To run the scraper, simply do: `scrapy crawl agencies` on terminal.
4) If you want to save the output to a JSON file, use `scrapy crawl agencies -o agencies.json` instead.
5) Once you've exported to JSON, you can also use the `translator.py` file to convert your JSON into a CSV for Excel/etc. based manipulation. Simply do: `python translator.py` and as long as you didn't use a different name for the `.json` file, you should be good! 
