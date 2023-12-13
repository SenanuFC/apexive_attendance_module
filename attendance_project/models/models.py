# -*- coding: utf-8 -*-

from odoo import models, fields, api


class attendance_project(models.Model):
    _name = 'attendance_project.attendance_project'
    _description = 'attendance_project.attendance_project'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100



class attendance_project(models.Model):
    _inherit = 'hr.attendance'
    _description = 'Adding required fields to allow users to record Project, task and details'

    
    project_id = fields.Many2one(string='Project', comodel_name='project.project', required=True)
    task_id = fields.Many2one(string='Task', comodel_name='project.task', required=True)
    activity_description = fields.Text('Description', required=True)
    
    

