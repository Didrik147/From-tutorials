// object literals

/* const blogs = [
    { title: 'why mac & cheese rules', likes: 30 },
    { title: '10 things to make with marmite', likes: 50 }
];

console.log(blogs) */

let user = {
    name: 'crystal',
    age: 30,
    email: 'crystal@thenetninja.co.uk',
    location: 'berlin',
    //blogs: ['why mac & cheese rules', '10 things to make with marmite'],
    blogs: [
        { title: 'why mac & cheese rules', likes: 30 },
        { title: '10 things to make with marmite', likes: 50 }
    ],
    login: function(){
        console.log('the user logged in')
    },
    logout: function(){
        console.log('the user logged out')
    },
    logBlogs(){
        //console.log(this.blogs)
        console.log("This user has written the following blogs:")
        this.blogs.forEach(blog => {
            console.log(blog.title, blog.likes);
        })
    }
}

user.logBlogs()

//user.login()
//user.logout()

/*
console.log(user)
console.log(user.name)

user.age = 35

console.log(user.age)

const key = "location"
console.log(user[key]) //user['location']

console.log(user['email'])
user['name'] = 'chun-li';
console.log(user['name'])

console.log(typeof (user))
*/