🚀 Automated Resume Screener and Detail Extractor

This project leverages advanced Natural Language Processing (NLP) and vector embeddings to automate the initial screening of candidate resumes against a specific Job Description (JD). It calculates a similarity score to rank applicants and uses spaCy for rapid extraction of key candidate details (contact, skills, education) directly from the raw text.

✨ Features

Intelligent Similarity Scoring: Uses Sentence Transformers to convert the JD and resume into dense vector embeddings, calculating Cosine Similarity for accurate relevance matching.

Threshold-Based Screening: Automatically categorizes candidates into Eligible, Needs Manual Review, or Not Eligible based on a predefined similarity threshold.

Automated Detail Extraction: Utilizes regex and spaCy's NER (Named Entity Recognition) to quickly pull contact information (Email, Phone) and structured data (Skills, Education).

PDF Text Loading: Includes functionality to read and extract text from PDF files, making it ready for processing.

Data Cleaning: Implements robust text preprocessing, including lowering case, punctuation removal, and stop word filtering (using NLTK), to ensure high-quality embeddings.

🛠 Technology Stack

Category

Tool / Library

Purpose

Language

Python

Core project language

NLP & ML

sentence-transformers

Generating high-quality vector embeddings (using the all-MiniLM-L6-v2 model)

NLP & Extraction

spaCy

Named Entity Recognition for structured data extraction

Text Processing

NLTK

Tokenization and Stop Word removal

PDF Handling

pdfminer.six

Extracting raw text from PDF documents

Core Utilities

pandas, numpy

Data manipulation and numeric operations

⚙️ Installation and Setup

Clone the repository:

git clone https://your-repo-link/automated-resume-screener.git
cd automated-resume-screener


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install the required dependencies:

pip install -r requirements.txt


Download the necessary spaCy model and NLTK data:

python -m spacy download en_core_web_sm
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"


📊 Screening Logic and Key Numeric Details

The project utilizes specific thresholds to determine candidate suitability.

Similarity Score Thresholds:

Score Range

Status

Action

Score ≥ 0.60

Eligible

Proceed directly to interview pipeline.

0.45 ≤ Score < 0.60

Needs Manual Review

Requires a human recruiter to quickly review context.

Score < 0.45

Not Eligible

Filtered out.

Example Run (Data Analyst Resume vs. JD)

In a test run using the provided resume against a Data Analyst Job Description, the following result was generated, demonstrating a strong match:

Metric

Value

Status

Match Score

0.7783

Accepted

Phone No

7303025805

Extracted

Email ID

prabhavs2004@gmail.com

Extracted

Performance Metrics from Projects (Quantifying Impact)

The candidate's resume highlighted strong quantitative achievements, demonstrating a focus on measurable results:

Project Metric

Numeric Detail

Project Name

Faster Data Discovery

70%

Conversational Data Analytics Platform

Increase in Data-Driven Decisions

20%

Conversational Data Analytics Platform

Improved Forecast Accuracy

15%

E-commerce Exploratory Data Analysis

Reduced Anomaly Detection Time

25%

E-commerce Exploratory Data Analysis

Reduction in Misclassification Rates

10%

Predictive Diabetes Risk Stratification Model




(Note: Refer to Data Ingestion.ipynb for the full step-by-step processing logic.)
