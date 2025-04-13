from odoo import  models, fields, api, _


class GalaxyDepartment(models.Model):
    _name = 'galaxy.department'
    _description = 'Galaxy Departments'



    d_name = fields.Char(string='Name')
    d_description = fields.Text(string='Description')
    doctor_id = fields.Many2one('galaxy.doctor','Doctor')

    # patient_ids = fields.One2many('galaxy.patient','dep_id','patient')