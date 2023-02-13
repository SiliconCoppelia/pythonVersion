function submit_form(){
    var formData = new FormData(document.forms.userInput)
    var user_msg= formData.get('user-input')
    print_user_response(user_msg)
    document.forms.userInput.submit()
    // const response = fetch('/request', user_msg);
    print_sys_response(get_sys_response(user_msg))
  }

const callAPI = async (nameStr, genderStr, age, aff, eth) => {
    console.log(nameStr);
    console.log(age);
    console.log(aff);
    console.log(eth);
    
    let body = {
        'name' : nameStr,
        'gender': genderStr,
        'age' : age,
        'aff' : aff,
        'eth' : eth,
    };

    jsonFile=JSON.stringify(body);
    let options = {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json',
        }
    }
    console.log(options);
    const response = await fetch('/submit', options);
    const myJson = await response.json(); 
    return (myJson);
}

// $.fn.serializeObject = function()  {  
//    var o = {};  
//    var a = this.serializeArray();  
//    $.each(a, function() {  
//        if (o[this.name]) {  
//            if (!o[this.name].push) {  
//                o[this.name] = [o[this.name]];  
//            }  
//            o[this.name].push(this.value || '');  
//        } else {  
//            o[this.name] = this.value || '';  
//        }  
//    });  
//    return o;  
// };
function formToJSON(form){
  jsonResult = callAPI(form);
}

// let questionForm = document.getElementById("choices");

// questionForm.addEventListener("submit", (e) => {
//   e.preventDefault();

//   let username = document.getElementById("user-name-input");
// //   let password = document.getElementById("password");

// console.log(
//       `This form has a username of ${username.value} and password of ${password.value}`
//     );

//     username.value = "";

//   });