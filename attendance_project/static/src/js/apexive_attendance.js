odoo.define([
    "attendance_project.AttendanceGreetings",
    
], function(require, factory) {
    'use strict';
    const KioskGreetings = require("hr_attendance.KioskGreetings")

    class AttendanceGreetings extends KioskGreetings{

    }
    
    AttendanceGreetings.template = "attendance_project.public_kiosk_greetings";

    return AttendanceGreetings;
    
});