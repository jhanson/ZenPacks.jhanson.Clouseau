Clouseau
=========

ZenPacks.jhanson.Clouseau

It's a Ajax based Zope/Python prompt. Think of it is as a convenient zendmd. This is a port of the Plone project "Clouseau" to the zenoss environment. Because the zenoss and plone
environments are so different, some of the Clouseau features have been disabled. They will be enabled as I get around to fixing their implementation.

* Get the code on [GitHub][repo]

Try it!
=======

    $ git clone git://github.com/jhanson/ZenPacks.jhanson.Clouseau.git
    $ zenpack --install ZenPack.jhanson.Clouseau
In your lower left hand corner of your browser window you should notice a magnifying glass icon. Click that to start Clouseau

Requires
=======
* Zenoss 3.0++
* Firefox 3.0+
* Seems to work in Chrome/Safari as well, I haven't really tested in IE

Todo
=======
* session switching, right now everything is in one session
* session saving/restoring

Security
========
This is taken from the original clouseau's README.txt
Is it secure?

    Probably not. All the methods that interact with the application are protected by Zope security. So if you trust that code, you'll be happy. However chances are if you know Plone and Zope you might be screaming at this point.

    It does fly in the face of the traditional security model a bit, although essentially you are allowing anyone who has Manager to do anything to your site. Running this on a production site is crazy. From the page template in Clouseau...

    Warning: this tool allows users to interact with your Zope at its most basic level. It will allow a user to add, edit, delete any data in the site  ignoring all security. This tool should only be used on development sites. If you are at all unsure, stop, back away and uninstall this product immediately and go and read the documentation in the source.

First, how can I protect my installation?

    There are two variables *enabled* and *enabled_only_in_debug_mode*. Both of these are defined in config.py. If you would like to turn Clouseau off, then set enabled = False. If you'd like clouseau to work only when Zope is in debug-mode then leave *enabled_only_in_debug_mode* = True.

    Note: by default Clouseau is set to *enabled* = True and *enabled_only_in_debug_mode* = True. If you are running in production mode, restart your server in debug-mode.

Next, will this work?

    Probably. It's got quite a way to go yet. See to do.

Why browser based?

    1) Ease of end users, this has NO dependencies (compare to PloneShell or zopectl)

    2) Collaborative debugging, multiple people can join a session and see the same data

    3) Lots of features we haven't gotten too yet.

    4) Ease of development, no hacking down in wxPython or Zope sources.

Thanks
=======
    Thanks goes out to the Andy McKay for making the awesome Clouseau project for Plone.

License
=======
Copyright 2010 Joseph Hanson

ZenPacks.jhanson.Clouseau is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

ZenPacks.jhanson.Clouseau is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with ZenPacks.jhanson.Clouseau. If not, see http://www.gnu.org/licenses/.

[website]: http://github.com/jhanson/ZenPacks.jhanson.Clouseau
[repo]: http://github.com/jhanson/ZenPacks.jhanson.Clouseau

