
# 📘 Backtracking - Complete README Guide

Backtracking is a **recursive technique** used to solve problems by **building a solution step by step**, and **removing ("backtracking") the last step** when a dead end is reached or to explore another path.

---

## 📌 What is Backtracking?

> Backtracking is a method of **trying all possible options** in a decision tree and **undoing previous choices** to explore new ones.

You explore each branch (choice) and go back when:
- A solution is found (save it)
- The current path is invalid or complete (backtrack)

---

## 🧠 General Template for Backtracking

```python
def backtrack(curr_state):
    if goal_reached(curr_state):
        save_solution(curr_state)
        return

    for option in choices:
        if is_valid(option, curr_state):
            make_choice(option)
            backtrack(new_state)
            undo_choice(option)
```

---

## 🔁 Key Concepts

| Term           | Description                                                      |
|----------------|------------------------------------------------------------------|
| **Choose**     | Pick an option (append to path)                                  |
| **Explore**    | Move forward with the current path (recursive call)              |
| **Un-choose**  | Backtrack: remove last option to try a different one             |
| **Base Case**  | When you've built a complete solution                            |

---

## 🧮 Example 1: Subsets

```python
class Solution:
    def subsets(self, nums):
        res, sol = [], []
        n = len(nums)

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return

            # Not pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()  # Undo

        backtrack(0)
        return res
```

### 🔍 Example Input:
```python
nums = [1, 2]
```

### ✅ Output:
```python
[[], [2], [1], [1, 2]]
```

---

## 🔢 Example 2: Permutations

```python
class Solution:
    def permute(self, nums):
        res, sol = [], []
        n = len(nums)

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()  # Undo

        backtrack()
        return res
```

### 🔍 Input:
```python
nums = [1, 2, 3]
```

### ✅ Output:
```python
[
 [1,2,3], [1,3,2],
 [2,1,3], [2,3,1],
 [3,1,2], [3,2,1]
]
```

---

## 🧰 Common Backtracking Problems

| Problem                              | Type         | Description                           |
|--------------------------------------|--------------|---------------------------------------|
| Subsets                              | Combination  | Pick/not pick elements                |
| Permutations                         | Permutation  | All orderings without repetition      |
| N-Queens                             | Constraint   | Place queens without attacking        |
| Sudoku Solver                        | Constraint   | Fill board according to rules         |
| Word Search (Leetcode 79)           | Grid Search  | Path finding in 2D board              |
| Combination Sum / Target Sum         | Combination  | Add elements to reach a target        |
| Palindrome Partitioning              | Partition    | Divide string into palindromic parts  |

---

## 🧠 Tips to Master Backtracking

1. **Visualize the recursion tree** 📈
2. Always identify:
   - What’s the choice?
   - What’s the base case?
   - What to undo?
3. Dry run your code with small inputs
4. Practice classic problems on LeetCode or GeeksForGeeks

---

## 🎓 Good Practice Problems

- [Subsets - Leetcode 78](https://leetcode.com/problems/subsets/)
- [Permutations - Leetcode 46](https://leetcode.com/problems/permutations/)
- [Combination Sum - Leetcode 39](https://leetcode.com/problems/combination-sum/)
- [Palindrome Partitioning - Leetcode 131](https://leetcode.com/problems/palindrome-partitioning/)
- [N-Queens - Leetcode 51](https://leetcode.com/problems/n-queens/)
