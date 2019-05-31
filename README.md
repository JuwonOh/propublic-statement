# Propublic-Statement

propublic-statement crawls statements in propublica api (https://projects.propublica.org/api-docs/congress-api/). Members, bills, votes, committees, and nominations provided by propublica api are provided by propublica-congress (https://github.com/eyeseast/propublica-congress). This package adds the statement functionality to the framework provided by propublica-congress.

I will extend the function of making each statement into individual json file in the future.

## User guide

Packages include init.py, client.py, statement.py, util.py, and usage-statement.ipynb. init.py and client.py are identical in functionality to the existing propublica-congress package. statement.py shows the statement according to a certain condition, or shows the subject of the statements. We created a function to collect the contents of the statement by collecting the URL of the statement provided by api temporarily by creating the statements_content function.
usage-statement.ipynb shows how the functions provided by the propublica-statement function in dataframe format.

## usage

class congress.statement.StatementClient(apikey=None, cache='.cache', http=None)

latest_get()
Return the latest public realease.

by_member(member_id, congress_session, offset_num=1)
Return statements for a specific member, defaulting to the fist_page.

by_terms(serch_terms, offset_num=1)
Return statements by a specific unicode term.

by_date(date, offset_num=1)
Return statements by a specific date.

by_bill(congress_session, bill_id, offset_num=1)
Return statements by a specific bill and chamber.

subjectlist(offset_num)
View statement`s subjectlist.

by_subject(subjects, offset_num=1)
Return statements by a specific subject
