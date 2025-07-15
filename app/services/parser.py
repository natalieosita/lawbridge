import fitz  # PyMuPDF
import json
import re
import spacy

doc = fitz.open("app/data/Constitution of Kenya.pdf")

articles = []
current_article = None
collecting = False
buffer = []
article_number = None
article_title = None

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    doc = nlp(text)
    return list(set([token.lemma_.lower() for token in doc if token.pos_ in {"NOUN", "PROPN"} and not token.is_stop]))

current_article["keywords"] = extract_keywords(current_article["text"])
for page_num, page in enumerate(doc):
    if page_num < 12:  # Skip Table of Contents
        continue
    lines = page.get_text().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # Match a line that is just a number and a dot (e.g., '1.')
        if re.match(r'^\d+\.$', line):
            # Save previous article if exists
            if current_article:
                current_article["text"] = " ".join(buffer).strip()
                articles.append(current_article)
                buffer = []
            article_number = line[:-1]  # Remove the dot
            # Next line is the title
            i += 1
            article_title = lines[i].strip() if i < len(lines) else ""
            current_article = {
                "article_number": article_number,
                "title": article_title,
                "text": ""
            }
            collecting = True
        elif collecting:
            # Stop collecting if we hit a new chapter or the end of the document
            if re.match(r'^\d+\.$', line):
                # This will be handled in the next loop iteration
                collecting = False
                continue
            buffer.append(line)
        i += 1

# Save the last article
if current_article:
    current_article["text"] = " ".join(buffer).strip()
    articles.append(current_article)

with open("app/data/constitution.json", "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=2, ensure_ascii=False)

print(f"Extracted {len(articles)} articles.")