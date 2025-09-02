# ☕ Coffee Machine Simulator

This project simulates a coffee machine using an event-driven design.  
The machine is represented as a class that exposes a **single interface method** to handle all user interactions.  
Instead of directly reading from system input, the machine processes commands through this method, just like a real-world device that reacts to button presses or touchscreen input.

Learn more at [Hyperskill site](https://hyperskill.org/projects/69)

Here's the link to the project: [Hyperskill site](https://hyperskill.org/projects/69)

Check out my profile: https://hyperskill.org/profile/266976280

---

## 🚀 Features

- Interactive coffee machine simulation
- Supports the following actions:
  - `buy` – purchase coffee (espresso, latte, cappuccino)
  - `fill` – refill water, milk, beans, and cups
  - `take` – withdraw money from the machine
  - `remaining` – display current resources
  - `exit` – stop the machine
- Resource management with automatic checks
  - If resources are insufficient, the machine refuses to make coffee
  - Otherwise, it deducts resources and adds money
- State-driven design:
  - The machine keeps track of its current state (waiting for action, buying coffee, filling, etc.)
  - User input is interpreted based on the current state

---

## 🛠️ Initial Resources

The machine starts with:

- `400 ml` of water  
- `540 ml` of milk  
- `120 g` of coffee beans  
- `9` disposable cups  
- `$550` in cash  

---

## ☕ Coffee Recipes

| Coffee       | Water | Milk | Beans | Cups | Price |
|--------------|-------|------|-------|------|-------|
| Espresso     | 250ml | 0ml  | 16g   | 1    | $4    |
| Latte        | 350ml | 75ml | 20g   | 1    | $7    |
| Cappuccino   | 200ml | 100ml| 12g   | 1    | $6    |

---
