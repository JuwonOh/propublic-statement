from .client import Client
from .utils import CURRENT_CONGRESS, parse_date, get_soup
import re

class StatementsClient(Client):

    def latest_get(self):
        "return the latest statements"
        path = "statements/latest.json"
        return self.fetch(path)

    def by_member(self, member_id, congress_session, offset_num=1):
        """
        Takes a bioguide ID and chamber
        Returns recent statement
        """
        offset=offset_num*20
        path = "members/{member_id}/statements/{congress_session}.json?offset={offset}".format(
            member_id=member_id, congress_session=congress_session, offset=offset)
        return self.fetch(path)

    def by_terms(self, serch_terms, offset_num=1):
        """
        Takes a serch_terms,
        Returns related statements
        """
        offset=offset_num*20
        path = "statements/search.json?query={serch_terms}&offset={offset}".format(
            serch_terms=serch_terms, offset=offset)
        return self.fetch(path)

    def by_date(self, date, offset_num=1):
        "Return statements in a chamber on a single day"
        date = parse_date(date)
        offset=offset_num*20

        path = "statements/date/{date:%Y-%m-%d}.json?offset={offset}".format(
            date=date, offset=offset)
        return self.fetch(path)

    def by_bills(self, congress_session, bill_id, offset_num=1):
        "Take a specific bill, Retrurns related statements "
        offset=offset_num*20
        path = "{congress_session}/bills/{bill_id}/statements.json?offset={offset}".format(congress_session=congress_session, bill_id=bill_id, offset=offset)
        return self.fetch(path)

    def subjectlist(self, offset_num=1):
        "Retrun subject list "
        offset=offset_num*20
        path = "statements/subjects.json?offset={offset}".format(offset=offset)
        return self.fetch(path)

    def by_subject(self, subjects, offset_num=1):
        "Take a statement`s subjects "
        offset=offset_num*20
        path = "statements/subject/{subjects}.json?offset={offset}".format(subjects=subjects, offset=offset)
        return self.fetch(path)

    def by_member(self, member_id, congress_session=CURRENT_CONGRESS, offset_num=1):
        "Takes a member_id and congress session and return specific member`s statements"
        offset=offset_num*20
        path = "members/{member_id}/statements/{congress_session}.json?{offset}=20*offset".format(member_id=member_id, congress_session=congress_session, offset=offset)
        return self.fetch(path)

    def statements_content(self ,url):
        if url:
            soup= get_soup(url)
            p_subcontent = soup.find_all('p')
            b_subcontent = soup.find_all('b')
            p_content = '\n'.join([p.text.strip() for p in p_subcontent])
            b_content = '\n'.join([b.text.strip() for b in b_subcontent])
            content= p_content + b_content
            return content
        if not url:
            return 'sever errors'
        if not content:
            content = 'Not p tag'
            return content
