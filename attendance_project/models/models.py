# -*- coding: utf-8 -*-

from odoo import models, fields, api

class attendance_project(models.Model):
    _inherit = 'hr.attendance'
    _description = 'Adding required fields to allow users to record Project, task and details'

    project_id = fields.Many2one(string='Project', comodel_name='project.project', required=True)
    task_id = fields.Many2one(string='Task', comodel_name='project.task', required=True)
    activity_description = fields.Text('Description', required=True)
    
    

