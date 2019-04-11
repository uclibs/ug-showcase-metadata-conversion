import pandas as pd

df = pd.read_csv('Cleaned_Showcase_Program_Datamkfin-csv.csv', sep=',')

def convert_row(row):
	return f"""<article xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" locale="en_US" section_ref="{row.SectionCode}" xsi:schemaLocation="http://pkp.sfu.ca native.xsd" stage="submission">
	<id type="internal">1</id>
	<title locale="en_US">{row.Title}</title>
	<prefix locale="en_US"></prefix>
	<abstract locale="en_US">&lt;p&gt;{statementOfResponsibility(row)}&lt;/p&gt;&#xD;
        &lt;p&gt;Advisor: {row.AdvisorFirst} {row.AdvisorLast}&lt;/p&gt;&#xD;
        &lt;p&gt;Presentation ID: {row.ProjectNumber}&lt;/p&gt;&#xD;
        &lt;p&gt;Abstract: {row.Abstract}&lt;p&gt;</abstract>
	<authors xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
		<author primary_contact="true" include_in_browse="true" user_group_ref="Author">
			<firstname>{row.FirstName1}</firstname>
			<lastname>{row.LastName1}</lastname>
			<email>{row.PresenterEmail1}</email>
		</author>
                {author2(row)}
                {author3(row)}
                {advisor(row)}
	</authors>
</article>
"""

def author2(row):
    if pd.isnull(row.FirstName2):
        return ''
    else:
        return f"""<author include_in_browse="true" user_group_ref="Author">
			<firstname>{row.FirstName2}</firstname>
			<lastname>{row.LastName2}</lastname>
			<email>{row.PresenterEmail2}</email>
		</author>"""

def author3(row):
    if pd.isnull(row.FirstName3):
        return''
    else:
        return f"""<author include_in_browse="true" user_group_ref="Author">
			<firstname>{row.FirstName3}</firstname>
			<lastname>{row.LastName3}</lastname>
			<email>{row.PresenterEmail3}</email>
		</author>"""

def advisor(row):
    if pd.isnull(row.AdvisorFirst):
        return''
    else:
        return f"""<author include_in_browse="true" user_group_ref="Advisor">
			<firstname>{row.AdvisorFirst}</firstname>
			<lastname>{row.AdvisorLast}</lastname>
			<email>{row.AdvisorEmail}</email>
		</author>"""

def statementOfResponsibility(row):
    firstauthor = '' if pd.isnull(row.FirstName1) else f"{row.FirstName1} {row.LastName1}, {row.PresenterMajor1}"
    secondauthor = '' if pd.isnull(row.FirstName2) else f"; {row.FirstName2} {row.LastName2}, {row.PresenterMajor2}"
    thirdauthor = '' if pd.isnull(row.FirstName3) else f"; {row.FirstName3} {row.LastName3}, {row.PresenterMajor3}"
    return f"By {firstauthor}{secondauthor}{thirdauthor}"

out = open('out.xml', 'a')
out.write("""<?xml version="1.0" encoding="UTF-8"?>
<articles xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
"""
)
out.write('\n'.join(df.apply(convert_row, axis=1)))
out.write("</articles>")
out.close()

