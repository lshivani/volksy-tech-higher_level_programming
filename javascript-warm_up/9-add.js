#!/usr/bin/node
function (a, b) {
	console.log(parsInt(a) + parseInt(b));
}
add(console.log(process.argv[2] + process.argv[3]));
