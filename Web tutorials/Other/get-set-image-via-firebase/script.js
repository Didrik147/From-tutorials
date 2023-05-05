import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";

const firebaseConfig = {
    apiKey: "AIzaSyCnMXmPMWYGB-1Cyjf9fGxCSdv255ikkYc",
    authDomain: "learning-147.firebaseapp.com",
    projectId: "learning-147",
    storageBucket: "learning-147.appspot.com",
    messagingSenderId: "367100846840",
    appId: "1:367100846840:web:1acbcf95ef4561638b910d",
    measurementId: "G-GGFNW71GS9"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

import { getStorage, ref as sRef, uploadBytesResumable, getDownloadURL } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-storage.js";

// Cloud Firestore Database
import { getFirestore, doc, getDoc, setDoc, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.6.10/firebase-firestore.js"
const clouddb = getFirestore();

// Variables & references
var files = [];
var reader = new FileReader();

var namebox = document.getElementById('namebox');
var extlab = document.getElementById('extlab');
var myimg = document.getElementById('myimg');
var proglab = document.getElementById('upprogress');
var selbtn = document.getElementById('selbtn');
var upbtn = document.getElementById('upbtn');
var downbtn = document.getElementById('downbtn');

var input = document.createElement('input');
input.type = 'file';

input.onchange = e => {
    files = e.target.files;

    var extention = GetFileExt(files[0]);
    var name = GetFileName(files[0]);

    namebox.value = name;
    extlab.innerHTML = extention;

    reader.readAsDataURL(files[0]);
}

reader.onload = function () {
    myimg.src = reader.result;
}

// Selection
selbtn.onclick = function () {
    input.click()
}

function GetFileExt(file) {
    var temp = file.name.split('.')
    var ext = temp.slice((temp.length - 1), (temp.length));
    return '.' + ext[0]
}

function GetFileName(file) {
    var temp = file.name.split('.')
    var fname = temp.slice(0, -1).join('.');
    return fname
}

// Upload process

async function UploadProcess() {
    var ImgToUpload = files[0];

    var ImgName = namebox.value + extlab.innerHTML

    const metaData = {
        contentType: ImgToUpload.type
    }

    const storage = getStorage()

    const storageRef = sRef(storage, "Images/" + ImgName)

    const UploadTask = uploadBytesResumable(storageRef, ImgToUpload, metaData)

    UploadTask.on('state-changed', (snapshot) => {
        var progress = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        proglab.innerHTML = "Upload " + progress + "%";
    },
        (error) => {
            alert("error: image not uploaded!")
        },
        () => {
            getDownloadURL(UploadTask.snapshot.ref).then((downloadURL) => {
                //console.log(downloadURL)
                SaveURLtoFirestore(downloadURL)
            })
        }
    )
}

// Functions for Firestore Database
async function SaveURLtoFirestore(url) {
    var name = namebox.value;
    var ext = extlab.innerHTML;

    var ref = doc(clouddb, "ImageLinks/" + name)

    await setDoc(ref, {
        ImageName: (name + ext),
        ImageURL: url
    })
}

async function GetImagefromFirestore() {
    var name = namebox.value;

    var ref = doc(clouddb, "ImageLinks/" + name)

    const docSnap = await getDoc(ref)

    if (docSnap.exists()) {
        myimg.src = docSnap.data().ImageURL;
    }
}


upbtn.onclick = UploadProcess
downbtn.onclick = GetImagefromFirestore;