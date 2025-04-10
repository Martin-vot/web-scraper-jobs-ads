# Job Listings Scraper

A simple Python script that scrapes job postings from a website and saves them to a CSV file.

## Features
- Fetches HTML content from a given URL
- Extracts job titles, company names, and links
- Saves the results into a `jobs.csv` file

## Usage

1. Install the dependencies:

```bash
pip install requests beautifulsoup4
```

2. Update the `url` and CSS selectors in `job_scraper.py` to match your target site.

3. Run the script:

```bash
python job_scraper.py
```

## Output

The results will be saved to a file named `jobs.csv` in the same directory.

## License

MIT

## Author

Martin-vot
