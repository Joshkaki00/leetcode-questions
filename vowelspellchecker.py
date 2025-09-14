# LeetCode 966: Vowel Spellchecker

class Solution:
    # Approach 1: Hash Maps for Each Priority Level (Optimal)
    def spellchecker(self, wordlist, queries):
        """
        Use hash maps to handle different matching priorities:
        1. Exact match (case-sensitive)
        2. Capitalization match (case-insensitive)  
        3. Vowel error match (vowels normalized + case-insensitive)
        """
        # Priority 1: Exact matches (case-sensitive)
        exact_matches = set(wordlist)
        
        # Priority 2: Capitalization matches (case-insensitive)
        # Map lowercase -> first occurrence in wordlist
        cap_matches = {}
        
        # Priority 3: Vowel error matches  
        # Map devoweled+lowercase -> first occurrence in wordlist
        vowel_matches = {}
        
        # Build lookup tables
        vowels = set('aeiouAEIOU')
        
        for word in wordlist:
            word_lower = word.lower()
            
            # For capitalization matches, store first occurrence
            if word_lower not in cap_matches:
                cap_matches[word_lower] = word
            
            # For vowel matches, create devoweled version
            devoweled = self.devowel(word_lower)
            if devoweled not in vowel_matches:
                vowel_matches[devoweled] = word
        
        # Process queries according to priority
        results = []
        for query in queries:
            result = self.find_match(query, exact_matches, cap_matches, vowel_matches)
            results.append(result)
        
        return results
    
    def devowel(self, word):
        """Replace all vowels with '*' for vowel error matching"""
        vowels = set('aeiou')
        return ''.join('*' if char in vowels else char for char in word)
    
    def find_match(self, query, exact_matches, cap_matches, vowel_matches):
        """Find match according to priority rules"""
        # Priority 1: Exact match (case-sensitive)
        if query in exact_matches:
            return query
        
        # Priority 2: Capitalization match (case-insensitive)
        query_lower = query.lower()
        if query_lower in cap_matches:
            return cap_matches[query_lower]
        
        # Priority 3: Vowel error match
        query_devoweled = self.devowel(query_lower)
        if query_devoweled in vowel_matches:
            return vowel_matches[query_devoweled]
        
        # No match found
        return ""
    
    # Approach 2: Explicit step-by-step (for understanding)
    def spellchecker_verbose(self, wordlist, queries):
        """
        More explicit implementation showing the matching logic clearly
        """
        results = []
        
        for query in queries:
            match = self.find_best_match(query, wordlist)
            results.append(match)
        
        return results
    
    def find_best_match(self, query, wordlist):
        """Find best match with explicit priority checking"""
        # Priority 1: Exact match
        for word in wordlist:
            if query == word:
                return word
        
        # Priority 2: Case-insensitive match
        query_lower = query.lower()
        for word in wordlist:
            if query_lower == word.lower():
                return word
        
        # Priority 3: Vowel error match
        query_devoweled = self.devowel(query_lower)
        for word in wordlist:
            word_devoweled = self.devowel(word.lower())
            if query_devoweled == word_devoweled:
                return word
        
        return ""

# Test cases (for local testing)
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # Example 1
        (["KiTe","kite","hare","Hare"], 
         ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"],
         ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]),
        
        # Example 2
        (["yellow"], ["YellOw"], ["yellow"]),
        
        # Additional test cases
        (["hello", "Hello", "HELLO"], ["hello", "Hello", "HELLO", "hELLo"], 
         ["hello", "Hello", "HELLO", "hello"]),
        
        (["apple"], ["aple", "epple", "ipple"], ["", "", ""]),
        
        (["test"], ["tast", "test", "Test", "TAST"], ["", "test", "test", ""]),
    ]
    
    approaches = [
        ("Hash Maps (Optimal)", solution.spellchecker),
        ("Verbose Step-by-step", solution.spellchecker_verbose)
    ]
    
    for approach_name, method in approaches:
        print(f"Testing {approach_name}:")
        all_correct = True
        
        for wordlist, queries, expected in test_cases:
            result = method(wordlist, queries)
            status = "✓" if result == expected else "✗"
            
            if result != expected:
                all_correct = False
                print(f"  {status} wordlist={wordlist}")
                print(f"      queries={queries}")
                print(f"      result={result}")  
                print(f"      expected={expected}")
            else:
                print(f"  {status} wordlist={wordlist}, queries={queries}")
        
        print(f"  {'All tests passed!' if all_correct else 'Some tests failed!'}")
        print()
    
    # Detailed analysis of Example 1
    print("Detailed analysis of Example 1:")
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    
    print(f"Wordlist: {wordlist}")
    print("Building lookup tables:")
    
    # Show exact matches
    exact_matches = set(wordlist)
    print(f"Exact matches: {exact_matches}")
    
    # Show capitalization matches
    cap_matches = {}
    for word in wordlist:
        word_lower = word.lower()
        if word_lower not in cap_matches:
            cap_matches[word_lower] = word
    print(f"Capitalization matches: {cap_matches}")
    
    # Show vowel matches
    vowel_matches = {}
    for word in wordlist:
        word_lower = word.lower()
        devoweled = solution.devowel(word_lower)
        if devoweled not in vowel_matches:
            vowel_matches[devoweled] = word
    print(f"Vowel matches: {vowel_matches}")
    print()
    
    print("Query processing:")
    for i, query in enumerate(queries):
        print(f"Query '{query}':")
        
        # Check exact match
        if query in exact_matches:
            print(f"  ✓ Exact match found: '{query}'")
            continue
        
        # Check capitalization match  
        query_lower = query.lower()
        if query_lower in cap_matches:
            print(f"  ✓ Capitalization match: '{query_lower}' -> '{cap_matches[query_lower]}'")
            continue
        
        # Check vowel match
        query_devoweled = solution.devowel(query_lower)
        if query_devoweled in vowel_matches:
            print(f"  ✓ Vowel match: '{query}' -> '{query_devoweled}' -> '{vowel_matches[query_devoweled]}'")
            continue
        
        print(f"  ✗ No match found")
    
    print("\nDevoweling examples:")
    examples = ["kite", "hear", "keti", "yellow"]
    for word in examples:
        devoweled = solution.devowel(word)
        print(f"  '{word}' -> '{devoweled}'")
    
    print("\nKey insights:")
    print("1. Use hash maps for O(1) lookups instead of O(n) linear search")
    print("2. Build all lookup tables once, then process queries efficiently")  
    print("3. Store first occurrence in wordlist to handle priority correctly")
    print("4. Devoweling: replace vowels with same character ('*') for pattern matching")