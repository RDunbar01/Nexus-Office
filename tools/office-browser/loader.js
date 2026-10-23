(function(){'use strict';
const boot=document.getElementById('nxOfficeBoot'),status=document.getElementById('nxBootStatus'),progress=document.getElementById('nxBootProgress'),error=document.getElementById('nxBootError'),retry=document.getElementById('nxBootRetry');
let busy=false;
function stage(n,text){progress.value=n;status.textContent=text;}
const frame=()=>new Promise(resolve=>setTimeout(resolve,0));
const hex=b=>Array.from(new Uint8Array(b),n=>n.toString(16).padStart(2,'0')).join('');
async function digest(bytes){return hex(await crypto.subtle.digest('SHA-256',bytes));}
function encode64(text){const bytes=new TextEncoder().encode(text);let binary='';for(let i=0;i<bytes.length;i+=32768)binary+=String.fromCharCode.apply(null,bytes.subarray(i,i+32768));return btoa(binary);}
function decode85(text){
 const alphabet='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&()*+-;<=>?@^_`{|}~';
 if(text.length%5===1)throw Error('Invalid embedded base85 length.');
 const table=new Int16Array(128);table.fill(-1);for(let i=0;i<alphabet.length;i++)table[alphabet.charCodeAt(i)]=i;
 const output=new Uint8Array(Math.floor(text.length*4/5));let offset=0;
 for(let i=0;i<text.length;i+=5){const count=Math.min(5,text.length-i);let value=0;
  for(let j=0;j<5;j++){const code=j<count?text.charCodeAt(i+j):126;const digit=code<128?table[code]:-1;if(digit<0)throw Error('Invalid embedded base85 character.');value=value*85+digit;}
  if(value>4294967295)throw Error('Embedded base85 block overflows.');
  for(let j=0;j<count-1;j++)output[offset++]=(value>>>((3-j)*8))&255;
 }
 return output;
}
function restore(pack,maximum){
 if(pack.schema!==1||!Array.isArray(pack.chunks)||pack.chunks.length>10000||!pack.chunks.every(s=>typeof s==='string'))throw Error('Invalid embedded dictionary.');
 let visits=0;
 function walk(nodes,depth){
  if(depth>4||!Array.isArray(nodes))throw Error('Invalid embedded structure.');
  const out=[];let length=0;
  for(const node of nodes){
   if(++visits>100000)throw Error('Embedded structure exceeds its limit.');
   let value;
   if(typeof node==='string')value=node;
   else if(node&&Object.keys(node).length===1&&Number.isInteger(node.r)&&node.r>=0&&node.r<pack.chunks.length)value=pack.chunks[node.r];
   else if(node&&Object.keys(node).length===1&&Array.isArray(node.b))value=encode64(walk(node.b,depth+1));
   else throw Error('Invalid embedded reference.');
   length+=value.length;if(length>maximum)throw Error('Expanded application exceeds its limit.');out.push(value);
  }
  return out.join('');
 }
 return walk(pack.parts,0);
}
async function start(){
 if(busy)return;busy=true;error.hidden=true;retry.hidden=true;
 try{
  if(typeof DecompressionStream!=='function'||typeof TextEncoder!=='function'||typeof TextDecoder!=='function'||!globalThis.crypto?.subtle)throw Error('This browser lacks the local decompression or integrity APIs needed by the single-file trial. Use a current desktop Chrome, Edge, Firefox or Safari browser. The full package remains available from the source link.');
  const config=JSON.parse(document.getElementById('nxOfficePackConfig').textContent);
  if(config.schema!==1||!Number.isSafeInteger(config.compressedBytes)||config.compressedBytes>20_000_000||!Number.isSafeInteger(config.packedBytes)||config.packedBytes>40_000_000||!Number.isSafeInteger(config.htmlBytes)||config.htmlBytes>40_000_000)throw Error('Invalid embedded size limits.');
  stage(1,'Decoding bundled data locally…');await frame();
  const encodedPayload=document.getElementById('nxOfficePackedApp').textContent.trim();
  if(encodedPayload.length!==Math.ceil(config.compressedBytes*5/4))throw Error('Embedded encoding length check failed.');
  const bytes=decode85(encodedPayload);
  if(bytes.length!==config.compressedBytes)throw Error('Embedded data length check failed. Download the HTML again.');
  if(await digest(bytes)!==config.compressedSha256)throw Error('Embedded data integrity check failed. Download the HTML again.');
  stage(2,'Expanding bundled assets…');await frame();
  const stream=new ReadableStream({start(controller){controller.enqueue(bytes);controller.close();}}).pipeThrough(new DecompressionStream('gzip'));
  const reader=stream.getReader(),chunks=[];let length=0;
  for(;;){const item=await reader.read();if(item.done)break;length+=item.value.byteLength;if(length>config.packedBytes){await reader.cancel();throw Error('Expanded data exceeds its verified limit.');}chunks.push(item.value);}
  if(length!==config.packedBytes)throw Error('Expanded data length check failed.');
  const raw=new Uint8Array(length);let offset=0;for(const chunk of chunks){raw.set(chunk,offset);offset+=chunk.byteLength;}
  stage(3,'Restoring the application…');await frame();
  const pack=JSON.parse(new TextDecoder('utf-8',{fatal:true}).decode(raw));const html=restore(pack,config.htmlBytes);const encoded=new TextEncoder().encode(html);
  if(encoded.length!==config.htmlBytes||await digest(encoded)!==config.htmlSha256)throw Error('Application reconstruction integrity check failed.');
  stage(4,'Starting Nexus Office…');await frame();
  // Only the verified, locally embedded app is written. Imported user documents
  // never enter this loader or this document.write path.
  document.open();document.write(html);document.close();
 }catch(e){busy=false;progress.value=0;status.textContent='Nexus Office could not start.';error.textContent=String(e&&e.message||e);error.hidden=false;retry.hidden=false;}
}
retry.addEventListener('click',start);start();
})();
