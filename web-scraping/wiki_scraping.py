import requests
from bs4 import BeautifulSoup
import time
import csv


HEADERS = {
    "User-Agent": "is310-course-scraper/1.0 (student project; abust23@illinois.edu)"
}
BASE_URL = "https://terraria.wiki.gg"
START_URL = "https://terraria.wiki.gg/wiki/Weapons"

def main():
    print("Starting up the scraper...")
    
    # First request to get the main page
    try:
        res = requests.get(START_URL, headers=HEADERS, timeout=10)
        if res.status_code != 200:
            print("Could not reach the page. Status:", res.status_code)
            return
    except Exception as e:
        print("Error connecting:", e)
        return

    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Finding the links for melee and magic weapons
    content = soup.find('div', class_='mw-parser-output')
    links_to_visit = []
    
    if content:
        for a_tag in content.find_all('a'):
            href = a_tag.get('href')
            if href and '/wiki/' in href and href not in links_to_visit:
                text = a_tag.text.lower()
                # Only grabbing Melee and Magic
                if 'melee weapons' in text or 'magic weapons' in text:
                    links_to_visit.append(href)

    links_to_visit = links_to_visit[:2]
    print("Going to scrape these pages:", links_to_visit)

    all_weapons_data = []

    # Now going into the second level of pages
    for link in links_to_visit:
        full_link = BASE_URL + link
        print("Scraping page:", full_link)
        
        try:
            page_res = requests.get(full_link, headers=HEADERS, timeout=10)
            if page_res.status_code == 200:
                page_soup = BeautifulSoup(page_res.text, 'html.parser')
                
                # Find the tables with the weapons
                tables = page_soup.find_all('table', class_='wikitable')
                
                for table in tables:
                    # skip the first row because it's the header (Name, Damage, Type)
                    rows = table.find_all('tr')[1:] 
                    
                    for row in rows:
                        cols = row.find_all('td')
                        # Need at least 3 columns for name, damage, type
                        if len(cols) >= 3:
                            name_text = cols[0].text.strip()
                            dmg_val = cols[1].text.strip()
                            dmg_type = cols[2].text.strip()
                            
                            # clean up 
                            name_text = " ".join(name_text.split())
                            dmg_val = " ".join(dmg_val.split())
                            dmg_type = " ".join(dmg_type.split())
                            
                            cat = link.replace('/wiki/', '').replace('_', ' ')
                            
                            all_weapons_data.append({
                                'Name': name_text,
                                'Damage': dmg_val,
                                'Type': dmg_type,
                                'Category': cat
                            })
            else:
                print("Failed to get page, status code:", page_res.status_code)
                
        except Exception as e:
            print("Something went wrong scraping the subpage:", e)

        print("Sleeping for 2 seconds...")
        time.sleep(2)

    # Save to CSV
    csv_file = 'terraria_weapons.csv'
    print(f"Saving {len(all_weapons_data)} rows to {csv_file}...")
    
    with open(csv_file, mode='w', newline='', encoding='utf-8') as f:
        # Using the keys from the dictionary above
        writer = csv.DictWriter(f, fieldnames=['Name', 'Damage', 'Type', 'Category'])
        writer.writeheader()
        for item in all_weapons_data:
            writer.writerow(item)

    print("Done!")

if __name__ == '__main__':
    main()