// Book Class: Represents a Book
class Book {
    constructor(title, author, isbn){
        this.title = title;
        this.author = author;
        this.isbn = isbn
    }
}

// UI Class: Handle UI Tasks
class UI {
    static displayBooks(){
        /* const StoredBooks = [
            {
                title: 'The Way of Kings',
                author: 'Brandon Sanderson',
                isbn: '9780765326355' 
            },
            {
                title: 'The Final Empire',
                author: 'Brandon Sanderson',
                isbn: '9780765311788'
            },
            {
                title: 'Super Powereds: Year 1',
                author: 'Drew Hayes',
                isbn: '9781495444289'
            }
        ]

        const books = StoredBooks */
        const books = Store.getBooks()

        books.forEach((book) => UI.addBookToList(book))
    }

    static addBookToList(book){
        const list = document.querySelector('#book-list')

        const row = document.createElement('tr')

        row.innerHTML = `
            <td>${book.title}</td>
            <td>${book.author}</td>
            <td>${book.isbn}</td>
            <td><a href="#" class="btn btn-danger btn-sm delete">X</a></td>
        `
        list.appendChild(row)
    }

    static deleteBook(el){
        if(el.classList.contains('delete')){
            el.parentElement.parentElement.remove();

            // Show success message
            UI.showAlert("Book Removed", "success")
        }
    }

    static showAlert(message, className){
        const div = document.createElement('div')
        div.className = `alert alert-${className}`
        div.appendChild(document.createTextNode(message))
        const container = document.querySelector('.container')
        const form = document.querySelector('#book-form')
        container.insertBefore(div, form)

        // Vanish in 3 seconds
        setTimeout(() => document.querySelector(".alert").remove(), 3000)
    }

    static clearFields(){
        document.querySelector('#title').value = ''
        document.querySelector('#author').value = ''
        document.querySelector('#isbn').value = ''
    }
}


// Store Class: Handles Storage
class Store {
    // Making the functions static, so we can call then without having to instanciate the Store class
    static getBooks() {
        let books;
        if(localStorage.getItem('books') === null){
            books = [];
        }else {
            books = JSON.parse(localStorage.getItem('books'))
        }

        return books
    }

    static addBook(book){
        const books = Store.getBooks()

        books.push(book)

        localStorage.setItem('books', JSON.stringify(books))
    }

    static removeBook(isbn){
        const books = Store.getBooks()

        books.forEach((book, index) => {
            if(book.isbn == isbn){
                books.splice(index, 1)
            }
        })

        localStorage.setItem('books', JSON.stringify(books))
    }
}


// Event: Display Books
document.addEventListener('DOMContentLoaded', UI.displayBooks)

// Event: Add a Book
document.querySelector('#book-form').addEventListener('submit', (e) => {
    // Prevent actual submit
    e.preventDefault()

    // Get form values
    const title = document.querySelector('#title').value
    const author = document.querySelector('#author').value
    const isbn = document.querySelector('#isbn').value

    // Validate
    if(title === '' || author === '' || isbn == ''){
        //alert('Please fill in all fields')
        UI.showAlert('Please fill in all fields', 'danger')
    }else {
        // Instatiate book
        const book = new Book(title, author, isbn);

        // Add Book to UI
        UI.addBookToList(book)

        // Add book to store
        Store.addBook(book)

        // Show success message
        UI.showAlert("Book Added", "success")

        // Clear fields
        UI.clearFields();
    }
})

// Event: Remove a Book
// event propagation
document.querySelector("#book-list").addEventListener('click', (e) => {
    UI.deleteBook(e.target)

    // Remove book from store
    Store.removeBook(e.target.parentElement.previousElementSibling.textContent)
})