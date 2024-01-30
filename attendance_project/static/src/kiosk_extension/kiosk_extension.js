/** @odoo-module */
import { patch } from '@web/core/utils/patch';
import kioskModule from '@hr_attendance/public_kiosk/public_kiosk_app';

const kioskAttendanceApp = kioskModule.kioskAttendanceApp;

console.log('Patching Kiosk Attendance App')
patch(kioskAttendanceApp.prototype, {
    onManualSelection: async function(employeeId, enteredPin) {
        try{
            console.log('Patched function onManualSelection')
            const result = await this.rpc('manual_selection', {
                'token': this.props.token,
                'employee_id': employeeId,
                'pin_code': enteredPin
            });
            if (result && result.attendance) {
                this.employeeData = result;
                console.log('Logged Manual Selection')
                this.switchDisplay('project');
            } else {
                if (enteredPin) {
                    this.displayNotification(_t("Wrong Pin"));
                }
            }
        }
        catch(err){
            console.error('Error in onManualSelection:', err);
        }
    }, 

    async kioskConfirm(employeeId){
        console.log('Patched function kioskConfirm')
        const employee = await this.rpc('attendance_employee_data',
            {
                'token': this.props.token,
                'employee_id': employeeId
            })
        if (employee && employee.employee_name){
            if (employee.use_pin){
                this.employeeData = employee
                this.switchDisplay('pin')
            }else{
                await this.onManualSelection(employeeId, false)
            }
        }
    },

    switchDisplay(screen) {
        console.log('Patched function switchDisplay')
        const displays = ["main", "greet", "manual", "pin", "project"]
        if (displays.includes(screen)){
            this.state.active_display = screen;
        }else{
            this.state.active_display = "main";
        }
    }
});

export { kioskAttendanceApp };
