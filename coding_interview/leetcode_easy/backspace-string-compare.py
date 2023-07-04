class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_idx = len(s)-1
        t_idx = len(t)-1
        s_backspaced = ""
        t_backspaced = ""
        s_skip = 0
        t_skip = 0


        while s_idx > -1:
            if s[s_idx] == "#":
                s_skip += 1
            else:
                if not s_skip:
                    s_backspaced = s_backspaced + s[s_idx]
                else:
                    s_skip -= 1
            s_idx -= 1

        while t_idx > -1:
            if t[t_idx] == "#":
                t_skip += 1
            else:
                if not t_skip:
                    t_backspaced = t_backspaced + t[t_idx]
                else:
                    t_skip -= 1
            t_idx -= 1

        return s_backspaced == t_backspaced