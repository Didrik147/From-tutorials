const poke_container = document.getElementById('poke-container')

//add missing types? (e.g. steel, dark and ghost) 
// color of two types? Combination, gradient or half-half?

/*
const colors = {
    fire: '#FDDFDF',
    grass: '#DEFDE0',
	electric: '#FCF7DE',
	water: '#DEF3FD',
	ground: '#f4e7da',
	rock: '#d5d5d4',
	fairy: '#fceaff',
	poison: '#98d7a5',
	bug: '#f8d5a3',
	dragon: '#97b3e6',
	psychic: '#eaeda1',
	flying: '#F5F5F5',
	fighting: '#E6E0D4',
	normal: '#F5F5F5'
}
*/

const colors = {
    normal: "#A8A77A",
    fire: "#EE8130",
    water: "#6390F0",
    electric: "#F7D02C",
    grass: "#7AC74C",
    ice: "#96D9D6",
    fighting:  "#C22E28",
    poison:  "#A33EA1",
    ground:  "#E2BF65",
    flying:  "#A98FF3",
    psychic:  "#F95587",
    bug:  "#A6B91A",
    rock:  "#B6A136",
    ghost:  "#735797",
    dragon:  "#6F35FC",
    dark:  "#705746",
    steel:  "#B7B7CE",
    fairy:  "#D685AD"
}


const main_types = Object.keys(colors)
//console.log(main_types)



/*
const pokemon_count = 150

const fetchPokemons = async () => {
    for(let i = 1; i <= pokemon_count; i++) {
        await getPokemon(i)
    }
}
*/


// Tried to make a new one, but I do not think it is better
function fetchPokemons_new(){
    //One Pokemon
    let url = `https://pokeapi.co/api/v2/pokemon/${pokemon_start}`
    
    // Many Pokemons 
    /* This does not seem faster. This is because it seems I only get the name, and still has to make a new API request to get the id, types etc. */
    //let url = `https://pokeapi.co/api/v2/pokemon?limit=${pokemon_count}&offset=${pokemon_start - 1}`

    fetch(url)
        .then(res => res.json())
        .then(pokemon => {
            console.log(pokemon.name)
        })
}


const fetchPokemons = async (pokemon_start, pokemon_count) => {
    for(let i = pokemon_start; i < pokemon_start+pokemon_count; i++) {
        await getPokemon(i)
    }
}



// Can be optimized by getting multiple pokemons for each request
// TODO: Try to do this
const getPokemon = async (id) => {
    //const url = `https://pokeapi.co/api/v2/pokemon/${id}`
    
    // From locally saved file (to avoid too many API requests)
    const url = `pokemon_data/data/${id}.json`
    const res = await fetch(url)
    const data = await res.json()
    //console.log(data)

    createPokemonCard(data)
}

const createPokemonCard = (pokemon) => {
    const pokemonEl = document.createElement('div')
    pokemonEl.classList.add('pokemon')

    // Get name. Make first letter uppercase
    const name = pokemon.name[0].toUpperCase() + pokemon.name.slice(1);

    // Get ID. Add leading zeros
    const id = pokemon.id.toString().padStart(3, '0')

    // Get both types for pokemons with 2 types?
    //console.log(pokemon.types)
    const poke_types = pokemon.types.map(type => type.type.name)
    //console.log(poke_types)
    let type = main_types.find(type => poke_types.indexOf(type) > -1)
    //console.log(type)

    let alpha = "99"

    //let color = colors[type]
    let color = `${colors[type]}${alpha}`
    //console.log(color)

    pokemonEl.style.backgroundColor = color;

    let type2, color2;
    let typetext = type;
    

    if (poke_types.length == 2){
        type = poke_types[0]
        type2 = poke_types[1]
        color = `${colors[type]}${alpha}`
        color2 = `${colors[type2]}${alpha}`

        pokemonEl.style.background = `linear-gradient(90deg, ${color}, ${color2})`;
        
        
        
        typetext = `${type}, ${type2}`;
    }

    //console.log(type, type2)


    /*
    const pokemonInnerHTML = `
        <div class="img-container">
            <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${pokemon.id}.png" alt="">
        </div>
        <div class="info">
            <span class="number">#${id}</span>
            <h3 class="name">${name}</h3>
            <small class="type">Type: <span>${type}</span></small>
        </div>
    `
    */
    
    const pokemonInnerHTML = `
        <div class="img-container">
            <img src="./pokemon_data/images/${pokemon.id}.png" alt="">
        </div>
        <div class="info">
            <span class="number">#${id}</span>
            <h3 class="name">${name}</h3>
            <small class="type">Type: <span>${typetext}</span></small>
        </div>
    `

    pokemonEl.innerHTML = pokemonInnerHTML

    poke_container.appendChild(pokemonEl)
}


let pokemon_start
let pokemon_count

let region;

//region = "Kanto" /* Red & Blue, gen 1 */
//region = "Johto" /* Gold & Silver, gen 2 */
region = "Hoenn" /* Ruby & Sapphire, gen 3 */
//region = "Sinnoh" /* Diamond & Pearl, gen 4 */

if (region == "Kanto"){
    pokemon_start = 1
    pokemon_count = 151
}else if(region == "Johto"){
    pokemon_start = 152
    pokemon_count = 251
}else if (region == "Hoenn"){
    pokemon_start = 252
    pokemon_count = 135
}else if (region == "Sinnoh"){
    pokemon_start = 387
    pokemon_count = 107
}else {
    pokemon_start = 1
    pokemon_count = 18
}

fetchPokemons(pokemon_start, pokemon_count)