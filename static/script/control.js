function proc() {
    let get_element = document.getElementById('gift_table');
    for (let i = 0; i < get_element.rows.length; i++) {
        for (let j = 0; j < get_element.rows[i].cells.length; j++) {
            if (get_element.rows[i].cells[j].childNodes[0].checked == true) {
                let name = get_element.rows[i].childNodes[3].innerText;
                let fr = document.createElement("form");
                fr.method = "POST";
                fr.action = '/remove_gift';
                let newInput1 = document.createElement("input");
                newInput1.type = "hidden";
                newInput1.id = "000202";
                newInput1.name = "000202";
                newInput1.value = name;
                fr.appendChild(newInput1);
                document.getElementById("hide_form_holder").appendChild(fr);
                fr.submit();
            } else {
                alert("Please select an Item to delete")
            }
        }
    }
}

function buy_gift(item_array) {

    let json_value = {
        'id': item_array[0],
        'name': item_array[1],
        'brand': item_array[2],
        'price': item_array[3],
        'in_stock_quantity': item_array[4]
    };
    let json_obj = JSON.stringify(json_value);
    let xhr = new XMLHttpRequest();
    xhr.open('POST', '/gift_to_buy', true);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(json_obj);
}