## 1️⃣ Problem restated

We are asked:

> Can we select some numbers from an array **without repeating any number** so that their sum equals `targetSum`?

We want an efficient method instead of checking all $2^n$ subsets.

---

## 2️⃣ What `dp[i]` means

- Define `dp[i]` = **true if sum `i` can be formed using some subset of numbers** (without repeating any number).
- Initialize: `dp[0] = true` because sum 0 is always possible (pick no numbers).
- Other `dp[i]` start as `false`.

So `dp` is like a **map of reachable sums** as we consider numbers one by one.

---

## 3️⃣ Iterating over numbers

We process numbers **one by one**. For each number `num`:

1. Check sums `i` from `targetSum` down to `num`.
2. If `dp[i - num]` is true, then `dp[i] = true`.

**Why backward?**

- We iterate **backward** to avoid counting the same number twice in the same iteration.
- `dp[i - num]` represents sums **before considering the current number**.
- By updating `dp[i]` from large to small, we ensure the current number is only used **once**.

---

### Intuition in plain words

Think of it as a **“reachable sums” table**:

1. Start: only sum 0 is reachable.
2. Take the first number `num`. Now sum `num` becomes reachable.
3. Take the next number. For each previously reachable sum, we can now **add this number** and reach a new sum.
4. Repeat until all numbers are processed.

- Each `dp[i]` is **true** if there exists **any subset of numbers processed so far** that sums to `i`.
- By going backward in the inner loop, we make sure **we don’t reuse a number in the same subset**.

---

## 4️⃣ Step-by-step small example

**Array:** `[2, 3, 5]`, **targetSum:** `7`

- Initial dp: `[true, false, false, false, false, false, false, false]`

**Process 2:**

- `dp[2] = true` → sum 2 reachable

**Process 3:**

- `dp[5] = dp[2] + 3 → true` → sum 5 reachable
- `dp[3] = dp[0] + 3 → true` → sum 3 reachable

**Process 5:**

- `dp[7] = dp[2] + 5 → true` → sum 7 reachable

✅ Final dp: `dp[7] = true` → sum 7 is possible **without repeating any number**.

---

## 5️⃣ Why it works mathematically

- Each number is considered **exactly once**.
- For each number, we only add it to **previously reachable sums** (`dp[i - num]`).
- This ensures every sum is formed by **some combination of unique numbers**.

> Conceptually, we are building up all sums possible with subsets of numbers step by step.

---

## 6️⃣ Key intuition

1. **dp[i] = reachable sum**
2. **Process numbers one by one**
3. **Backward iteration prevents reuse**
4. **After all numbers**, `dp[targetSum]` tells you whether a subset sum exists.

- Forward iteration → numbers can repeat → unbounded sum problem.
- Backward iteration → numbers used once → 0/1 subset sum.

---

Perfect! Let’s make a **step-by-step visual diagram** of the **0/1 DP approach** for:

**Array:** `[2, 3, 5]`
**TargetSum:** `7`

We'll show the `dp` array after each number is processed.

---

### Step 0: Initialization

```
dp indices: 0 1 2 3 4 5 6 7
dp values:  t f f f f f f f
t = true, f = false
```

- Only sum 0 is reachable initially.

---

### Step 1: Process number 2

- Iterate `i` from 7 down to 2:

| i   | dp[i - 2] | Action  | dp[i] after |
| --- | --------- | ------- | ----------- |
| 7   | dp[5] = f | skip    | f           |
| 6   | dp[4] = f | skip    | f           |
| 5   | dp[3] = f | skip    | f           |
| 4   | dp[2] = f | skip    | f           |
| 3   | dp[1] = f | skip    | f           |
| 2   | dp[0] = t | dp[2]=t | t           |

```
dp: t f t f f f f f
```

- **Reachable sums:** 0, 2

---

### Step 2: Process number 3

- Iterate `i` from 7 down to 3:

| i   | dp[i - 3] | Action  | dp[i] after |
| --- | --------- | ------- | ----------- |
| 7   | dp[4] = f | skip    | f           |
| 6   | dp[3] = f | skip    | f           |
| 5   | dp[2] = t | dp[5]=t | t           |
| 4   | dp[1] = f | skip    | f           |
| 3   | dp[0] = t | dp[3]=t | t           |

```
dp: t f t t f t f f
```

- **Reachable sums:** 0, 2, 3, 5

---

### Step 3: Process number 5

- Iterate `i` from 7 down to 5:

| i   | dp[i - 5] | Action  | dp[i] after   |
| --- | --------- | ------- | ------------- |
| 7   | dp[2] = t | dp[7]=t | t             |
| 6   | dp[1] = f | skip    | f             |
| 5   | dp[0] = t | dp[5]=t | t (already t) |

```
dp: t f t t f t f t
```

- **Reachable sums:** 0, 2, 3, 5, 7

✅ `dp[7] = true` → sum 7 is possible **without repeating numbers**.

---

### Visual explanation (stepping stones analogy)

```
Start:    [0] reachable

After 2:  [0, 2] reachable
After 3:  [0, 2, 3, 5] reachable
After 5:  [0, 2, 3, 5, 7] reachable → target sum reachable
```

- Each number **adds new “reachable sums”** based on sums from previous numbers.
- **Backward iteration** ensures we don’t reuse the current number.
