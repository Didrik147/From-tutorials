const firebaseConfig = {
    apiKey: "AIzaSyBNg4iowN0vaGUOQm8wOJnmqWswrVqzEuc",
    authDomain: "blokkd.firebaseapp.com",
    projectId: "blokkd",
    storageBucket: "blokkd.appspot.com",
    messagingSenderId: "777073264345",
    appId: "1:777073264345:web:b764cac5bd8c66f4d6a0c8",
    databaseURL: "https://blokkd-default-rtdb.europe-west1.firebasedatabase.app"
};

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const auth = firebase.auth()
const database = firebase.database()

// Set up out register function
function register() {
    // Get all our input fields
    email = document.getElementById("email").value
    password = document.getElementById('password').value
    full_name = document.getElementById('full_name').value
    favourite_song = document.getElementById('favourite_song').value
    milk_before_cereal = document.getElementById('milk_before_cereal').value

    // Validate input fields
    if (!validate_email(email) || !validate_password(password)) {
        alert("Email or Password is Outta Line!!") //gangsta
        return // Don't continue running the code
    }

    if (!validate_field(full_name) || !validate_field(favourite_song) || !validate_field(milk_before_cereal)) {
        console.log("Email? ", validate_field(full_name))
        console.log("Favourite song? ", validate_field(favourite_song))
        console.log("Milk before cereal?", validate_field(milk_before_cereal))
        alert("One or More Extra Fields is Outta Line!!") //gangsta
        return // Don't continue running the code
    }

    // Move on with Auth
    auth.createUserWithEmailAndPassword(email, password)
        .then(function () {
            // Declare user variable
            let user = auth.currentUser

            // Add this user to Firebase Database
            let database_ref = database.ref()

            // Create user data
            let user_data = {
                email: email,
                full_name: full_name,
                favourite_song: favourite_song,
                milk_before_cereal: milk_before_cereal,
                last_login: Date.now()
            }

            // Push to Firebase Database
            database_ref.child("users/" + user.uid).set(user_data)

            // Done
            alert("User Created!!")


        })
        .catch(function (error) {
            // Firebase will use this to alert of its errors
            let error_code = error.code
            let error_message = error.message

            alert(error_message)
        })

}

// Set up our login function
function login() {
    // Get all our input fields
    email = document.getElementById("email").value
    password = document.getElementById("password").value

    // Validate input fields
    if (!validate_email(email) || !validate_password(password)) {
        alert("Email or Password is Outta Line!!")
        return
    }

    auth.signInWithEmailAndPassword(email, password)
    .then(function () {
        // Declare user variable
        let user = auth.currentUser

        // Add this user to Firebase Database
        let database_ref = database.ref()

        // Create user data
        let user_data = {
            last_login: Date.now()
        }

        // Push to Firebase Database
        database_ref.child("users/" + user.uid).update(user_data)

        // Done
        alert("User Logged in!!")
    })
        .catch(function(error) {
            // Firebase will use this to alert of its errors
            let error_code = error.code
            let error_message = error.message

            alert(error_message)
        })

}


// Validate Functions
function validate_email(email) {
    expression = /^[^@]+@\w+(\.\w+)+\w$/;
    if (expression.test(email)) {
        // Email is good
        return true
    } else {
        // Email is not good
        return false
    }
}

function validate_password(password) {
    // Firebase only accepts lengths greater than 6
    /* if (password < 6){
        return false
    }else {
        return true
    } */

    // One line LETS GO
    return (password < 6) ? false : true
}


function validate_field(field) {
    if (field == null) {
        return false
    }

    if (field.length <= 0) {
        return false
    } else {
        return true
    }
}