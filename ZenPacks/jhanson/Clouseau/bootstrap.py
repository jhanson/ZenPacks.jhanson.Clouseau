# this is the first code that is run by a session
import Zope2
import os
from Products.ZenUtils.Utils import set_context
from Testing.makerequest import makerequest
from cStringIO import StringIO

CONF_FILE = os.path.join(os.environ['ZENHOME'], 'etc', 'zope.conf')
_ = Zope2.configure(CONF_FILE)
app = Zope2.app()
app = set_context(app)
dmd = app.zport.dmd
zport = app.zport
sync  = zport._p_jar.sync
find  = dmd.Devices.findDevice
devices = dmd.Devices


# login the current user
response_output = StringIO()
app = makerequest(app, stdout=response_output)

# load the zcmls

# context is added in the new_namespace
if context:
    context = app.unrestrictedTraverse(context, None)
    if context is None:
        del context
else:
    # not needed
    del context


# underscore is so that the results are not sent to the input
_ = login(app, userid)
# clean out variables

try:
    del self
except NameError:
    pass

del transaction_manager
del userid
del StringIO
del makerequest
del os
del CONF_FILE
del Zope2
del set_context
del response_output
"Welcome to the Zenoss dmd command shell!"
