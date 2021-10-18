#!/usr/bin/env python3
#
#   Copyright (c) 2021 eGauge Systems LLC
#     1644 Conestoga St, Suite 2
#     Boulder, CO 80301
#     voice: 720-545-9767
#     email: dave@egauge.net
#
#   All rights reserved.
#
#   This code is the property of eGauge Systems LLC and may not be
#   copied, modified, or disclosed without any prior and written
#   permission from eGauge Systems LLC.
#
# pylint: disable=no-name-in-module
#
'''This module provides a helper function to ask for eGauge cloud API
credentials (aka eGuard credentials) via a popup dialog.  To use it,
pass the ask method to the TokenAuth's ask parameter after partially
evaluating it to bind the parent Qt window to "parent":

from functools import partial

import egauge.webapi.cloud.credentials

    # this `self' is a Pyside2 Ui_MainWindow:
    auth = webapi.auth.TokenAuth(ask=partial(credentials.ask, self))
    self.sn_api = webapi.cloud.SerialNumber(auth=auth)

'''
import getpass

from PySide2.QtWidgets import QDialog
from .gui.credentials_dialog import Ui_Credentials_Dialog

class LoginCanceled(Exception):
    '''Raised when the user cancels a login request.'''

class Credentials_Manager:
    def __init__(self, gui_parent=None):
        '''Create a credentials manager.  The task of this manager is mainly
        to track if a previous login failed.  The creator of this
        object should set the object's previous_login_failed member
        according to the success/failure of a login.

        If GUI_PARENT is not None, it must be the QT5 (PySide2) parent
        window to use for the dialog.  If it is None, the credentials
        will be requested via standard I/O (getpass).

        '''
        self.parent = gui_parent
        self.previous_login_failed = False

    def ask(self):
        '''Ask for the username, password, and optional token for an eGauge
        cloud API account (eGuard account).  Returns a tuple
        containing a username and password or raises LoginCanceled if
        the user presses the "Cancel" button.

        '''
        if self.parent:
            dialog = Credentials_Dialog(self.parent,
                                        self.previous_login_failed)
            dialog.exec_()
            if not dialog.accepted:
                raise LoginCanceled()
            return (dialog.username, dialog.password + dialog.token)

        fail_msg = ''
        if self.previous_login_failed:
            fail_msg = 'Login failed.  '
        print('%sPlease enter eGuard credentials.' % fail_msg)
        try:
            usr = input('Username: ')
            pwd = getpass.getpass(prompt='Password[+token]: ')
        except (KeyboardInterrupt, EOFError) as e:
            raise LoginCanceled from e
        return [usr, pwd]

class Credentials_Dialog(QDialog, Ui_Credentials_Dialog):
    def __init__(self, parent, failed):
        self.accepted = False
        self.username = None
        self.password = None
        self.token = ''
        super().__init__(parent)
        self.setupUi(self)
        if failed:
            prompt = 'Login failed. ' + self.prompt_label.text()
            self.prompt_label.setText(prompt)
        self.username_lineEdit.setFocus()

    def exec_(self):
        self.accepted = False
        super().exec_()

    def accept(self):
        super().accept()
        self.accepted = True
        self.username = self.username_lineEdit.text()
        self.password = self.password_lineEdit.text()
        self.token = self.token_lineEdit.text()
