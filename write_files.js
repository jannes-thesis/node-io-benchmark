const { promisify } = require("util");
fs = require('fs');

const asyncOpen = promisify(fs.open)
const asyncFsync = promisify(fs.fsync)
const aysncClose = promisify(fs.close)


async function read_write_delete(path) {
    const content = await fs.promises.readFile(path)
    await fs.promises.writeFile(path + '-b', content)
    const fd = await asyncOpen(path)
    await asyncFsync(fd)
    await aysncClose(fd)
    await fs.promises.unlink(path + '-b')
}

const writes = []
for (i = 1; i <= 30; i++) {
    writes.push(read_write_delete('/mnt/hdd/files/file' + i))
}

Promise.all(writes).then(() => console.log('done'))

