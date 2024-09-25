# check_redirects

## Goal
Make sure that the links in blogs, footer, etc. point to valid links in the docs.

## Virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Add scrapy

```bash
pip install scrapy
```

## Run a crawl

```bash
scrapy runspider linkchecker.py -o ~/tmp/broken-links.csv
```
