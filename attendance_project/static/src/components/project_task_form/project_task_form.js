/** @odoo-module */
// Create OWL component to add new for project, task and description to record in the hr.attendance model
import {Component, useState} from "@odoo/owl";
import { Registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks"

const myRegistry = new Registry();

export class ProjectTaskForm extends Component {
    setup() {
        this.rpc = useService("rpc");
        this.state = useState({
            projects: "",
            selectedProject: "",
            tasks: "",
            selectedTask: "",
            description: "",
            enableDescription: false,
        });

        this.fetchProjects();

    }

    // Fetch the projects for the employee
    async fetchProjects() {
        const projects = await this.rpc(
            'get_projects',{employee_id: this.props.employeeData.id}
            
        );
        console.log(projects);
        this.state.projects = projects;
    }   
    
    // Fetch the tasks for the selected project
    async fetchTasks(p_id) {
        const tasks = await this.rpc(
            'get_tasks',{project_id: p_id, employee_id: this.props.employeeData.id}
        );
        console.log(tasks);
        this.state.tasks = tasks;
    }

    projectIdSelection(ev) {
        this.state.selectedProject = ev.target.value;
        if (this.state.selectedProject != "") {
            this.state.tasks = this.fetchTasks(this.state.selectedProject);
        }
        else {
            this.state.tasks = [];
            this.state.enableDescription = false;
        }
    }
    
    taskIdSelection(ev) {
        this.state.selectedTask = ev.target.value;
        if (this.state.selectedTask != "") {
            this.state.enableDescription = true;
        }
        else {
            this.state.enableDescription = false;
        }
    }

    descriptionInput(ev) {
        this.state.description = ev.target.value;
    }

    kioskReturn() {
        this.props.kioskReturn();
    }

    saveProjectTask() {

        this.env.kioskReturn(this.state.selectedProject, this.state.selectedTask, this.state.description);
    }

    async onlyCheckIn (employeeId, enteredPin) {
        try{
            console.log("Employer ID: ", employeeId, "Entered Pin: ", enteredPin)
            const result = await this.rpc('manual_selection', {
                'token': this.props.token,
                'employee_id': employeeId,
                'pin_code': enteredPin
            });
            if (result && result.attendance) {
                this.props.employeeData = result;
                // console.log('Logged Manual Selection', this.employeeData)
                this.switchDisplay('project');
            }
        }
        catch (err) {
            console.error('Error in onlyCheckIn:', err);
        }
    }
    // async addNewRecord() {
    //     const { project, task, description } = this.state;
    //     const { attendance } = this.env.services;
    //     await attendance.addNewRecord(project, task, description);
    //     this.state.project = "";
    //     this.state.task = "";
    //     this.state.description = "";
    // }

    async save(){
        this.props.nextStep(this.props.employeeData);
        // await this.onlyCheckIn(this.props.employeeData.id, false);
    }
}

ProjectTaskForm.template = "attendance_project.project_task_form"
ProjectTaskForm.props = {
    employeeData : {type: Object},
    kioskReturn: {type: Function},
    nextStep: {type: Function},
    token: {type: String},
}

myRegistry.category("components").add("ProjectTaskForm", ProjectTaskForm);

