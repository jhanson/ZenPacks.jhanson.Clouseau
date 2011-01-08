
import os, time

def test(self):
	data = self.REQUEST.get("string")
	output = eval(data)
	self.REQUEST.RESPONSE.setHeader('content-type', 'text/xml')
	res = """<?xml version="1.0" ?>
<response>
	<line>%s</line>
	<line>%s</line>
</response>
""" % (data, output)
	return res