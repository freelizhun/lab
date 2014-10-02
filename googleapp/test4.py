#!/usr/bin/env python

import gdata.spreadsheet.service

email = 'jonahjun.wu@gmail.com'
password = '2xuiuiji'
spreadsheet_key = '1JTv-1rtlv6QbjgcKFnD9ENcl0kGijD4RTZfjBpDziEc' # key param
worksheet_id = 'od6' # default

def main():
    client = gdata.spreadsheet.service.SpreadsheetsService()
    client.debug = True
    client.email = email
    client.password = password
    client.source = 'test client'
    client.ProgrammaticLogin()
    
    rows = []
    rows.append({'id':'0','title':'First'})
    rows.append({'id':'1','title':'Second'})
    sheets = client.GetSpreadsheetsFeed()
    print '------------------------------------'
    print sheets
    print '------------------------------------'
    print map(lambda e: e.title.text + " : "  + e.id.text.rsplit('/', 1)[1],sheets.entry)
    """
    for row in rows:
        try:
            client.InsertRow(row, spreadsheet_key, worksheet_id)
        except Exception as e:
            print e
    """
    
    return
    
if __name__ == '__main__':
    main()
