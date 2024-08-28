// password hide or show for login and register pages

let password = document.getElementById('password');
let icon = document.querySelector('i')
function showPassword() {
    if (password.type === 'password') {
        password.type = 'text'
        icon.classList.remove('fa-eye-slash')
        icon.classList.add('fa-eye')
    } else {
        password.type = 'password'
        icon.classList.remove('fa-eye')
        icon.classList.add('fa-eye-slash')
    }
}


// Registration Validation

// Form Validation

//document.addEventListener('DOMContentLoaded', () => {
//    let form = document.querySelector('form');
//    let name = document.getElementById('name');
//    let email = document.getElementById('email');
//    let tel = document.getElementById('tel');
//    let username = document.getElementById('username')
//    let password = document.getElementById('password');
//
//    // messages
//
//    let emailQuote = document.getElementById('emailquote')
//    let telQuote = document.getElementById('telquote')
//    let passwordQuote = document.getElementById('passwordquote')
//    let success = document.getElementById('popup')
//
//    form.addEventListener('submit', (e) => {
//        e.preventDefault();
//
//        if(!validateEmail(email.value)){
//            emailQuote.style.display='block';
//            setTimeout(() => {
//                emailQuote.style.display = 'none';
//            }, 6000);
//        }else if(!validatePhone(tel.value)){
//            telQuote.style.display='block';
//            setTimeout(() => {
//                telQuote.style.display = 'none';
//            }, 6000);
//        }else if(!validatePassword(password.value)){
//            passwordQuote.style.display = 'block';
//            setTimeout(() => {
//                passwordQuote.style.display = 'none';
//            }, 6000);
//        }else{
//            success.style.display = 'block';
//            setTimeout(() => {
//                success.style.display = 'none';
//            }, 3000);
//        }
//    })
//
//
//    let validateEmail = (email) =>{
//        const register = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
//        return register.test(email)
//    }
//
//    let validatePhone = (tel) => {
//        const register = /^[0-9]{10,15}$/;
//        return register.test(tel)
//    }
//
//    let validatePassword = (password) =>{
//        const register = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
//        return register.test(password)
//    }
//
//})


// Calculate the price in vendor quotation

function calculate(){
    let landArea = document.getElementById('land-area').value;
    let floor = document.getElementById('floors').value;
    let cement = document.getElementById('cement').value;
    let sand = document.getElementById('sand').value;
    let stone = document.getElementById('stone').value;
    let brick = document.getElementById('brick').value;
    let steel = document.getElementById('steel').value;
    let paint = document.getElementById('paint').value;
    let estimation = document.getElementById('estimation');

    let cement_cost = (cement * (landArea/1000))* floor
    let sand_cost = (sand * (landArea/1000))* floor
    let stone_cost = (stone * (landArea/1000))* floor
    let brick_cost = (brick * (landArea/1000))* floor
    let steel_cost = (steel * (landArea/1000))* floor
    let paint_cost = (paint * (landArea/1000))* floor

    let total_estimation = cement_cost + sand_cost + stone_cost + brick_cost + steel_cost + paint_cost

// It will show the result on input field
    estimation.value = total_estimation.toFixed(2);

}


// Calculating the cost in manager update page

function calculateQuotation(){
    let vendor_quote = parseFloat(document.getElementById('vendor_quote').value);
    let other_cost = parseFloat(document.getElementById('other-cost').value);
    let manager_quotation = document.getElementById('manager-quotation');

    let total_cost = vendor_quote + other_cost;

    manager_quotation.value = total_cost.toFixed(2);
}


// Profit Calculation

function profit_calculation(){
    let final_quote = parseFloat(document.getElementById('final_quote').value);
    let actual_quote = parseFloat(document.getElementById('actual_quote').value);
    let profit_quotation = document.getElementById('profit-quotation');

    let profit_cost = final_quote - actual_quote;

    profit_quotation.value = profit_cost.toFixed(2);
}








