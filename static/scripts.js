function verify(){

    let descendentes = document.querySelectorAll(".link-td");
    let item;

    for (let i = 0; i < descendentes.length; i++) {
        descendentes[i].addEventListener("click", function (e) {
            item = this.innerHTML
            //alert('O elemento clicado foi o ' + this.innerHTML);
            var r=confirm("Tem certeza que deseja deletar esse item?");
            if (r==true){
                    window.location.assign('http://127.0.0.1:5000/del_data/' + item);
                }
            else{
                    window.location.assign('http://127.0.0.1:5000/read_all');
                }
        })
    }

}