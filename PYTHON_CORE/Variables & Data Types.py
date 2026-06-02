# Defining data for a mini machine learning model tracker
model_name = "NeuralNet_v1"  # String
epochs = 50                  # Integer
learning_rate = 0.001        # Float (Decimal)
is_trained = False           # Boolean

# Printing the values
print(f"Model: {model_name}")
print(f"Learning Rate is set to: {learning_rate}")
print(f"Epochs: {epochs}")
print(f"Is Trained: {is_trained}")

datasets = "bodyweightdimensions"
total_number_of_rows = 5
training_data = 0.5

print(f"Dataset: {datasets}")
print(f"Total number of rows: {total_number_of_rows}")
print(f"Training Data: {training_data}")