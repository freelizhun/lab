import gdata.docs
import gdata.docs.service
import gdata.spreadsheet.service
import re, os

# Connect to Google
username        = 'jonahjun.wu@gmail.com'
passwd          = '2xuiuiji'
doc_name        = 'apitest'
gd_client = gdata.spreadsheet.service.SpreadsheetsService()
gd_client.email = username
gd_client.password = passwd
gd_client.source = 'payne.org-example-1'
gd_client.ProgrammaticLogin()
q = gdata.spreadsheet.service.DocumentQuery()
q['title'] = doc_name
q['title-exact'] = 'true'
feed = gd_client.GetSpreadsheetsFeed(query=q)
spreadsheet_id = feed.entry[0].id.text.rsplit('/',1)[1]
feed = gd_client.GetWorksheetsFeed(spreadsheet_id)
worksheet_id = feed.entry[0].id.text.rsplit('/',1)[1]

rows = gd_client.GetListFeed(spreadsheet_id, worksheet_id).entry
print rows
for row in rows:
    for key in row.custom:
        print " %s: %s" % (key, row.custom[key].text)
    print
row_data={}
row_data['id']="test1"
row_data['title']="test1"
gd_client.InsertRow(row_data, spreadsheet_id, worksheet_id)
