// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyD-O-1LLUqelLVSuAeMdUUfTHycjy7yuG0",
    authDomain: "tutorial-9a792.firebaseapp.com",
    databaseURL: "https://tutorial-9a792-default-rtdb.europe-west1.firebasedatabase.app",
    projectId: "tutorial-9a792",
    storageBucket: "tutorial-9a792.appspot.com",
    messagingSenderId: "1010822825404",
    appId: "1:1010822825404:web:ec27a4714347c8710c57b9",
    measurementId: "G-T96Z9LJ2W6"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const database = firebase.database()

const contactFormEl = document.getElementById('contactForm')
const alertEl = document.querySelector(".alert")

// Reference messages collection
var messagesRef = database.ref('messages')


// Listen for form submit
contactFormEl.addEventListener('submit', submitForm);

// Submit form
function submitForm(e){
    e.preventDefault();

    // Get values
    var name = getInputVal('name')
    var company = getInputVal('company')
    var email = getInputVal('email')
    var phone = getInputVal('phone')
    var message = getInputVal('message')

    // Save message
    saveMessage(name, company, email, phone, message)

    // Show alert
    alertEl.style.display = "block"

    // Hide alert after 3 seconds
    setTimeout(function(){
        alertEl.style.display = "none"
    }, 3000)

    contactFormEl.reset();
}

// Function to get form values
function getInputVal(id){
    return document.getElementById(id).value
}

// Save message to firebase
function saveMessage(name, company, email, phone, message){
    var newMessageRef = messagesRef.push();
    newMessageRef.set({
        name: name,
        company: company,
        email: email,
        phone: phone,
        message: message
    })
}