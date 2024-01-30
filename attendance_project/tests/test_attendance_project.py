
import time

from odoo.tests.common import tagged, TransactionCase


@tagged('attendance_project')
class TestAttendanceProject(TransactionCase):
    """Tests for attendance date ranges validity"""

    @classmethod
    def setUpClass(cls):
        super(TestAttendanceProject, cls).setUpClass()
        cls.attendance = cls.env['hr.attendance']
        cls.test_employee = cls.env['hr.employee'].create({'name': "Jacky"})
        cls.project = cls.env['project.project'].create({'name': "Project 1"})
        cls.project_task = cls.env['project.task'].create({'name': "Task 1",
                                                           'project_id': cls.project.id})
        # demo data contains set up for cls.test_employee
        cls.open_attendance = cls.attendance.create({
            'employee_id': cls.test_employee.id,
            'check_in': time.strftime('%Y-%m-10 10:00'),
            'project_id': cls.project.id,
            'task_id': cls.project_task.id
        })

    def test_attendance_without_project(self):
        # Make sure check_out is before check_in
        with self.assertRaises(Exception):
            self.my_attend = self.attendance.create({
                'employee_id': self.test_employee.id,
                'check_in': time.strftime('%Y-%m-10 08:00'),
                'check_out': time.strftime('%Y-%m-10 11:00'),
            })
