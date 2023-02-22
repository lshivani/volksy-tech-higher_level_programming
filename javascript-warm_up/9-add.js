#!/usr/bin/node
function add (a, b) {
	console.log(parsInt(a) + parseInt(b));
}
add(process.argv[2] + process.argv[3]));
