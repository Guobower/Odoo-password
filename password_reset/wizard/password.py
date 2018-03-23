# -*- coding: utf-8 -*-

from odoo import *


class set_password(models.Model):
    _name = 'set.password'

    @api.multi
    def action_reset_password(self):
        res_user = self.env['res.users']
        users_ids = res_user.search([])
        for user in res_user.browse(users_ids):
            if not user.id == 1:
                for users in user.id:
                    if users.partner_id.email:
                        res_user.reset_password(users.partner_id.email)
        return True


class password(models.TransientModel):
    _name = 'password'

    @api.multi
    def action_reset_password(self):
        res_user = self.env['res.users']
        users_ids = res_user.search([])
        for user in res_user.browse(users_ids):
            if not user.id == 1:
                for users in user.id:
                    if users.partner_id.email:
                        res_user.reset_password(users.partner_id.email)
        return True