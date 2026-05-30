"""
================================================================================
📄 File: approaches.py
================================================================================
Description: 
    Solutions for "Ransom Note" (LeetCode 383).
    The goal is to determine if we can build a specific ransom note using 
    ONLY the letters available in a given magazine. (Scissors and glue style!)

Approaches Included:
    1. Brute_Force_Approach    -> The Sorting & Scanning Method 🐢
    2. Hashmap_Approach        -> The Pythonic Dictionary Trick 📚
    3. Constant_Space_Approach -> The FAANG 26-Letter Array Optimal 🚀
================================================================================
"""

from typing import List
from collections import Counter

class Brute_Force_Approach:
    """
    🐢 APPROACH 1: The Sorting & Scanning Method
    This approach groups identical letters together by sorting the ransom note, 
    then scans the entire magazine for each unique letter to see if we have enough.
    It's reliable, but requires a lot of re-reading the magazine!
    """
    def __init__(self, ransomNote: str, magazine: str) -> None:
        self.__ransom_note: str = ransomNote
        self.__magazine: str = magazine

    def apply(self) -> bool:
        # 🚫 Early Exit: If the note is longer than the magazine, it's impossible!
        if len(self.__magazine) < len(self.__ransom_note):
            return False

        # 🗂️ Sort the note to group identical characters (e.g., "aba" -> "aab")
        self.__ransom_note = ''.join(sorted(self.__ransom_note))
        current_ptr: int = 0

        # 🔍 Scan through our sorted ransom note
        while current_ptr < len(self.__ransom_note):
            current_character_count: int = 0
            temp_ptr: int = current_ptr

            # 🧮 Count how many of this specific character we need
            while (
                temp_ptr < len(self.__ransom_note) and 
                self.__ransom_note[temp_ptr] == self.__ransom_note[current_ptr]
            ):
                current_character_count += 1
                temp_ptr += 1

            # 📰 Read through the ENTIRE magazine to find matches for this character
            for character in self.__magazine:
                if character == self.__ransom_note[current_ptr]:
                    current_character_count -= 1

            # ❌ If we still need more of this character after reading the whole magazine, we fail.
            if current_character_count > 0:
                return False

            # ⏭️ Move our pointer to the next unique character group
            current_ptr = temp_ptr
        
        return True
    
class Hashmap_Approach:
    """
    📚 APPROACH 2: The Pythonic Dictionary 
    We use a Hash Map (via Python's `Counter`) to take a complete inventory 
    of the magazine first. Then, we simply deduct letters as we write the note.
    """
    def __init__(self, ransomNote: str, magazine: str) -> None:
        self.__ransom_note: str = ransomNote
        self.__magazine: str = magazine

    def apply(self) -> bool:
        # 🚫 Early Exit: Same as before, physically impossible if the note is longer.
        if len(self.__magazine) < len(self.__ransom_note): 
            return False

        # 📝 Inventory Time! Count every letter in the magazine (e.g., {'a': 2, 'b': 1})
        magazine_characters_count: Counter = Counter(self.__magazine)
        
        # ✂️ Write the Note: Deduct letters one by one
        for character in self.__ransom_note:
            # If we run out (or never had it to begin with), we get caught!
            if magazine_characters_count.get(character, 0) == 0: 
                return False
            
            # Successfully used a letter, decrement our stash
            magazine_characters_count[character] -= 1
        
        return True
    
class Constant_Space_Approach:
    """
    🚀 APPROACH 3: The FAANG Optimal (Fixed Array)
    Since constraints specify "lowercase English letters only", we don't need 
    the overhead of a dynamic Hash Map! We can use a fixed-size array of 26 slots.
    Strict O(1) Constant Space!
    """
    def __init__(self, ransomNote: str, magazine: str) -> None:
        self.__ransom_note: str = ransomNote
        self.__magazine: str = magazine

    def apply(self) -> bool:
        # 🚫 Early Exit: Still the easiest way to save time!
        if len(self.__magazine) < len(self.__ransom_note): 
            return False

        # 🧠 Create exactly 26 buckets for 'a' through 'z'
        magazine_characters_count: List[int] = [0] * 26
        
        # 📝 Inventory the Magazine using ASCII math
        # ord('a') is 97. We subtract 97 to map 'a'->0, 'b'->1, ..., 'z'->25
        for character in self.__magazine:
            index: int = ord(character) - ord('a')
            magazine_characters_count[index] += 1

        # ✂️ Write the Note and deduct from our array buckets
        for character in self.__ransom_note:
            index: int = ord(character) - ord('a')
            
            # If the bucket is empty, the heist is off!
            if magazine_characters_count[index] <= 0: 
                return False
                
            # Take the letter out of the bucket
            magazine_characters_count[index] -= 1
        
        return True
