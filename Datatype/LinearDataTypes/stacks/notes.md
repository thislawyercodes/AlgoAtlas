# Stack Cheat Sheet

## Introduction to Stacks
A **stack** is a linear data structure that follows the **LIFO** (Last In, First Out) principle. This means that the most recently added item is the first to be removed. Stacks are useful in scenarios where you need to manage data in a specific order (e.g., undo mechanisms, function call stacks).

In Python, stacks are often implemented using lists, which provide all necessary stack operations.

---

## Common Stack Operations

| Operation    | Python Code                          | Description                                        |
|--------------|--------------------------------------|----------------------------------------------------|
| **Push**     | `stack.append(item)`                 | Adds an item to the top of the stack.              |
| **Pop**      | `stack.pop()`                        | Removes and returns the top item. Raises error if empty. |
| **Peek**     | `stack[-1]`                          | Returns the top item without removing it.          |
| **Is Empty** | `len(stack) == 0`                    | Checks if the stack is empty.                      |
| **Size**     | `len(stack)`                         | Returns the number of items in the stack.          |

### Example Usage

```python
# Initialize an empty stack
stack = []

# Push items
stack.append(10)
stack.append(20)
stack.append(30)

# Peek at the top item
top_item = stack[-1]  # 30

# Pop items
stack.pop()  # Removes 30
stack.pop()  # Removes 20

# Check if stack is empty
is_empty = len(stack) == 0  # False

# Get stack size
size = len(stack)  

```


## LeetCode Questions on Stacks
Practice these problems on LeetCode to improve your understanding of stack-based problems:

Valid Parentheses - LeetCode #20
Min Stack - LeetCode #155
Evaluate Reverse Polish Notation - LeetCode #150
Daily Temperatures - LeetCode #739
Next Greater Element I - LeetCode #496
Trapping Rain Water - LeetCode #42
Largest Rectangle in Histogram - LeetCode #84
Basic Calculator II - LeetCode #227



## Using collections.deque to Create a Python Stack
TODO:

