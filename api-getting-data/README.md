# API Homework - Comparing Open Library and Tolkien Gateway

## The APIs I Chose
1. **Open Library API** (https://openlibrary.org/developers/api)
2. **MediaWiki Action API** (Tolkien Gateway - https://tolkiengateway.net/w/api.php)

## How I Connected Them
I started by using Open Library to search for the book *The Hobbit*. I pulled the author's name (J.R.R. Tolkien) from that data. Then, I took that author name and queried the Tolkien Gateway wiki to see if they had a page for him. 

## The Comparison 

**Requirements & Assumptions:**
Neither API required an API key or an account, which was nice. Open Library just needed a standard GET request. The Tolkien Gateway MediaWiki API also just needed a GET request, but I found I had to use a descriptive `User-Agent` header, otherwise it felt like I was sneaking around. This tells me Open Library is built for broad, open access (for readers), while MediaWiki sites are often protecting against bots scraping their servers, so they expect developers to identify themselves.

**Rate Limits & Scale:**
Open Library seems built for high volume (it's a library catalog), so I didn't hit any limits. The MediaWiki API also let me do a few requests, but I added a `time.sleep()` because wiki sites are usually run by volunteers and can crash if you ping them too fast. This implies Open Library is built for scale (corporate/nonprofit servers), while the wiki is built for human-paced browsing.

**Data Shape:**
This was the hardest part. Open Library gave me super clean, nested JSON (`['docs'][0]['author_name']`). It was very easy to get exactly what I wanted. The MediaWiki API, however, was a nightmare to parse. The data is buried under `['query']['pages']`, and the page ID is a random number that I had to extract using `list(pages.keys())[0]`. It's built for rendering web pages, not for data analysis. It quietly makes it really hard to get lists of things without writing extra loops.

**Who Runs It & Funding:**
Open Library is run by the Internet Archive, a massive nonprofit. If they shut down, it would be a huge loss for digital culture. The Tolkien Gateway is run by a community of fans/volunteers. If the wiki shuts down, the data might just vanish. It made me realize that relying on volunteer wikis for research is kind of risky long-term.

**What's Missing & The "Post-API Age":**
This connects to the readings. When I searched the wiki for the *author* (J.R.R. Tolkien), the wiki didn't have a page for him—it only has pages for his *fictional characters* and lore. The wiki is built for in-universe research, so the "author" is missing from the dataset. Conversely, Open Library is missing the actual text/lore of the book—it just catalogs the book as an object. 

As a researcher (the "fourth user"), I'm trying to use tools built for two completely different purposes. It's uncomfortable because neither API was designed for me to cross-reference them. I had to stitch them together manually, and the fact that the wiki didn't have the author's page shows the limits of how these cultural datasets are structured. 