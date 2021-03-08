

function calculate(min, max){
    let total = 0;
    for(i=min; i<=max; i++){
        total = total + min;
        min++;
    }
    console.log(total);
}

calculate(1, 3)
calculate(4, 8)


