from odoo import models, fields, api, exceptions, _


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'
    
    # overwrite function _attendance_action_change
    def _attendance_action_change(self, geo_information=None, project_id=None, task_id=None, activity_description=None):
        """ Check In/Check Out action
            Check In: create a new attendance record
            Check Out: modify check_out field of appropriate attendance record
        """
        self.ensure_one()
        action_date = fields.Datetime.now()

        if self.attendance_state != 'checked_in':
            if geo_information:
                vals = {
                    'employee_id': self.id,
                    'check_in': action_date,
                    **{'in_%s' % key: geo_information[key] for key in geo_information}
                }
            else:
                vals = {
                    'employee_id': self.id,
                    'check_in': action_date,
                }
            return self.env['hr.attendance'].create(vals)
        attendance = self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_out', '=', False)], limit=1)
        if attendance:
            if geo_information:
                attendance.write({
                    'check_out': action_date,
                    'project_id': project_id,
                    'task_id': task_id,
                    'activity_description': activity_description,
                    **{'out_%s' % key: geo_information[key] for key in geo_information}
                })
            else:
                attendance.write({
                    'project_id': project_id,
                    'task_id': task_id,
                    'activity_description': activity_description,
                    'check_out': action_date
                })
        else:
            raise exceptions.UserError(_(
                'Cannot perform check out on %(empl_name)s, could not find corresponding check in. '
                'Your attendances have probably been modified manually by human resources.',
                empl_name=self.sudo().name))
        return attendance

    
