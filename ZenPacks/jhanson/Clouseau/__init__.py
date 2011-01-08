from ZenPacks.jhanson.Clouseau.config import *
from ZenPacks.jhanson.Clouseau.config import unique_id
from Products.CMFCore.DirectoryView import registerDirectory
from Products.ZenModel.ZenPack import ZenPackBase
registerDirectory('skins/ZenPacks.jhanson.Clouseau', product_globals)

try:
    import transaction
except ImportError:
    print "You must have Zope 2.9 for this library to work."
    raise

from Products.CMFCore import utils
from ZenPacks.jhanson.Clouseau.tools.clouseautool import ClouseauTool
import permissions

tools = ( ClouseauTool, )

def initialize(context):
    # check to see if it exists and set up the tool otherwise
    utils.ToolInit(
        product_name,
        tools=tools,
        icon='clouseau.jpg').initialize(context)


class ZenPack(ZenPackBase):
    def install(self, dmd):
        # create the object on the dmd
        if not hasattr(dmd, unique_id):
            tool = ClouseauTool()
            dmd._setObject(unique_id, tool)

