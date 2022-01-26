var start;
const element = document.getElementById("SEC");

function Click(id){
    if (String(id)=="start"){
        start = new Date().getSeconds();
    }
    else{
        ret = (new Date().getSeconds() - start);
        element.innerHTML = 504/(ret/60);
    }
}