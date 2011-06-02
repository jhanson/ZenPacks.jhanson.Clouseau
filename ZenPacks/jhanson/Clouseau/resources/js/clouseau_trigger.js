Ext.onReady(function () {

    function toggleClouseau(){
        var win;
        if (Ext.getCmp('clouseauWindow')){
            win = Ext.getCmp('clouseauWindow');
            win.close();
            return;
        }

        win = new Ext.Window({
            id: 'clouseauWindow',
            width: 800,
            height: 400,
            title: _t('ZenDMD'),
            plain: true,
            closeAction: 'destroy',
            html:'<iframe frameborder="0" width="100%" height="100%" src="/zport/dmd/web_dmd"></iframe>'
        });
        win.show();
    }

    // add the glass icon to the bottom of the page
    Ext.ComponentMgr.onAvailable('footer_bar', function(config) {
        config.items = config.items || [];
        config.items.push({
            xtype: 'button',
            id: 'show_inspector',
            icon: '/++resource++clouseau/img/clouseau.png',
            handler: function(button) {
                toggleClouseau();
            }
        });

        config.items.push('-');
    });

});