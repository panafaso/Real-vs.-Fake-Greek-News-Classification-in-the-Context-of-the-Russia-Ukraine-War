This project implements a machine learning pipeline for detecting fake vs. real news articles in the context of the Russia–Ukraine war, focusing on Greek-language data where benchmark resources are insufficient.

The approach combines:

-TF-IDF lexical features

-MiniLM sentence embeddings

-Logistic Regression classifier with balanced class weights

To improve transparency and trust, we integrated Explainable AI (XAI) methods:

1.SHAP to highlight token-level contributions

2.Case-Based Reasoning (CBR) to retrieve similar examples from the training set

By leveraging both lexical and semantic features, this project demonstrates a hybrid approach that is both effective for classification and interpretable through XAI techniques.
