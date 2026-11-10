import requests
import json
import time


ol_url = "https://openlibrary.org/search.json"
ol_params = {"q": "The Hobbit", "limit": 1}

try:
    ol_res = requests.get(ol_url, params=ol_params, timeout=10)
    
    # Check status code before parsing
    if ol_res.status_code == 200:
        ol_data = ol_res.json()
        book = ol_data['docs'][0]
        book_title = book.get('title')
        
        # Getting the author. 
        if 'author_name' in book:
            author_name = book['author_name'][0]
        else:
            author_name = "Unknown"
            
        print(f"Found book: '{book_title}' by {author_name}")
        
        
        ol_save_data = {
            "title": book_title,
            "author": author_name,
            "first_publish_year": book.get('first_publish_year', 'N/A')
        }
        
        with open('openlibrary_data.json', 'w') as f:
            json.dump(ol_save_data, f, indent=4)
            print("Saved book data to openlibrary_data.json")
            
    else:
        print(f"Error with Open Library. Status: {ol_res.status_code}")
        author_name = None

except Exception as e:
    print("Something crashed with Open Library:", e)
    author_name = None


time.sleep(1)



if author_name:
    print(f"Connecting APIs: Searching the wiki for '{author_name}'...")
    
    wiki_url = "https://tolkiengateway.net/w/api.php"
    wiki_params = {
        "action": "query",
        "prop": "extracts",
        "exintro": True, 
        "titles": author_name, 
        "format": "json",
        "explaintext": True
    }
    
    try:
        wiki_res = requests.get(wiki_url, params=wiki_params, timeout=10)
        
        if wiki_res.status_code == 200:
            wiki_data = wiki_res.json()
            
          
            pages = wiki_data['query']['pages']
            
            
            page_id = list(pages.keys())[0]
            
          
            if 'missing' in pages[page_id]:
                print(f"Finding: The wiki doesn't have a direct page for '{author_name}'.")
                print("This is an ambiguous match because the wiki focuses on the lore, not the author.")
            else:
                page_title = pages[page_id]['title']
                extract = pages[page_id].get('extract', 'No text found.')
                
                print(f"Found Wiki Page: {page_title}")
                # Print just the first 200 characters so the terminal isn't flooded
                print(f"Preview: {extract[:200]}...")
                
                # Save wiki data
                wiki_save_data = {
                    "page_title": page_title,
                    "extract_preview": extract[:500]
                }
                with open('tolkien_wiki_data.json', 'w') as f:
                    json.dump(wiki_save_data, f, indent=4)
                    print("Saved wiki data to tolkien_wiki_data.json")
        else:
            print(f"Error with Wiki. Status: {wiki_res.status_code}")
            
    except Exception as e:
        print("Something crashed with the Wiki:", e)
else:
    print("Skipping wiki lookup because we didn't get an author from Open Library.")

print("\nScript finished!")