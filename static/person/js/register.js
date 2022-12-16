let form = document.querySelector("#id_form_register_person")

let first_name_field = form.querySelector("[name='first_name']")
let last_name_field = form.querySelector("[name='last_name']")

const URL_API = "https://randomuser.me/api/"

first_name_field_value = first_name_field.getAttribute('value')
last_name_field_value = last_name_field.getAttribute('value')

if (first_name_field_value == null || last_name_field_value == null){
    set_first_name_and_last_name_fields()
}

function set_first_name_and_last_name_fields(){
    fetch(URL_API).then((response) => {
        if (response.ok) {
        return response.json();
        }
        throw new Error('Erro ao acessar api');
    })
    .then((response_json) => {
        data_api = response_json.results[0]
        if (first_name_field_value == null){
            first_name_field.setAttribute('value', data_api.name.first)
        }
        if (last_name_field_value == null){
            last_name_field.setAttribute('value', data_api.name.last)
        }
    })
    .catch((error) => {
        console.log(error)
    });
}