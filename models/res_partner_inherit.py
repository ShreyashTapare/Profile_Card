# -*- coding: utf-8 -*-

from odoo import models, fields

#Inherited Module From 'res.partner' 
#some Changes Lets try

class portal_profile(models.Model):
    _name = 'res.partner'
    _inherit = "res.partner"
    _description = 'New Additional Fields'

    addhar_no = fields.Text(string="Addhar No")
