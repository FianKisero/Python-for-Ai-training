weights = [0.2, 0.4, 0.6, 0.8, 1.0]

model_config = {
    "algorithm": "linear regression",
    "layers": 4,
    "accuracy_history": weights
}
print("Model Configuration:")
print(model_config)

for weight in weights:
    print(f"Weight: {weight}")
    if weight >= 0.6:
        print(f"Weight {weight} is heavy")
    else :
        print(f"Weight {weight} is light")

