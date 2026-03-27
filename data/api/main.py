import requests
import pandas as pd

url = "https://newsdata.io/api/1/latest?apikey=pub_4ccfa82a7fa94e56b7a99d394c12bf76"

data = requests.get(url).json()
articles = data.get("results", [])

rows = []
for a in articles:
    rows.append({
        "article_id": a.get("article_id"),
        "title": a.get("title"),
        "link": a.get("link"),
        "source": a.get("source_id"),
        "creator": ", ".join(a.get("creator", [])) if isinstance(a.get("creator"), list) else a.get("creator"),
        "category": ", ".join(a.get("category", [])) if isinstance(a.get("category"), list) else a.get("category"),
        "country": ", ".join(a.get("country", [])) if isinstance(a.get("country"), list) else a.get("country"),
        "language": a.get("language"),
        "date": a.get("pubDate"),
        "description": a.get("description")
    })

df = pd.DataFrame(rows)

df = df.drop_duplicates(subset=["article_id"])
df = df.dropna(subset=["title", "date"])
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = df.dropna(subset=["date"])

df["title"] = df["title"].str.strip()
df["source"] = df["source"].fillna("unknown").str.lower().str.strip()
df["language"] = df["language"].fillna("unknown").str.lower().str.strip()
df["description"] = df["description"].fillna("").str.strip()

df["title_length"] = df["title"].str.len()
df["description_length"] = df["description"].str.len()
df["title_word_count"] = df["title"].str.split().str.len()

df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["hour"] = df["date"].dt.hour
df["day_name"] = df["date"].dt.day_name()

df["is_weekend"] = df["day_name"].isin(["Saturday", "Sunday"])
df["has_description"] = df["description_length"] > 0

df = df.sort_values(by=["date", "title_length"], ascending=[False, False])

df.to_csv("news_transformed.csv", index=False)

print(df.head())
print(df.info())