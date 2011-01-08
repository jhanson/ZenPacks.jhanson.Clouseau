from Products.CMFCore.DirectoryView import createDirectoryView
from Products.CMFCore.utils import getToolByName

from Products.CMFCore.permissions import ManagePortal
from ZenPacks.jhanson.Clouseau.config import layer_name, layer_location, unique_id

def install(self):
    """ Install this product """
    out = []
    skinsTool = getToolByName(self, 'portal_skins')

    # add in the directory view pointing to our skin
    if layer_name not in skinsTool.objectIds():
        createDirectoryView(skinsTool, layer_location, layer_name)
        out.append('Added "%s" directory view to portal_skins' % layer_name)

    # add in the layer to all our skins    
    skins = skinsTool.getSkinSelections()
    for skin in skins:
        path = skinsTool.getSkinPath(skin)
        path = [ p.strip() for p in path.split(',') ]
        if layer_name not in path:
            if 'custom' in path:
                pos = path.index('custom') + 1
            else:
                pos = 0
            path.insert(pos, layer_name)
            path = ", ".join(path)
            skinsTool.addSkinSelection(skin, path)
            out.append('Added "%s" to "%s" skins' % (layer_name, skin))
        else:
            out.append('Skipping "%s" skin' % skin)

        try:
                ctool = getToolByName(self, unique_id)
        except AttributeError:
                self.manage_addProduct['Clouseau'].manage_addTool('Clouseau', None)
    cp = getToolByName(self, "portal_controlpanel")

    if "Clouseau" not in [ c.id for c in cp._actions ]:
        cp.registerConfiglet(
                "Clouseau",
            "Clouseau",
            "string:${portal_url}/clouseau_list",
            category="Products",
            permission="Manage portal",
            appId="Clouseau",
            imageUrl="clouseau.png",)

    cssreg = getToolByName(self, 'portal_css', None)
    skins = ["SyntaxHighlighter.css", "clouseau.css"]
    if cssreg is not None:
        for skin in skins:
            stylesheet_ids = cssreg.getResourceIds()
            if skin not in stylesheet_ids:
                cssreg.registerStylesheet(skin)
                out.append("Registered %s" % skin)
    
    # add in the clearspell js
    jsreg = getToolByName(self, 'portal_javascripts', None)
    scripts = ["clouseau_trigger.js",]
    if jsreg is not None:
        for script in scripts:
            if script not in jsreg.getResourceIds():
                jsreg.registerScript(script)
                out.append('Registered %s' % script)
                            
    actionsTool = getToolByName(self, 'portal_actions', None)
    if actionsTool is not None:
        for action in actionsTool.listActions():
            if action.getId() == 'clouseau_view':
                break # We already have the action
        else:
            actionsTool.addAction('clouseau_view',
                name='Python prompt',
                action='''python:"javascript:showClouseau('%s');" % '/'.join(object.getPhysicalPath())''',
                condition='python:portal.clouseau_tool.enabled',
                permission=ManagePortal,
                category='document_actions',
                visible=1,
                )
        out.append("Added 'clouseau_view' action to actions tool.")

    iconsTool = getToolByName(self, 'portal_actionicons', None)
    if iconsTool is not None:
        for icon in iconsTool.listActionIcons():
            if icon.getActionId() == 'clouseau_view':
                break # We already have the icon
        else:
            iconsTool.addActionIcon(
                category='plone',
                action_id='clouseau_view',
                icon_expr='clouseau.png',
                title='Python prompt',
                )
        out.append("Added 'clouseau_view' icon to actionicons tool.")
    
    return "\n".join(out)
    

def uninstall(self):
    out = []

    # remove the configlets from the portal control panel
    cp = getToolByName(self, 'portal_controlpanel', None)
    if "Clouseau" in [ c.id for c in cp._actions ]:
        cp.unregisterConfiglet("Clouseau")
        out.append('Removed configlet %s Clouseau')

    # remove action from portal_actions
    actionsTool = getToolByName(self, 'portal_actions', None)
    if actionsTool is not None:
        index = 0
        for action in actionsTool.listActions():
            if action.getId() == 'clouseau_view':
                actionsTool.deleteActions(selections=(index,))
                out.append('Removed action %s Clouseau')
            index += 1

    out.append('Successfully uninstalled %s.Clouseau')
    return "\n".join(out)
