from odoo import models, fields, api


class VtexExtention(models.Model):
    # _name = 'vtex.extension'
    _inherit = 'product.template'




    vtex_id = fields.Char(string='Vtex Id')
    vtex_status = fields.Char(string='Vtex status')


    @api.model
    def check_company_for_update(self):
        print('hyy testing is successful')
        # if vtex_id !=None:
        #     for rec in vtex_status:
        #         if 'DuplicateKeyException' in rec:
        #             rec.vtex_status='404 error'
        #             print('testing12')
        #         else:
        #             print('error')
        #
