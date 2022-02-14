
Yahoo Finance Web Scraping with Python, Selenium, BeautifulSoup and Chromedriver
=================================================================================

Python API to get BTC-EUR data from Yahoo Finance website

How to install
-----------------

1. Make sure you got python3 and chromedriver on your machine

2. Install the requirements 
   ```console
    $ pip install selenium
    $ pip install beatifulsoup4
    ```

How does it work
----------------
The algorithm scraps through Yahoo's finances website and get the historical data of **BTC-EUR** over the last teen days and save it on a csv file automatically. 


Output CSV Example
--------

Historical data
````c
Date,Close
Feb 09 2022,39125.37
Feb 08 2022,38630.60
Feb 07 2022,38316.41
Feb 06 2022,37026.61
Feb 05 2022,36195.83
Feb 04 2022,36247.98
Feb 03 2022,32490.47
Feb 02 2022,32702.76
Feb 01 2022,34367.76
Jan 31 2022,34270.42
````




