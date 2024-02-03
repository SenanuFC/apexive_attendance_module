/** @odoo-module */
import { patch } from '@web/core/utils/patch';
import kioskModule from '@hr_attendance/public_kiosk/public_kiosk_app';
import { ProjectTaskForm } from '@attendance_project/components/project_task_form/project_task_form';
import { useService } from "@web/core/utils/hooks";

const kioskAttendanceApp = kioskModule.kioskAttendanceApp;

console.log('Patching Kiosk Attendance App')
console.log(kioskAttendanceApp.prototype.setup);
patch(kioskAttendanceApp.prototype, {
    setup() {
        super.setup();
        this.constructor.components.ProjectTaskForm = ProjectTaskForm;
    },

    onManualSelection: async function (employeeId, enteredPin) {
        try {
            // console.log('Patched function onManualSelection')
            const result = await this.rpc('manual_selection_no_check_in_out', {
                'token': this.props.token,
                'employee_id': employeeId,
                'pin_code': enteredPin
            });
            if (result && result.attendance) {
                this.employeeData = result;
                // console.log('Logged Manual Selection', this.employeeData)
                this.switchDisplay('project');
            } else {
                if (enteredPin) {
                    this.displayNotification(_t("Wrong Pin"));
                }
            }
        }
        catch (err) {
            console.error('Error in onManualSelection:', err);
        }
    },

    async onlyCheckIn (employeeId, enteredPin) {
        try{
            console.log("Employer ID: ", employeeId, "Entered Pin: ", enteredPin)
            const result = await this.rpc('manual_selection', {
                'token': this.props.token,
                'employee_id': employeeId,
                'pin_code': enteredPin
            });
            if (result && result.attendance) {
                this.employeeData = result;
                // console.log('Logged Manual Selection', this.employeeData)
                this.switchDisplay('project');
            }
        }
        catch (err) {
            console.error('Error in onlyCheckIn:', err);
        }
    },

    async kioskConfirm(employeeId) {
        // console.log('Patched function kioskConfirm')
        const employee = await this.rpc('attendance_employee_data',
            {
                'token': this.props.token,
                'employee_id': employeeId
            })
        if (employee && employee.employee_name) {
            if (employee.use_pin) {
                this.employeeData = employee
                this.switchDisplay('pin')
            } else {
                await this.onManualSelection(employeeId, false)
            }
        }
    },

    switchDisplay(screen) {
        // console.log('Patched function switchDisplay')
        const displays = ["main", "greet", "manual", "pin", "project"]
        if (displays.includes(screen)) {
            this.state.active_display = screen;
        } else {
            this.state.active_display = "main";
        }
    },

    async nextStep(employeeData) {
        await this.onlyCheckIn(employeeData.id, false);
        await this.switchDisplay('greet');
    }
});

export { kioskAttendanceApp };
