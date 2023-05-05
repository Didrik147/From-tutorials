/* Made from the following tutorial: 
https://www.youtube.com/watch?v=ZniVgo8U7ek */

const cards = document.querySelectorAll('.memory-card')

let hasFlippedCard = false
let lockBoard = false;
let firstCard, secondCard

function flipCard(){
    if(lockBoard) return
    if (this === firstCard) return

    //console.log("I was clicked")
    //console.log(this)
    this.classList.toggle('flip')

    if(!hasFlippedCard){
        // first click
        hasFlippedCard = true
        firstCard = this

        return

        //console.log(hasFlippedCard, firstCard)
    }
    // second click
    secondCard = this

    checkForMatch();
    /*
    //console.log(firstCard, secondCard)
    
    // do cards match?
    if(firstCard.dataset.framework === secondCard.dataset.framework){
        // It's a match!!
        disableCards()
    }else {
        // Not a match
        unflipCards();
    }
    //console.log("Function was executed!")
    */
}

function checkForMatch(){
    let isMatch = (firstCard.dataset.framework === secondCard.dataset.framework)

    isMatch ? disableCards() : unflipCards();
}

function disableCards(){
    firstCard.removeEventListener('click', flipCard)
    secondCard.removeEventListener('click', flipCard)

    resetBoard();
}

function unflipCards(){
    lockBoard = true

    setTimeout(() => {
        firstCard.classList.remove('flip')
        secondCard.classList.remove('flip')

        resetBoard();
    }, 1500)
}

function resetBoard(){
    [hasFlippedCard, lockBoard] = [false, false]
    [firstCard, secondCard] = [null, null]
}

(function shuffle() {
    cards.forEach(card => {
        let randomPos = Math.floor(Math.random() * 12)
        card.style.order = randomPos
    })
})()



cards.forEach(card => card.addEventListener('click', flipCard))