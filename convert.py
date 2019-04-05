import pandas as pd

df = pd.read_csv('ShowcaseProgram.csv', sep=',')

def convert_row(row):
	return f"""<?xml version="1.0" encoding="UTF-8"?>
<articles xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
<article xmlns="http://pkp.sfu.ca" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	locale="en_US" section_ref="ART" xsi:schemaLocation="http://pkp.sfu.ca native.xsd"
	stage="submission">
	<id type="internal">1</id>
	<title locale="en_US">{row.title}</title>
	<prefix locale="en_US">{row.prefix}</prefix>
	<abstract locale="en_US">{row.abstract}</abstract>
	<authors xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
		xsi:schemaLocation="http://pkp.sfu.ca native.xsd">
		<author primary_contact="true" user_group_ref="author">
			<firstname>{row.authorfirstname}</firstname>
			<lastname>{row.authorlastname}</lastname>
			<email>{row.authoremail}</email>
		</author>
	</authors>
</article>
"""
print('\n'.join(df.apply(convert_row, axis=1)))
