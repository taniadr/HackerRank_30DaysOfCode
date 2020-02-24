function processData(input) {
    //Enter your code here
    var evenIndexed = "";
    var oddIndexed = "";

    for (i=0; i < input.length - 2;){
        evenIndexed += input.charAt(i);
        oddIndexed += input.charAt(i+1);
        i = i+2;
    }
    console.log(evenIndexed + " " + oddIndexed + '\n');
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
