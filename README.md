
A Github Web Scraper Rest Api Using Flask

## Installation
```
pip install flask
pip install beautifulsoup4
```

## Run
open console, type 
```
python scraper.py
```
Open the default URL on browser 


## Path 

### Trending  
get trending open source project
```http
@GET  /github/trend
```
 
 results:
 ``` python
 "detail": [
        "Animation of the SHA-256 hash function in your terminal."
      ], 
      "folk": "36", 
      "language": [
        "Ruby"
      ], 
      "link": [
        "https://github.com//in3rsha/sha256-animation"
      ], 
      "star": [
        "1,469"
      ], 
      "title": [
        "in3rsha/sha256-animation"
      ]
    }, 
```
## What's Next 
Looking for someone to continue the work , obviously there are more github page to scrap, to be continue...
