'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

function getLetter(s) {
    let letter;
    
    if ('aeiou'.indexOf(s[0]) >= 0) {
        letter = 'A';
    } else if ('bcdfg'.indexOf(s[0]) >= 0) {
        letter = 'B';
    } else if ('hjklm'.indexOf(s[0]) >= 0) {
        letter = 'C';
    } else if ('npqrstvxyz'.indexOf(s[0]) >= 0) {
        letter = 'D';
    }
    
    return letter;
}


function main() {
    const s = readLine();
    
    console.log(getLetter(s));
}