function addItem(event) {
    event.preventDefault();
    let text = document.getElementById("todo-input");

    console.log(text);

    db.collection("todo-items").add({
        text: text.value,
        status: "active"
    })

    text.value = "";

}


function getItems() {
    db.collection("todo-items").onSnapshot((snapshot) => {
        //console.log(snapshot);
        let items = [];
        snapshot.docs.forEach((doc) => {
            items.push({
                id: doc.id,
                ...doc.data()
            })
        })
        generateItems(items);
    })
}

function generateItems(items) {
    let itemsHTML = "";

    items.forEach((item) => {
        
        itemsHTML += `
            <div class="todo-item">
                <div class="check">
                    <div data-id="${item.id}" class="check-mark ${item.status == "completed" ? "checked": ""}">
                        <img src="./assets/icon-check.svg">
                    </div>
                </div>
                <div class="todo-text ${item.status == "completed" ? "checked": ""}">
                    ${item.text}
                </div>
            </div>
        `
    })

    document.querySelector(".todo-items").innerHTML = itemsHTML;
    createEventListeners();
}

function createEventListeners(){
    let todoCheckMarks = document.querySelectorAll(".todo-item .check-mark");
    todoCheckMarks.forEach((checkMark)=>{
        checkMark.addEventListener("click", function(){
            markCompleted(checkMark.dataset.id);
        })
    })
}

function markCompleted(id){
    //console.log(id);
    //console.log("Mark completed");
    // From a database
    let item = db.collection("todo-items").doc(id);
    
    item.get().then(function(doc){
        if(doc.exists){
            //console.log('Here is the doc', doc.data());
            let status = doc.data().status;

            if(status == "active"){
                item.update({
                    status: "completed"
                })
                
            } else if (status == "completed"){
                item.update({
                    status: "active"
                })
            }
        }
    })
}


getItems();