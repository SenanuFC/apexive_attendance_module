# -*- coding: utf-8 -*-
from odoo import http
from odoo.addons.hr_attendance.controllers.main import HrAttendance
from odoo.http import request

import logging
_logger = logging.getLogger(__name__)




class AttendanceProject(HrAttendance):
#     @http.route('/attendance_project/attendance_project', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/attendance_project/attendance_project/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('attendance_project.listing', {
#             'root': '/attendance_project/attendance_project',
#             'objects': http.request.env['attendance_project.attendance_project'].search([]),
#         })

#     @http.route('/attendance_project/attendance_project/objects/<model("attendance_project.attendance_project"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('attendance_project.object', {
#             'object': obj
#         })

# Create route to fetch all projects related to a passed employee_id
    @http.route('/hr_attendance/get_projects', auth='public', type='json')
    def get_projects(self, employee_id=None, **kw):
        _logger.info(f'Employee ID: {employee_id}')
        # Fetch the user_id of the passed employee_id
        user_id = http.request.env['hr.employee'].sudo().search([('id', '=', employee_id)]).user_id.id     
        _logger.info(f'User ID: {user_id}')
        
        project_tasks = http.request.env['project.task'].sudo().search([('user_ids', 'in', user_id)])
        _logger.info(f'Project Tasks: {project_tasks}')
        
        # Get the projects of the project_tasks
        projects = http.request.env['project.project'].sudo().search([('id', 'in', project_tasks.project_id.ids)])
        
        _logger.info('Extending controller')
        return projects.read(['name', 'id'])
    
    
    # Create route to fetch all tasks related to a passed project_id and employee_id
    @http.route('/hr_attendance/get_tasks', auth='public', type='json')
    def get_tasks(self, project_id=None, employee_id=None, **kw):
        _logger.info(f'Project ID: {project_id}')
        _logger.info(f'Employee ID: {employee_id}')
        
        # Fetch the user_id of the passed employee_id
        user_id = http.request.env['hr.employee'].sudo().search([('id', '=', employee_id)]).user_id.id     
        _logger.info(f'User ID: {user_id}')
        
        # Fetch the tasks of the passed project_id
        tasks = http.request.env['project.task'].sudo().search([('project_id.id', '=', project_id), ('user_ids', 'in', user_id)])
        _logger.info(f'Tasks: {tasks}')
        
        return tasks.read(['name', 'id'])
    
    
    # Version of manual selection New version that does actually check in or out
    @http.route('/hr_attendance/manual_selection_no_check_in_out', type="json", auth="public")
    def manual_selection_v2(self, token, employee_id, pin_code):
        company = self._get_company(token)
        if company:
            employee = request.env['hr.employee'].sudo().browse(employee_id)
            if employee.company_id == company and ((not company.attendance_kiosk_use_pin) or (employee.pin == pin_code)):
                return self._get_employee_info_response(employee)
        return {}
    



