import pandas as pd
data = {
    "results": [
        {
            "article_id": "123",
            "title": "News",
            "source": {"id": "bbc", "name": "BBC"},
            "keywords": ["politics", "election"]
        }
    ]
}
df = pd.json_normalize(data['results'])
df = df.explode("keywords")
print(df)