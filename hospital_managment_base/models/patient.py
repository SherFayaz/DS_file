from email.policy import default

from odoo import models, api, fields, _
from odoo.exceptions import UserError, ValidationError
from datetime import datetime


class GalaxyPatients(models.Model):
    _name = 'galaxy.patient'
    _description = 'Galaxy patients'

    # sequence number
    sequences = fields.Char(string='Sequence No', required=True, readonly=True, default=lambda self: _('New'))

    p_name = fields.Char('Name')
    p_dob = fields.Integer(string='DOB')
    p_age = fields.Integer('Age')
    p_gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], default='male')
    p_contact = fields.Char('Contact Info')
    p_email = fields.Char(string='Email', default='testing@gmail.com')
    p_merital_status = fields.Selection([('single','Single'),('marriage','Marriage')], default='single')

    #medical info
    p_bp = fields.Integer(string='Blood Pressure')
    p_med = fields.Text(string='Current Medications')
    p_A_date = fields.Date(string='Admission Date')
    P_d_date = fields.Date(string='Discharge Date')
    p_status = fields.Selection([('inpatient','Inpatient'),('outpatient','Outpatient'),('discharge','Discharged')], default='inpatient')

    #department & hospital related
    # many to one
    p_deptt = fields.Char('department')
    doctor_id = fields.Many2one('galaxy.doctor', string='Doctor')
    dep_id = fields.Many2one('galaxy.department','Department')
    # p_merital_status = fields.Selection([('single', 'Single'), ('marriage', 'Marriage')], default='single',
    #                                     related='doctor_id.dr_gender')


    # @api.onchange('doctor_id')
    # def _discount_for_patient(self):
    #    self.update({
    #        'dr_email':'Patientupdated@gmail.com'
    #    })

    '''override the create to generate the sequence number for patient'''
    @api.model
    def create(self, vals):
        if vals.get('sequences', _('New')) == _('New'):
            vals['sequences'] = self.env['ir.sequence'].next_by_code(
                'galaxy.patient') or _('New')
        res = super(GalaxyPatients, self).create(vals)
        return res
