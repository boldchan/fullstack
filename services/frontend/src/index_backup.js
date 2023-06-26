import { styleBody, addTitle, addForm } from './dom';
import Handsontable from "handsontable";
//import 'handsontable/dist/handsontable.full.min.css';


import { data } from "./constants";
import { progressBarRenderer, starRenderer } from "./customRenderers";

import {
  alignHeaders,
  addClassesToRows,
  changeCheckboxCell
} from "./hooksCallbacks";

console.log('index file');

styleBody();
addTitle('Algo Input');

const example = document.getElementById("handsontable");
new Handsontable(example, {
    data,
    height: 450,
    colWidths: [140, 126, 192, 100, 100, 90, 90, 110, 97],
    colHeaders: [
      "Company name",
      "Country",
      "Name",
      "Sell date",
      "Order ID",
      "In stock",
      "Qty",
      "Progress",
      "Rating"
    ],
    columns: [
      { data: 1, type: "text" },
      { data: 2, type: "text" },
      { data: 3, type: "text" },
      {
        data: 4,
        type: "date",
        allowInvalid: false
      },
      { data: 5, type: "text" },
      {
        data: 6,
        type: "checkbox",
        className: "htCenter"
      },
      {
        data: 7,
        type: "numeric"
      },
      {
        data: 8,
        renderer: progressBarRenderer,
        readOnly: true,
        className: "htMiddle"
      },
      {
        data: 9,
        renderer: starRenderer,
        readOnly: true,
        className: "star htCenter"
      }
    ],
    dropdownMenu: true,
    hiddenColumns: {
      indicators: true
    },
    contextMenu: true,
    multiColumnSorting: true,
    filters: true,
    rowHeaders: true,
    manualRowMove: true,
    afterGetColHeader: alignHeaders,
    afterOnCellMouseDown: changeCheckboxCell,
    beforeRenderer: addClassesToRows,
    licenseKey: "non-commercial-and-evaluation"
  });

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