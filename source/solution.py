"""
================================================================================
📄 File: solution.py
================================================================================
Description: 
    The main entry point and runner for "Ransom Note" (LeetCode 383).
    This file acts as the clean interface expected by LeetCode, delegating 
    all the heavy detective work to our modular Approaches! 🕵️‍♂️
================================================================================
"""

from .approaches import (
    Brute_Force_Approach, 
    Hashmap_Approach, 
    Constant_Space_Approach
)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Determines if the ransom note can be cut out from the magazine.
        """
        
        # 📦 Instantiate our arsenal of string-matching algorithms
        bf: Brute_Force_Approach = Brute_Force_Approach(ransomNote=ransomNote, magazine=magazine)
        hm: Hashmap_Approach = Hashmap_Approach(ransomNote=ransomNote, magazine=magazine)
        cs: Constant_Space_Approach = Constant_Space_Approach(ransomNote=ransomNote, magazine=magazine)
        
        # 🚀 EXECUTION BLOCK
        # Choose your weapon! We default to the FAANG-optimal constant space approach.
        # (You can easily swap 'cs' with 'bf' or 'hm' to test the other algorithms!)
        return cs.apply()
