from docx import Document
from bs4 import BeautifulSoup
import pandas as pd

# -------------------------------
# Read the docx file
# -------------------------------
doc = Document("section class 2.docx")

html = "\n".join([p.text for p in doc.paragraphs])

# -------------------------------
# Parse HTML
# -------------------------------
soup = BeautifulSoup(html, "html.parser")

comments = []

# -------------------------------
# Extract ONLY top-level comments
# -------------------------------
for comment in soup.find_all("shreddit-comment"):

    # Keep only first comments (ignore replies)
    if comment.get("depth") != "0":
        continue

    author = comment.get("author", "Unknown")
    score = comment.get("score", "0")
    created = comment.get("created", "")

    # Comment text
    text_div = comment.find(
        "div",
        id=lambda x: x and x.endswith("-post-rtjson-content")
    )

    if text_div:
        text = text_div.get_text(" ", strip=True)
    else:
        text = ""

    comments.append({
        "author": author,
        "score": score,
        "created": created,
        "comment": text
    })

# -------------------------------
# Save CSV
# -------------------------------
df = pd.DataFrame(comments)

df.to_csv("season5_top_comments.csv",
          index=False,
          encoding="utf-8-sig")

print(f"Top-level comments extracted: {len(df)}")
print(df.head())