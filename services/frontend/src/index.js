import { styleBody, addTitle, addForm } from './dom';

styleBody();
addTitle('Algo Input');

const project_schema = [
  {
    name: 'Project Name',
    type: 'text',
    placeholder: ''
  },
  {
    name: 'District',
    type: 'text',
    placeholder: ''
  },
  {
    name: 'Version',
    type: 'text',
    placeholder: '2022'
  }
];
  
document.getElementsByTagName("body")[0].appendChild(addForm('project_info', project_schema));