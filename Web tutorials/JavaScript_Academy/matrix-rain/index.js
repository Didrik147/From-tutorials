const canvas = document.getElementById('Matrix')
const context = canvas.getContext('2d')


canvas.width = window.innerWidth
canvas.height = window.innerHeight


let katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン'
let latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
let nums = '0123456789'

let hiragana = 'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやいゆえよらりるれろわいうえをん'
let ukrainian = 'бвгґджзклмнпрстфхцчшщаеєиіїоуюя'
let greek = 'ΑαΒβΓγΔδΕεΖζΗηΘθΙιΚκΛλΜμΝνΞξΟοΠπΡρΣσςΤτΥυΦφΧχΨψΩω.'

let alphabet = katakana + latin + nums

alphabet += hiragana
alphabet += ukrainian
alphabet += greek

const fontSize = 16

// Calculate how many characters can fit on the screen horisontally
const columns = canvas.width/fontSize

const rainDrops = []

for(let x=0; x<columns; x++){
    rainDrops[x] = 1
}

const draw = () => {
    context.fillStyle = `rgba(0,0,0, 0.05)`;
    context.fillRect(0,0,canvas.width, canvas.height)

    context.fillStyle = '#0f0'
    context.font = fontSize + 'px monospace'

    for(let i=0; i<rainDrops.length; i++){
        const text = alphabet.charAt(Math.floor(Math.random()*alphabet.length))
        context.fillText(text, i*fontSize, rainDrops[i]*fontSize)

        if(rainDrops[i]*fontSize > canvas.height && Math.random() > 0.975){
            rainDrops[i] = 0;
        }
        rainDrops[i]++
    }
}

//setInterval(draw, 30)
setInterval(draw, 40)