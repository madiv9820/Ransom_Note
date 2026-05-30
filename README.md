# [🕵️‍♂️ The Case: The Ransom Note](https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150)

Welcome to the detective's desk! You have a secret message to send, and a stack of old magazines to cut letters out of.

### 🎯 The Goal:

You are given two strings: a **`ransomNote`** and a **`magazine`**. You need to figure out if you can successfully spell out your exact ransom note using *only* the letters provided in the magazine. If you can, return **`True`**. If you run out of letters, return **`False`**.

### ⚠️ The Golden Rule: 

Scissors and glue, my friend. Every time you use a letter from the magazine, you physically cut it out. This means **each letter in the magazine can only be used ONCE**. You cannot reuse a single 'a' to spell "aardvark"!

### 🧪 Let's Look at the Evidence (Examples)

* #### Example 1: The Impossible Target 🚫

    > **Target:** **`"a"`** <br>
    > **Magazine:** **`"b"`** <br>
    > **Verdict:** **`False`**. You need an 'a', but all you have is a 'b'. The heist is off!

* #### Example 2: The Letter Shortage 📉

    > **Target:** **`"aa"`** <br>
    > **Magazine:** **`"ab"`** <br>
    > **Verdict:** **`False`**. You found one 'a', but you need two! You ran out of supplies.

* #### Example 3: The Perfect Match 📦

    > **Target:** **`"aa"`** <br>
    > **Magazine:** **`"aab"`** <br>
    > **Verdict:** **`True`**. You need two 'a's, and the magazine gives you exactly two 'a's and a bonus 'b'. Success!

### 🚧 The Laws of Physics (Constraints)

> * **`1 <= ransomNote.length, magazine.length <= 10^5`**
>   * **🚫 What it rules out:** You absolutely cannot use nested for loops (like checking the whole magazine from the beginning for every single letter in the note). An $O(N \times M)$ approach would result in 10,000,000,000 operations and give you a **Time Limit Exceeded (TLE)** error.
>
>   * **✅ What it requires:** You must solve this in a single pass $O(N + M)$ time.
>
> * **`ransomNote` and `magazine` consist of lowercase English letters.**
>
>   * **🚫 What it rules out:** We don't have to worry about uppercase letters, numbers, spaces, or special punctuation.
>
>   * **✅ What it gives us:** Because there are exactly 26 lowercase English letters, we don't need to waste memory on a dynamic Hash Map that scales up. We can build a **fixed array of exactly 26 slots** (using $O(1)$ constant space) to tally our inventory!

### 🛣️ Approaches

| 🛠️ Approach | ⏱️ Time Complexity | 💾 Space Complexity | ✅ Pros | ❌ Cons | 🏆 Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. [The Brute Force](docs/brute_force.md)** <br> *(Sorting & Scanning)* | O(N log N + U * M) | O(N) | Intuitive approach; grouping identical letters makes logical sense to human readers. | Extremely slow; requires sorting the string and repeatedly scanning the entire magazine. | A fun thought experiment, but not for production code. |
| **2. [The Pythonic Dictionary](docs/hashmap.md)** <br> *(Hash Map)* | O(N + M) | O(U) | Highly readable; perfectly utilizes standard Python libraries (`collections.Counter`). | Dynamic memory allocation means the space scales up with the number of unique characters. | Writing clean, maintainable, standard Python code on the job. |
| **3. [The FAANG Optimal](docs/constant_space.md)** <br> *(Fixed Array)* | **O(N + M)** | **O(1)** | **Strict constant memory.** Bypasses the overhead of dynamic Hash Maps via ASCII index mapping. | Slightly less "Pythonic" syntax as it relies on `ord()` math. | Acing technical interviews by exploiting constraints! |

> **Key:** 
> * **N** = Length of the Ransom Note 
> * **M** = Length of the Magazine
> * **U** = Unique characters in the Magazine

### 📦 Repository Structure

This project follows a clean, modular architecture, separating the core algorithms from the execution interface and the automated testing suite.

```Plaintext
✂️ Ransom_Note
 ┣ 📂 docs
 ┃ ┗ 📜 approach-comparison.md       # 📊 Detailed Big-O breakdown and pros/cons
 ┣ 📂 source
 ┃ ┣ 📜 __init__.py                  # 📦 Makes source a Python package
 ┃ ┣ 📜 approaches.py                # 🧠 The core string manipulation & Hash Map logic
 ┃ ┗ 📜 solution.py                  # 🔌 The clean LeetCode runner interface
 ┣ 📂 test
 ┃ ┣ 📜 __init__.py                  # 📦 Makes test a Python package
 ┃ ┣ 📜 cases.json                   # 🗃️ Edge cases (Alphabet Soup, Shortages, etc.)
 ┃ ┗ 📜 test.py                      # 🚦 The automated dynamic test runner
 ┣ 📜 .gitignore                     # 🙈 Hides __pycache__ and system files
 ┗ 📜 README.md                      # 🌌 The master project landing page
```

#### 🚀 How to Run the Code

Since we built a highly professional, modular repository, there are two ways to interact with the code: running the automated test suite or writing your own custom runner script.

> **Prerequisite**: Ensure you have Python 3.x installed on your machine.

We built a dynamic test runner that will automatically ingest the cases.json file and test our optimal algorithms against the edge cases.

Open your terminal, navigate to the root of the repository (**`Ransom_Note/`**), and run:

```bash
python3 -m test.test -v
```

---