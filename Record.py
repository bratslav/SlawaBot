import urllib.request
import urllib.parse
from urllib.error import HTTPError

cln_id = 92012
gr_id = 7
cln_name = 'Иванов Иван'
data_br = '12.05.1985'

br_data = data_br[6:10]+data_br[3:5]+data_br[0:2]+'000000'

send_req = '''<?xml version="1.0" encoding="UTF-8"?>
    <Tables>
    <CLNT>
    <CLNTID>%i</CLNTID>
    <CLNTGRPID>%i</CLNTGRPID>
    <CLNTNAME>%s</CLNTNAME>
    <CLNTBIRTHDAY>%s</CLNTBIRTHDAY>
    <LOCKED>0</LOCKED>
    <DELFLAG>0</DELFLAG>
    <UPDATENUM>0</UPDATENUM>
    </CLNT>
    </Tables>''' % (cln_id, gr_id, cln_name, br_data)

print(send_req)

senddata = [('XML', send_req)]
senddata = urllib.parse.urlencode(senddata)
path = 'http://185.80.232.179:8090/5BC0F616-93ED-4E58-ACE5-37A1577C6A07/SaveTables?CallID=1&SystemID=1'
#req = urllib.request.Request(path, senddata)
req = urllib.request.Request(path, send_req)

req.add_header("Content-type", "application/x-www-form-urlencoded")
req.data = req.data.encode('utf-8')
try:
    result = urllib.request.urlopen(req)
    print(result.status)

except HTTPError as e:
    content = e.read()
    print(e)

