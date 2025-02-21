const a = new ArrayBuffer(6);
console.log(a);

const a8 = new Uint8Array(a);
console.log(a8);
console.log(a);

a8[1] = 45;
console.log(a8);
console.log(a);

const a16 = new Uint16Array(a);
console.log(a16);

a16[1] = 0x4545;
console.log(a16);
console.log(a);
