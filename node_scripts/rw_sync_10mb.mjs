import { close, fsync, open } from 'fs';
import { promises as fs } from 'fs';
import { promisify } from 'util';

const fsOpen = promisify(open)
const fsClose = promisify(close)
const fsFsync = promisify(fsync)

async function read_write_delete(path) {
    const content = await fs.readFile(path)
    await fs.writeFile(path + '-b', content)
    const fd = await fsOpen(path)
    await fsFsync(fd)
    await fsClose(fd)
    await fs.unlink(path + '-b')
}

const fileDir = process.argv[2]
const n = process.argv[3]
// do max 100 files at same time, so we don't run oom
const batches = Math.ceil(n / 100)
console.log('amount batches: ', batches)

var currentBatch = 1
var fileCounter = 1
while (currentBatch <= batches) {
    const batchLastFile = Math.min(n, currentBatch * 100)
    const writes = []
    while (fileCounter <= batchLastFile) {
        writes.push(read_write_delete(fileDir + '/10mb-' + fileCounter + '.txt'))
        fileCounter += 1
    }
    await Promise.all(writes)
    console.log(`done with batch ${currentBatch}`)
    currentBatch += 1
}

