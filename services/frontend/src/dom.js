console.log('dom file');

const body = document.querySelector('body');

export const styleBody = () => {
    body.style.background = 'peachpuff';
}

export const addTitle = (text) => {
    const title = document.createElement('h1');
    title.textContent = text;
    body.appendChild(title);
}

export const addForm = (form_id, fields) => {
    console.log(fields)
    const form = document.createElement("form");
    form.setAttribute("method", "post");
    form.setAttribute("action", "submit.php");
    const form_list = document.createElement("ul");
    form_list.setAttribute('id', form_id);
    fields.forEach(field => {
        console.log(field)
        const list_item = document.createElement('li');
        const label = document.createElement("label");
        label.setAttribute('for', field['name']);
        label.innerHTML = field['name']
        list_item.appendChild(label)
        
        const FN = document.createElement("input");
        FN.setAttribute("type", field['type']);
        FN.setAttribute("name", field['name']);
        FN.setAttribute("placeholder", field['placeholder']);
        FN.setAttribute("id", field["name"]);
        list_item.appendChild(FN)
        form_list.appendChild(list_item)
    })

    form.appendChild(form_list)

    const s = document.createElement("input");
    s.setAttribute("type", "submit");
    s.setAttribute("value", "Submit");

    form.appendChild(s)

    form.addEventListener("submit", (event) => {
        event.preventDefault();
        sendData();
      });
      
    return form
}




