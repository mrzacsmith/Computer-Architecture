class CPU {
  constructor(renderer, keyboard, speaker) {
    this.renderer = renderer
    this.keyboard = keyboard
    this.speaker = speaker

    this.memory = new Uint8Array(4096)
    this.v = new Uint8Array(16)
    this.i = 0
    this.delayTimer = 0
    this.soundTimer = 0

    this.pc = 0x200
    this.stack = new Array()

    this.paused = false
    this.speed = 10
  }
}

export default CPU
