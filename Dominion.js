function buyPhase(){
    var response = null;
    $.ajax({
        url:"http://192.168.0.230/BuyPhase/Matt",
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });

}

function endTurn(){
    var name = $("#playerNameInput").val();
    var response = null;
    $.ajax({
        url:"http://192.168.0.230/EndTurn/" + name,
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });

}

function reset(){
    var response = null;
    $.ajax({
        url:"http://192.168.0.230/ResetGame",
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });

}

function addPlayer(){
    var name = $("#playerNameInput").val();
    $("#addPlayer").hide();
    $("#playerNameInput").prop("readonly", true);
    var response = null;
    $.ajax({
        url:"http://192.168.0.230/AddPlayer/"+ name,
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });

}