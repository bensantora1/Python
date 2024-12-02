# PyTorch Linear Regression Tutorial

## The Goal
We want PyTorch to learn the mathematical relationship:

\[
y = 2x
\]

from the data we provide.

---

## Key Concepts in the Code

### 1. The Data (`x` and `y`)
We provide the model with **input data** (`x`) and **target output** (`y`).

In this case:
\[
x = [[1.0], [2.0], [3.0]] \quad \text{and} \quad y = [[2.0], [4.0], [6.0]]
\]

The relationship between `x` and `y` is:
\[
y = 2x
\]

---

### 2. The Model
The model is a simple **linear function**:
\[
y = mx + c
\]
- \( m \): The **weight** (slope of the line).
- \( c \): The **bias** (y-intercept of the line).

---

### 3. Training the Model
**Training** means teaching the model to adjust \( m \) (weight) and \( c \) (bias) so it can predict `y` accurately for any given `x`.

---

### 4. Loss Function (`loss_fn`)
The **loss function** measures how "wrong" the model’s predictions are compared to the true `y`.

In this case, the **Mean Squared Error (MSE)** is used:
\[
\text{Loss} = \frac{1}{n} \sum_{i=1}^n (\text{predicted } y_i - \text{actual } y_i)^2
\]

The **smaller** the loss, the better the model is doing.

---

### 5. Optimizer (`optimizer`)
The optimizer adjusts \( m \) and \( c \) to minimize the loss.  
We use **Stochastic Gradient Descent (SGD)** to update the values step-by-step.

---

## What Happened in Your Code?

### 1. **Starting Point**
When the program starts:
- \( m \) and \( c \) are initialized to **random values**.  
  For example:
\[
m = 1.591, \quad c = 0.928
\]

---

### 2. **Training Process**
For 100 **epochs** (repeats), the model:
1. Predicts `y` using its current guess for \( m \) and \( c \).
2. Calculates how far off its predictions are using the **loss function**.
3. Updates \( m \) and \( c \) to improve its predictions.

---

### 3. **Ending Point**
After training, the model **approximates**:
\[
m = 2, \quad c = 0
\]

If:
\[
m = 2 \quad \text{and} \quad c = 0,
\]
the model exactly represents:
\[
y = 2x
\]

Your result might look like this:
\[
m = 1.591, \quad c = 0.928
\]

This is **close**, but not exact, because:
1. The model only trained for **100 epochs** (not enough for perfect learning).
2. Learning rates (step size) and epochs can affect accuracy.

---

## How to Improve the Model

1. **Train Longer**:
   - Increase the number of epochs:
     ```python
     for epoch in range(1000):  # Train for 1000 epochs
     ```

2. **Tweak the Learning Rate**:
   - Use a smaller learning rate for finer adjustments:
     ```python
     optimizer = torch.optim.SGD(model.parameters(), lr=0.001)
     ```

3. **Monitor the Loss**:
   - Add a print statement to check the loss during training:
     ```python
     print(f"Epoch {epoch+1}, Loss: {loss.item()}")
     ```

---

## What Did the Model Learn?
After training:
- **Learned Weight (\( m \))**: Approaches 2.0.
- **Learned Bias (\( c \))**: Approaches 0.0.

The model is trying to approximate \( y = 2x \) as closely as possible based on the data.
