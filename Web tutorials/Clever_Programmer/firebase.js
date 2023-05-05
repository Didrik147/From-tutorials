// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
var firebaseConfig = {
    apiKey: "AIzaSyCT3wd6LnU0OvI8tPHN-XkH_dFQbppFUIs",
    authDomain: "ninja-firestore-tut-9770b.firebaseapp.com",
    projectId: "ninja-firestore-tut-9770b",
    storageBucket: "ninja-firestore-tut-9770b.appspot.com",
    messagingSenderId: "874596700659",
    appId: "1:874596700659:web:e4870f6e469d1b57de4286",
    measurementId: "G-7E3HDB8WFG"
};
// Initialize Firebase
firebase.initializeApp(firebaseConfig);

const db = firebase.firestore();
db.settings({ timestampsInSnapshots: true });
