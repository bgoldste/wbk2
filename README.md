Django project using torchbox's excellent django-template vagrant box. 

This is an in-progress build of a surfing website that does a few things with data:

  1. Builds out 'spot' locations including html location of data to scrape, name, and lat/long geo-location
  2. Runs scrapers on NOAA (natl oceanic atmospheric association) to pull data into a ForecastData model that is linked to a spot
  3. Scrapes instagram photos based on the spot location for photos that match "surf" and links those photos to the nearest forecastdata by time.
  

TODOS-
change how spots are displayed
Add Celery (or some other task queue) to automate data scraping. Move scrapers from views to tasks.py.
