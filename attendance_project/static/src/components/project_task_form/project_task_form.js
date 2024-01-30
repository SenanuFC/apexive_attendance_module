/** @odoo-module */
// Create OWL component to add new for project, task and description to record in the hr.attendance model
import {Component} from "@odoo/owl";
import { Registry } from "@web/core/registry";

const myRegistry = new Registry();

export class ProjectTaskForm extends Component {
    
    setup() {
        this.state = useState({
            project: "",
            task: "",
            description: "",
        });
    }

    async addNewRecord() {
        const { project, task, description } = this.state;
        const { attendance } = this.env.services;
        await attendance.addNewRecord(project, task, description);
        this.state.project = "";
        this.state.task = "";
        this.state.description = "";
    }
}

ProjectTaskForm.template = "attendance_project.project_task_form"

myRegistry.category("components").add("ProjectTaskForm", ProjectTaskForm);

