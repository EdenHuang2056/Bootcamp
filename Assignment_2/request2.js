
function avg(data){
    var Sum = 0;
    var Avg = 0;
    var Count = 0;
    var employeesList = data.employees;    
    for(i=0; i<data.count; i++){          
        Count = Count + 1
    };
    for(j=0; j<Count; j++){
        Salary = employeesList[j].salary;
        Sum += Salary;
    }
    j+=1;
    Avg = Sum / Count;
    document.write(Avg)
}


avg({
"count":3,
"employees":[
{"name":"John","salary":30000},
{"name":"Bob","salary":60000},
{"name":"Jenny","salary":50000}]
});

