class Solution:
    from collections import defaultdict, deque
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        for account in accounts:
            name, *emails = account
            for email in emails[1:]:
                graph[emails[0]].add(email)
                graph[email].add(emails[0])
        
        grouped = []
        seen = set()
        for account in accounts:
            name, *emails = account
            queue = deque()
            for email in emails:
                if email not in seen:
                    res = []
                    queue.append(email)
                    while queue:
                        cur_email = queue.popleft()
                        if cur_email in seen:
                            continue
                        res.append(cur_email)
                        seen.add(cur_email)
                        for e in graph[cur_email]:
                            if e not in seen:
                                queue.append(e)
                    grouped.append([name] + sorted(res))
        return grouped