# -*- coding: utf-8 -*-
# vim: ts=4
###
#
# LibreOffice Extension to Transcribe spanish spelling to Andalûh (EPA).
# Further details: https://andaluh.es
#
# Copyleft (c) 2021 AndaluGeeks Team
#
# Authors:
#   J. Félix Ontañón <felixonta@gmail.com>

import sys
import logging

import unohelper
from com.sun.star.task import XJobExecutor

# pip3 install andaluh
import andaluh

ImplementationName = "org.openoffice.comp.pyuno.AndaluhLibre"
ServiceName = "com.sun.star.task.Job"

# Recuersively iterates over table objects
def transcribe_table(t, vaf='ç', vvf='h'):
    t = list(t) if type(t) is tuple else t

    for i in range(0, len(t)):
        if type(t[i]) == str:
            t[i] = andaluh.epa(t[i], vaf, vvf)
        else:
            t[i] = transcribe_table(t[i], vaf, vvf)

    return list(t)

# Extension base class
class AndaluhLibre(unohelper.Base, XJobExecutor):
    def __init__(self, ctx):
        self.ctx = ctx
        self.desktop = self.ctx.ServiceManager.createInstanceWithContext( "com.sun.star.frame.Desktop", self.ctx )
        self.document = self.desktop.getCurrentComponent()

    # Credits to Barcode LibreOffice Extension: https://github.com/LibreOffice/barcode
    def createdialog(self, dialogname ):
        psm = self.ctx.ServiceManager
        dlgprovider = psm.createInstance('com.sun.star.awt.DialogProvider')
        dlg = dlgprovider.createDialog('vnd.sun.star.script:AndaluhDialogs.%s?location=application'%(dialogname))

        class Wrapper( object ):
            def __init__( self, dlg ):
                object.__setattr__( self, 'xdialog', dlg )
            def __getattr__( self, name ):
                return getattr( self.xdialog, name )
            def __setattr__( self, name, value ):
                try:
                    setattr( self.xdialog, name, value )
                except AttributeError:
                    object.__setattr__( self, name, value )

        dlg = Wrapper( dlg )

        for c in dlg.getControls():
            setattr( dlg, c.Model.Name, c )
        return dlg

    def transcription(self, parenum, vaf='ç', vvf='h'):
        while parenum.hasMoreElements():
            par = parenum.nextElement()

            # Text paragraphs
            if hasattr(par, "createEnumeration"):
                textenum = par.createEnumeration()

                while textenum.hasMoreElements():
                    text = textenum.nextElement()

                    if text.getString():
                        text.setString(andaluh.epa(text.getString(), vaf, vvf))

            # Tables
            elif hasattr(par, "getDataArray"):
                tab = par.getDataArray()
                tab = transcribe_table(tab, vaf, vvf)
                tup = tuple(tab)
                par.setDataArray(tup)

            else:
                pass

    # This is what the dialog triggers. From Menu or Toolbar.
    def trigger(self, args):
        dlg = self.createdialog( 'TranscriptorDlg' )
        ok = dlg.execute()

        if not ok:
            return

        # Read user preferences from dialog
        vaf = dlg.zezeo.State and 'z' or dlg.seseo.State and 's' or dlg.heheo.State and 'h' or dlg.çeçeo.State and 'ç' or 'ç'
        vvf = dlg.jota.State and 'j' or dlg.aspirada.State and 'h' or 'h'

        # When full transcription is selected
        if dlg.completo.State:
            # Transcribe the document header
            # Reference: https://forum.openoffice.org/en/forum/viewtopic.php?f=20&t=89910
            style = self.document.StyleFamilies.getByName("PageStyles").getByName("Standard")
            header_parenum = style.HeaderText.createEnumeration()
            self.transcription(header_parenum, vaf, vvf)

            # Transcribe the document content
            doc_parenum = self.document.Text.createEnumeration()
            self.transcription(doc_parenum, vaf, vvf)

        # Or whether to transcribe selected text only
        else:
            controller = self.document.getCurrentController()
            selection = controller.getSelection()
            xTextRange = selection.getByIndex(0)
            parenum = xTextRange.createEnumeration()
            self.transcription(parenum, vaf, vvf)

# uno implementation
g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(AndaluhLibre, ImplementationName, (ServiceName,),)