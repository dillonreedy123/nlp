from transformers import pipeline

classifier = pipeline("sentiment-analysis")
print(classifier("I've been waiting for a HuggingFace course my whole life."))

print(classifier(
    ["I've been waiting for a HuggingFace course my whole life.", "I hate this so much!"]
))

zeroShotClassifier = pipeline("zero-shot-classification")
print(
zeroShotClassifier(
    "This is a course about the Transformers library",
    candidate_labels=["education", "politics", "business"],
))