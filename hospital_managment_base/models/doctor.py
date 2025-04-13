from email.policy import default


import warnings

from addons.odoo.tools.populate import compute
from odoo import models, fields, api, _
from odoo.addons.test_impex.tests.test_load import values
from odoo.exceptions import UserError


class DoctorDetail(models.Model):
    _name = 'galaxy.doctor'
    _description = 'Doctor Details Information'
    _rec_name = 'dr_name'

    # sequence number
    sequences = fields.Char(string='Sequence No', required=True, readonly=True, default=lambda self: _('New'))

    dr_name = fields.Char(string='Name')
    dr_gender = fields.Selection([('male','Male'),('female','Female')], defaul='male', string='Gender')
    dr_contact = fields.Char('Doctor Number')
    dr_email = fields.Char(string='Email')
    dr_address = fields.Text('Address')

    #professional fields
    dr_specialization = fields.Char(string='Specialization')
    dr_qualification = fields.Selection([('mbbs','MBBS'),('fcps','FCPS'),('general','General')], default='general')
    dr_expr = fields.Integer('Experience')
    dr_designation = fields.Char('Designation')

    #work detail
    dr_department = fields.Char('Department')
    dr_availabity = fields.Selection([('yes','Yes'),('no','No')], default='no')
    dr_fees = fields.Float(string='Doctor Fees')
    medicine_fee = fields.Float(string="Medicine Fee")
    total_fee = fields.Float(string='Total Fee', compute='_total_patient_fee', store=True)

    #for doctor sallary compute methods
    working_hr = fields.Float(string='No of working hours')
    fee_per_hour = fields.Float(string='Fee per hour')
    total_over_time = fields.Float(string='Total Over Time Fee', compute="_calculate_total_over_time", store=True)

    #relational fields
    patient_id = fields.Many2one('galaxy.patient','Patient')
    deptt_id = fields.Many2one('galaxy.department','Department')

    #compute methods
    '''calculate the doctor overtime '''
    # def _calculate_total_over_time(self):
    #     for rec in self:
    #         self.total_over_time = rec.working_hr * rec.fee_per_hour


    '''to calculate the doctor fee as medicine & doctor fee'''
    def _total_patient_fee(self):
        for rec in self:
            self.total_fee = rec.dr_fees + rec.medicine_fee

    #through depand methods
    @api.depends('working_hr','fee_per_hour')
    def _calculate_total_over_time(self):
        for rec in self:
            rec.total_over_time = rec.working_hr * rec.fee_per_hour



    #onchange_methods
    @api.onchange('dr_name')
    def _onchange_emails(self):
        self.dr_address = "Fayyaz@gmail.com"


    # search all the record without any filter.
    '''searching  for all doctor'''
    # def orm_methods(self):
    #     Doctors = self.env['galaxy.doctor'].search([])
    #     for re in Doctors:
    #         print('doct_name', re.dr_name, 'doct_gender', re.dr_gender)

 # search about the specific filter(conditions)
    '''base on specific condition search '''
    # def orm_methods(self):
    #     Doctors = self.env['galaxy.doctor'].search([('dr_gender', '=', 'male')])
    #     for re in Doctors:
    #         print('doct_name',re.dr_name, 'doct_gender', re.dr_gender)
    #     # print('rec =========>>>', Doctors)


    #search_counts
    '''to counts all the numbers of record in the model base on the specific condition'''
    # def orm_methods(self):
    #     doc_counts = self.env['galaxy.doctor'].search_count([('dr_gender', '=', 'male')])
    #     print('the tottal number of doctor are===============>', doc_counts)


    #browse methods
    '''To browse all the records base on their ids'''
    # def orm_methods(self):
    #     doctor_model = self.env['galaxy.doctor']
    #     all_ids = doctor_model.search([]).ids  # Get list of all doctor IDs
    #     recs = doctor_model.browse(all_ids)  # Browse those records
    #     for re in recs:
    #         print('doct_name:', re.dr_name, 'doct_gender:', re.dr_gender)


    '''browse the for the specific id and retrieve a record'''
    # def orm_methods(self):
    #     doctor = self.browse([1])
    #     print('the doctor are  created! ===============>>',doctor.dr_name)


    #create methods
    '''creating a new record in database'''
    # def orm_methods(self):
    #     doctor = self.env['galaxy.doctor'].create({'dr_name':'Maaz Alam'})
    #     print('the doctor are  created! ===============>>',doctor)

    # write methods
    '''updating a record in database'''
    # def orm_methods(self):
    #     doctor_update = self.write({'dr_name':'Maaz Alam Odoo Technical developer!', 'dr_gender':'male'})
    #     print('the doctor are  created! ===============>>',doctor_update)

    #copy methods
    '''To copy the existing record with the defaults values'''
    # def orm_methods(self):
    #     cop_doc = self.copy({'dr_name':'Maaz Alam'})
    #     print('The doctor are successfully duplicated........>', cop_doc.dr_name, cop_doc.dr_gender)



    #unlink methods
    '''deleting the particular record from the database!'''
    # def orm_methods(self):
    #     delete_doc = self.env['galaxy.doctor'].browse(10).unlink()
    #     print('The duplicated Record are Deleted.=============>>', delete_doc)

    '''Deleting the current record from the db'''
    # def orm_methods(self):
    #     delete_doc = self.env['galaxy.doctor'].unlink()
    #     print('The duplicated Record are Deleted.=============>>', delete_doc)


    #ensure_one()
    '''to check weather the record are single or not'''
    # def orm_methods(self):
    #     delete_doc = self.ensure_one()
    #     print('The duplicated Record are presence!=============>>', delete_doc, delete_doc.dr_name)



    # filter()
    '''Filter a record base on the specific condition'''
    # def orm_methods(self):
    #     male_doctor = self.env['galaxy.doctor'].filtered(lambda doctor:doctor.dr_gender == False)
    #     print('Retrieve all male Doctors!=============>>', male_doctor, male_doctor.dr_name)

    '''filter methods to check only the female doctor'''
    # def orm_methods(self):
    #     male_doctor = self.env['galaxy.doctor'].search([('dr_gender', '=', 'male')])
    #     print('Retrieve all male Doctors!=============>>', male_doctor.filtered(lambda o:o.dr_gender).mapped('dr_name'))


    '''only male doctor are retrieve using map methods'''
    # def orm_methods(self):
    #     doc = self.env['galaxy.doctor'].filtered(lambda x: x.dr_gender == "male")
    #     print('only male doctor are Retrieve ',doc.dr_name)

    #mapped()
    '''The mapped method are iterates on every record over the recordset'''
    # def orm_methods(self):
    #     for re in self:
    #         doc = self.env['galaxy.doctor'].search([])
    #         print('the Doctor are! ', doc.mapped('dr_name'))


    #mapped methods
    '''mapping all doctor with male gender'''
    # def orm_methods(self):
    #     doc = self.env['galaxy.doctor'].search([('dr_gender', '=', 'male')]).mapped('dr_name')
    #     print('only male doctor are Retrieve ',doc)



    #sorted methods
    '''sorting name using the sorted methods and combine with mapped method to & reverse order'''
    # def orm_methods(self):
    #     sort_name = self.env['galaxy.doctor'].search([]).sorted(key= lambda m:m.dr_name, reverse=True)
    #     print('sorted name of the doctors', sort_name.mapped('dr_name'))
    #

    def orm_methods(self):
        pass












    '''override the create to generate the sequence number for doctor'''
    # @api.model
    # def create(self, vals):
    #     if vals.get('sequences', _('New')) == _('New'):
    #         vals['sequences'] = self.env['ir.sequence'].next_by_code(
    #             'galaxy.doctor') or _('New')
    #     res = super(DoctorDetail, self).create(vals)
    #     return res


    '''override a create method to create a new record'''
    # @api.model
    # def create(self, data_list):
    #     # print('the values', data_list)
    #     # print('the self before...', self)
    #     data_list['dr_expr']= 4 #setting the default values to the create methods
    #     rtn = super(DoctorDetail, self).create(data_list)
    #     # print('the self after', rtn)
    #     return rtn


    '''override the write method to update any records'''

    # def write(self, vals):
    #     print('the list of values', vals)
    #     rtn = super(DoctorDetail, self).write(vals)
    #     print('the Return', rtn)
    #     return rtn


    '''override the copy method to duplicate the records'''
    # def copy(self, default={}):
    #     # print('the default values', default)
    #     # print('the self ', self)
    #     default['dr_name'] = self.dr_name+"(Copy)"
    #     rtn = super(DoctorDetail, self).copy(default=default)
    #     # print('the return response', rtn)
    #     rtn.dr_fees = 2500
    #     return rtn


    '''override unlink methods to delete the existing records'''
    # def unlink(self):
    #     for doc in self:
    #         if doc.dr_fees > 0:
    #             raise UserError(_("%s you cont delete this record!"%doc.dr_name))
    #     rtn = super(DoctorDetail, self).unlink()
    #     print('the return are ', rtn)


    '''override the name_create method to create name of the doctor'''
     #    # def name_create(self, dr_gender):
        #     rtn = self.create({'dr_gender':'dr_gender'})
        #     # print("rtn.name_get()[0]", rtn.name_get()[0])
        #     return rtn.name_get()[0]


        # '''override the default_get methods'''
        # @api.model
        # def default_get(self, fields_list=[]):
        #     rtn = super().default_get(fields_list)
        #     rtn['dr_expr'] = 3
        #     rtn['dr_gender'] = 'female'
        #     return rtn