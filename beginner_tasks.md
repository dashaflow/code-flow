# Beginner Python Tasks

A collection of beginner-level Python tasks with solutions.  

---

## 1. Square Every Digit

**Task:**  
Given an integer, square every digit of the number and concatenate them to produce a new integer.  

**Examples:**  
9119 → 81 1 1 81 → 811181
765 → 49 36 25 → 493625

**Solution:**
def square_digits(n):
    return int("".join(str(int(d) ** 2) for d in str(n)))

print(square_digits(9119))

---

## 2. Descending Order

**Task:**
Your task is to make a function that can take any non-negative integer and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

**Examples:** 
42145 → 54421
145263 → 654321
123456789 → 987654321

**Solution:**
def descending_order(n):
  return int("".join(sorted(str(n), reverse=True)))
  
print(descending_order(19939))

---
