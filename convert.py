import pandas as pd

df = pd.read_csv('Cleaned_Showcase_Program_Datamkfin-csv.csv', sep=',')
nl = '\n\n'
def convert_row(row):
	return f"""<?xml version="1.0" encoding="UTF-8"?>
<articles xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
<article xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	locale="en_US" section_ref="{row.Session}" xsi:schemaLocation="http://pkp.sfu.ca native.xsd"
	stage="submission">
	<id type="internal">1</id>
	<title locale="en_US">{row.Title}</title>
	<prefix locale="en_US"></prefix>
	<abstract locale="en_US">{statementOfResponsibility(row)}.{nl}Advisor: {row.AdvisorFirst} {row.AdvisorLast}{nl}{row.Abstract}</abstract>
	<authors xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
		<author primary_contact="true" user_group_ref="author">
			<firstname>{row.FirstName1}</firstname>
			<lastname>{row.LastName1}</lastname>
			<email>{row.PresenterEmail1}</email>
		</author>
                {author2(row)}
                {author3(row)}
	</authors>
</article>
"""

def author2(row):
    if pd.isnull(row.FirstName2):
        return ''
    else:
        return f"""<author primary_contact="true" user_group_ref="author">
			<firstname>{row.FirstName2}</firstname>
			<lastname>{row.LastName2}</lastname>
			<email>{row.PresenterEmail2}</email>
		</author>"""

def author3(row):
    if pd.isnull(row.FirstName3):
        return''
    else:
        return f"""<author primary_contact="true" user_group_ref="author">
			<firstname>{row.FirstName3}</firstname>
			<lastname>{row.LastName3}</lastname>
			<email>{row.PresenterEmail3}</email>
		</author>"""

def statementOfResponsibility(row):
    firstauthor = '' if pd.isnull(row.FirstName1) else f"{row.FirstName1} {row.LastName1}"
    secondauthor = '' if pd.isnull(row.FirstName2) else f", {row.FirstName2} {row.LastName2}"
    thirdauthor = '' if pd.isnull(row.FirstName3) else f", {row.FirstName3} {row.LastName3}"
    return f"By {firstauthor}{secondauthor}{thirdauthor}"

print('\n'.join(df.apply(convert_row, axis=1)))

