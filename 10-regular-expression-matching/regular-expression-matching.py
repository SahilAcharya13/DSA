class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # If pattern is empty, string must also be empty
        if not p:
            return not s

        # Check whether the first character matches
        first_match = bool(s) and (p[0] == s[0] or p[0] == ".")

        # If next character is '*'
        if len(p) >= 2 and p[1] == "*":
            return (
                # Use '*' zero times
                self.isMatch(s, p[2:])
                or
                # Use '*' one or more times
                (first_match and self.isMatch(s[1:], p))
            )

        # Normal character or '.'
        return first_match and self.isMatch(s[1:], p[1:])