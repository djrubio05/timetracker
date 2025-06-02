document.addEventListener('DOMContentLoaded', () => {
    const inputUsername = document.querySelector('input[name="username"]');
    if (inputUsername) {
        inputUsername.setAttribute('placeholder', 'Username');
    } else {
        console.log('Username input not found');
    }

    const inputPassword = document.querySelector('input[name="password"]');
    if (inputPassword) {
        inputPassword.setAttribute('placeholder', 'Password');
    } else {
    }
    
    const inputCreateUsername = document.querySelector('input[id="id_username"]');
    if (inputCreateUsername) {
        inputCreateUsername.setAttribute('placeholder', 'Username');
    } else {
    }


    const inputCreatePassword1 = document.querySelector('input[id="id_password1"]');
    if (inputCreatePassword1) {
        inputCreatePassword1.setAttribute('placeholder', 'Password');
    } else {
    }
    
    const inputCreatePassword2 = document.querySelector('input[id="id_password2"]');
    if (inputCreatePassword2) {
        inputCreatePassword2.setAttribute('placeholder', 'Confirm Password');
    } else {
    }
});


