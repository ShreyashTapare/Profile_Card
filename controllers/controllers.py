# # # -*- coding: utf-8 -*-
from odoo.http import route
# from addons.portal.controllers.portal import CustomerPortal
from odoo.addons.portal.controllers.portal import CustomerPortal


#Inherited Controller From 'my/account' 
class Inherted1Portal (CustomerPortal):

    @route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        v1 = super(Inherted1Portal, self).account(redirect=None, **post)
        print("it is working-----------------------------------------------------------------------------")
        CustomerPortal.OPTIONAL_BILLING_FIELDS.append("addhar_no")
        return v1


