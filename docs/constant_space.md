## 🚀 Approach 3: The FAANG Optimal (Fixed Array)

This is the holy grail for this specific problem. While the Hash Map approach is excellent, a true FAANG interviewer will point to the constraints and ask: *"Can you do this without dynamically allocating memory?"* By exploiting the "lowercase English letters only" rule, we can achieve strict constant space.

### 💡 The Intuition

In the previous approach, we used a Hash Map. Hash Maps are fantastic, but they grow in size based on how many unique characters we feed them.

Think about our detective desk. Instead of bringing a notebook with an infinite number of blank pages (a Hash Map), we can just build a wooden tray with **exactly 26 slots**—one for every letter in the alphabet.

**The Strategy:** We create a fixed array of **`26`** zeroes. Because computers understand letters as numbers (ASCII values), we can use simple math to map 'a' to slot **`0`**, 'b' to slot **`1`**, all the way to 'z' at slot **`25`**. We tally our magazine inventory in these slots. Because our tray never grows beyond 26 slots, our memory usage is perfectly flat, no matter how massive the magazine is!

### 🚶‍♂️ Step-by-Step Logic

1. **The Quick Check:** If the ransom note is longer than the magazine, it is physically impossible to construct. Return **`False`**.

2. **Build the Tray:** Initialize an array of exactly 26 integers, all set to **`0`**.

3. **Inventory the Magazine:** Loop through every character in the **`magazine`**.

    * **The ASCII Trick:** Subtract the ASCII value of 'a' from the current character to get its index. (e.g., **`ord('c') - ord('a') = 99 - 97 = 2`**).

    * Increment the value at that specific index in our array by **`1`**.

4. **Write the Note:** Loop through every character in the **`ransomNote`**.

5. **Check the Slots:** For each character, calculate its index using the same ASCII math.

    * **The Trap:** Check the array at that index. If the value is **`0`**, our slot is empty. We don't have the letter. Return **`False`**!

    * **The Cut:** If the value is greater than **`0`**, deduct **`1`** from that index.

6. **The Verdict:** If you finish the loop without running into an empty slot, return **`True`**.

### 💻 Pseudocode

```plaintext
FUNCTION can_construct(ransomNote, magazine):
    
    // 1. Impossible state check
    IF length(magazine) < length(ransomNote):
        RETURN False
        
    // 2. Build our 26-slot tray
    inventory_tray = Array of 26 zeroes
    
    // 3. Tally up the magazine using ASCII math
    FOR every char in magazine:
        index = ASCII_VALUE(char) - ASCII_VALUE('a')
        inventory_tray[index] = inventory_tray[index] + 1
            
    // 4. Attempt to write the ransom note
    FOR every target_char in ransomNote:
        index = ASCII_VALUE(target_char) - ASCII_VALUE('a')
        
        // If the slot is empty, we are out of letters!
        IF inventory_tray[index] == 0:
            RETURN False
            
        // Otherwise, "cut" the letter out
        inventory_tray[index] = inventory_tray[index] - 1
        
    RETURN True
```

### 📊 Complexity Analysis
* **⏱️ Time Complexity:** $O(N + M)$
    
    * **Taking Inventory:** We iterate through the magazine exactly once, taking $O(M)$ time.
    
    * **Writing the Note:** We iterate through the ransom note exactly once, taking $O(N)$ time.
    
    * Array index lookups (using our ASCII math) operate in instant $O(1)$ time. The total time complexity remains strictly linear.

* **💾 Space Complexity:** $O(1)$

    * This is where the magic happens! We allocate an array of exactly 26 integers.
    
    * Whether our strings are 10 characters long or 100,000 characters long, we never allocate more than 26 slots. Because the memory usage does not scale with the input size, it is mathematically classified as $O(1)$ Constant Space. 🏆

---
