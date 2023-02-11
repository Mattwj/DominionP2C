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

    location.reload();

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
    hand = playerHand();
    console.log(hand);
}


function playerHand(){
    var response = null;
    var name = $("#playerNameInput").val();
    $.ajax({
        url:"http://192.168.0.230/GetPlayer/" +name,
        method:"GET",
        async: false,
        success:function(data){
            response = data;
            
        }
    });
    var hand = JSON.parse(response['data']).hand;
    $(".hand").hide();
    for(var i=0; i< hand.length; i++){
        $("#card"+i).attr("src", "http://192.168.0.230/Image/"+ hand[i]);
        $("#hand"+i).show();
        
    }
    return hand;
}