import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "kVEta4nZ981pnR1k1Vqw", "isbns": "9781632168146"})
print(res.json())