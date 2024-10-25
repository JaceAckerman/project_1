from scrappingManager import ScrapingManager

# Author: Jace Ackerman
# Date: 10/24/24
# File: executable.py
# Description: This file is responsible for running the software. This file has a main() 
# that creates all the scrapingManager objects necessary to do obtain all the reviews for all five
# apple watche versions. The main method ensures that this script runs only when called directly.

def main():
    #instatiating objects
    series5 = ScrapingManager("appleWatchSeries5URLS.txt", "series5OutPut.txt")
    series6 = ScrapingManager("appleWatchSeries6URLS.txt", "series6Reviews.txt")
    series7 = ScrapingManager("appleWatchSeries7URLS.txt", "series7Reviews.txt")
    series8 = ScrapingManager("appleWatchSeries8URLS.txt", "series8Reviews.txt")
    series9 = ScrapingManager("appleWatchSeries9URLS.txt", "series9Reviews.txt")
    
    #getting reviews for each product
    series5.getReviewsForProduct()
    series6.getReviewsForProduct()
    series7.getReviewsForProduct()
    series8.getReviewsForProduct()
    series9.getReviewsForProduct()
    
if __name__ == "__main__":
    main()
    
    