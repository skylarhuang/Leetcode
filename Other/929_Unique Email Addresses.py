## UNIQUE->USE SET

class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        localname = []
        domainname = []
        for email in emails:
            at_index = email.index('@')
            add_index = email.index('+')
            if at_index:
                localname = email[:at_index]
            if add_index:
                localname = email[:add_index]
            localname = localname.replace('.', '')
            domainname = email[at_index:]
            result.add(localname+'@'+domainname)
        return len(result)