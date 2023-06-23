from transformers import pipeline

def classify_text(text):
    classifier = pipeline("sentiment-analysis")
    return classifier(text)


# zeroShotClassifier = pipeline("zero-shot-classification")
# print(
# zeroShotClassifier(
#     "This is a course about the Transformers library",
#     candidate_labels=["education", "politics", "business"],
# ))