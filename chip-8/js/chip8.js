import Renderer from './renderer.js'
import Keyboard from './keyboard.js'
import Speaker from './speaker.js'
const renderer = new Renderer(12)
const keyboard = new Keyboard()
const speaker = new Speaker()

let loop

let fps = 60,
  fpsInterval,
  startTime,
  now,
  then,
  elapsed

const init = () => {
  fpsInterval = 1000 / fps
  then = Date.now()
  startTime = then

  // TESTING CODE. REMOVE WHEN DONE TESTING.
  // renderer.testRender()
  // renderer.render()
  // END TESTING CODE

  loop = requestAnimationFrame(step)
}

const step = () => {
  now = Date.now()
  elapsed = now - then

  if (elapsed > fpsInterval) {
    // Cycle the CPU. We'll come back to this later and fill it out.
  }

  loop = requestAnimationFrame(step)
}

init()
