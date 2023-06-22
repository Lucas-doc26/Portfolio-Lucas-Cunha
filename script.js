class animacao_texto {
  constructor(el) {
    this.el = el
    this.chars = '!<>-_\\/[]{}—=+*^?#𖤐__ツ'
    this.update = this.update.bind(this)
  }
  setText(newText) {
    const texto_antigo = this.el.innerText
    const length = Math.max(texto_antigo.length, newText.length)
    const promise = new Promise((resolve) => this.resolve = resolve)
    this.sequencia = []
    for (let i = 0; i < length; i++) {
      const from = texto_antigo[i] || ''
      const to = newText[i] || ''
      const inicio = Math.floor(Math.random() * 40)
      const fim = inicio + Math.floor(Math.random() * 40)
      this.sequencia.push({ from, to, inicio, fim })
    }
    cancelAnimationFrame(this.frameRequest)
    this.frame = 0
    this.update()
    return promise
  }
  update() {
    let output = ''
    let complete = 0
    for (let i = 0, n = this.sequencia.length; i < n; i++) {
      let { from, to, inicio, fim, char } = this.sequencia[i]
      if (this.frame >= fim) {
        complete++
        output += to
      } else if (this.frame >= inicio) {
        if (!char || Math.random() < 0.35) {
          char = this.randomChar()
          this.sequencia[i].char = char
        }
        output += `<span class="dud">${char}</span>`
      } else {
        output += from
      }
    }
    this.el.innerHTML = output
    if (complete === this.sequencia.length) {
      this.resolve()
    } else {
      this.frameRequest = requestAnimationFrame(this.update)
      this.frame++
    }
  }
  randomChar() {
    return this.chars[Math.floor(Math.random() * this.chars.length)]
  }
}

const frases = [
  'Olá,',
  'Aloha,',
  'Hello,',
  'Saluton,',
  'Nihao,',
  'Hallå,',
  'Bonjour,'
]

const el = document.querySelector('.text')
const fx = new animacao_texto(el)

let counter = 0
const next = () => {
  fx.setText(frases[counter]).then(() => {
    setTimeout(next, 1000)
  })
  counter = (counter + 1) % frases.length
}

next()