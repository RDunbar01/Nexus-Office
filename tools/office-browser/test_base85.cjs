const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const code=fs.readFileSync(__dirname+'/loader.js','utf8');const start=code.indexOf('function decode85('),end=code.indexOf('function restore(');const ctx={Uint8Array,Int16Array,Error};vm.runInNewContext(code.slice(start,end),ctx);
for(const v of JSON.parse(fs.readFileSync(__dirname+'/BASE85_VECTORS.json','utf8')))assert.equal(Buffer.from(ctx.decode85(v.base85)).toString('hex'),v.hex);
for(const invalid of ['0','000000','~~~~~','/////','0000"','0000é'])assert.throws(()=>ctx.decode85(invalid));
assert.equal(Buffer.from(ctx.decode85('|NsC0')).toString('hex'),'ffffffff');console.log('PASS base85 lengths0–8, random buffers, maximum word, invalid characters, impossible tail and overflow');
