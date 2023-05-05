
// Listen for auth status changes
auth.onAuthStateChanged(user => {
    //console.log(user)
    if (user){
        // Get data
        /*db.collection('guides').get().then(snapshot => {
            //console.log(snapshot.docs)
            setupGuides(snapshot.docs)
            setupUI(user)
        }).catch(err => {
            console.log(err.message)
        });
        */
       db.collection('guides').onSnapshot(snapshot => {
        setupGuides(snapshot.docs)
        setupUI(user)
       }, err => {
           console.log(err.message)
       })
    }else {
        setupUI()
        setupGuides([])
        //console.log('User logged out')
    }
})

// Create new guide
const createForm = document.querySelector("#create-form")
createForm.addEventListener('submit', (e) => {
    e.preventDefault();

    db.collection('guides').add({
        title: createForm['title'].value,
        content: createForm['content'].value
    }).then(() => {
        // Close the modal and reset form
        const modal = document.querySelector("#modal-create");
        M.Modal.getInstance(modal).close();
        createForm.reset();
    }).catch(err => {
        console.log(err.message)
    })
})



// Signup
const signupForm = document.querySelector("#signup-form");

signupForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get user info
    const email = signupForm['signup-email'].value
    const password = signupForm['signup-password'].value

    //console.log(email, password)

    // Sign up the user
    auth.createUserWithEmailAndPassword(email, password).then(cred => {
        return db.collection("users").doc(cred.user.uid).set({
            bio: signupForm['signup-bio'].value
        })
    }).then(() => {
        const modal = document.querySelector("#modal-signup");
        M.Modal.getInstance(modal).close();
        signupForm.reset();
    })
})


// Logout
const logout = document.querySelector("#logout")
logout.addEventListener('click', (e) => {
    e.preventDefault()
    /* auth.signOut().then(() => {
        //console.log("User signed out")
    }) */
    auth.signOut()
})


// Login
const loginForm = document.querySelector("#login-form")
loginForm.addEventListener("submit", (e) => {
    e.preventDefault() //prevents page from reloading

    // Get user info
    const email = loginForm['login-email'].value
    const password = loginForm['login-password'].value

    //console.log(email, password)

    // Sign up the user
    auth.signInWithEmailAndPassword(email, password).then(cred => {
        //console.log(cred.user)
        // Close the login modal and reset the form
        const modal = document.querySelector("#modal-login");
        M.Modal.getInstance(modal).close();
        loginForm.reset();
    })
})



