import torch

# Create data
x = torch.tensor([[1.0], [2.0], [3.0]])
y = torch.tensor([[2.0], [4.0], [6.0]])

# Define the model
model = torch.nn.Linear(1, 1)  # A simple "line" model: y = mx + c

# Define the loss function and optimizer
loss_fn = torch.nn.MSELoss()  # Measures how wrong the predictions are
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)  # Helps the model learn

# Train the model
for epoch in range(100):  # Repeat 100 times
    optimizer.zero_grad()  # Reset gradients
    y_pred = model(x)  # Make a prediction
    loss = loss_fn(y_pred, y)  # Calculate the error
    loss.backward()  # Figure out how to adjust
    optimizer.step()  # Adjust the model

# Print the learned rule
print("Learned weight (m):", model.weight.item())
print("Learned bias (c):", model.bias.item())
