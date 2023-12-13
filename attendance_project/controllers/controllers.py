# -*- coding: utf-8 -*-
# from odoo import http


# class AttendanceProject(http.Controller):
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

