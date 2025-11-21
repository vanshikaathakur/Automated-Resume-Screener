import re
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sentence_transformers import SentenceTransformer, util

def clean_and_remove_stopwords(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s\.@]', ' ', text)
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words and (len(word) > 1 or word in ['@', '.'])
    ]
    clean_text = ' '.join(filtered_tokens)
    clean_text = re.sub(r'\s*@\s*', '@', clean_text)
    clean_text = re.sub(r'\s*\.\s*', '.', clean_text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    return clean_text

def compute_similarity(jd_text, resume_text, model):
    jd_clean = clean_and_remove_stopwords(jd_text)
    resume_clean = clean_and_remove_stopwords(resume_text)
    jd_emb = model.encode(jd_clean, convert_to_tensor=True)
    resume_emb = model.encode(resume_clean, convert_to_tensor=True)
    score = float(util.cos_sim(jd_emb, resume_emb))

    if score >= 0.60:
        status = "Eligible"
    elif 0.45 <= score < 0.60:
        status = "Needs Manual Review"
    else:
        status = "Not Eligible"

    return {
        "Similarity Score": round(score, 3),
        "Status": status
    }

def save_pickle():
    data = {
        "clean_function": clean_and_remove_stopwords,
        "similarity_function": compute_similarity
    }
    with open("resume_similarity.pkl", "wb") as f:
        pickle.dump(data, f)
    print("Pickle file created: resume_similarity.pkl")
