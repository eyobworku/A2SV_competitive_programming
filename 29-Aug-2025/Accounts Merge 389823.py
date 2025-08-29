# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent_map = {}
        
        def find(email):
            parent_map.setdefault(email, email)
            if parent_map[email] != email:
                parent_map[email] = find(parent_map[email])
            return parent_map[email]
        
        def union(email1, email2):
            parent_map[find(email1)] = find(email2)
        
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            primary_email = account[1]
            for email in account[1:]:
                union(primary_email, email)
                email_to_name[email] = name
        
        grouped_emails = defaultdict(list)
        for email in email_to_name:
            root_email = find(email)
            grouped_emails[root_email].append(email)

        merged_accounts = []
        for root_email, emails in grouped_emails.items():
            merged_accounts.append([email_to_name[root_email]] + sorted(emails))
        
        return merged_accounts