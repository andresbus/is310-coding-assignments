# Terraria Wiki Scraper

## What I Chose and Why
For my wiki, I went with the **Terraria Wiki** (https://terraria.wiki.gg). I have a friend who is abig fan of this game so I figured it would be fun to scrape data from it. 

My question was: **How do the base damage numbers and damage types compare between early melee weapons and magic weapons?**

I think this could be interesting to someone studying game design. Melee weapons usually force you to get close to enemies and take damage, while magic weapons let you attack from far away but use up mana. I wanted to see if the game developers gave melee weapons higher base damage to compensate for the fact that you have to get right in the enemy's face.

## robots.txt check
I checked the terms of service and the robots.txt file here: https://terraria.wiki.gg/robots.txt


## Reflection on my data
My scraper grabbed the weapon name, base damage, and damage type from the HTML tables. But I realized there's a big difference between what I actually measured and what the game is really like.

I measured a static number on a webpage. What I actually care about is how good a weapon is in combat. Someone would be wrong to look at my CSV and conclude that a weapon with higher base damage is automatically better than one with lower damage. For example, some magic weapons have lower damage but they shoot super fast, or they pierce through multiple enemies, or they set things on fire (like the Space Gun or Water Bolt). My data completely ignores stuff like attack speed, critical strike chance, and enemy defense. 

So my raw damage numbers are just a proxy for combat effectiveness, not the whole picture. You can't really judge game balance based just on the numbers in this CSV.