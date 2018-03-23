# -*- coding: utf-8 -*-

from odoo import fields, models, api


class password_history(models.Model):
    _name = 'password_history'

    name = fields.Char(string='Password', required=True)
    user_id = fields.Many2one('res.users', string="User", required=True)

class res_users(models.Model):
    _inherit = 'res.users'

    password_history_ids = fields.One2many('password.history', 'user_id', string="User")
