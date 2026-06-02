weights = [0.2, 0.4, 0.6, 0.8, 1.0]

model_config = {
    "algorithm": "linear regression",
    "layers": 4,
    "accuracy_history": weights
}
print("Model Configuration:")
print(model_config)

def classify_weights(weight):
    if weights >= 0.6:
        return "heavy"
    else:
        return "light"

for weight in weights:
    classification = classify_weights(weight)
    print(f"Weight: {weight} is classified as {classification}")    