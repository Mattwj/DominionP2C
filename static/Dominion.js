function buyPhase(){
    var response = null;
    var name = $("#playerNameInput").val();
    $.ajax({
        url:"http://192.168.0.230/BuyPhase/"+ name,
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });
    playerHand();
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

    playerHand();

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
    $.ajax({
        url:"http://192.168.0.230/Endpoints",
        method:"GET",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });
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
    console.log(response['data']);
    var hand = JSON.parse(response['data']).hand;
    $(".hand").hide();
    for(var i=0; i< hand.length; i++){
        $("#card"+i).attr("src", "http://192.168.0.230/Image/"+ hand[i]);
        $("#card"+i).attr("onclick","handAction(this);");
        $("#hand"+i).show();
        
    }
    
    var data = JSON.parse(response['data']);

    var actions = data.actions;
    $("#actions").text(actions);
    var buys = data.buys;
    $("#buys").text(buys);
    var coins = data.coins;
    $("#coins").text(coins);

    $.ajax({
        url:"http://192.168.0.230/GetCardsWithCounts",
        method:"GET",
        async: false,
        success:function(data){
            response = data;
            console.log(response);
        }
    });
}

function boardCards(){
    var board = null;
    $.ajax({
        url: "http://192.168.0.230/GetCards",
        method: "GET",
        async: false,
        success:function(data){
            board = data;
            
            console.log(board);
        }
    });
    console.log(board['data']);
    var boardcards = JSON.parse(board['data']).cards;
    console.log(boardcards);
    $(".gameCards").hide();
    for(var i=0; i< boardcards.length; i++){
        $("#cboard"+i).attr("src", "http://192.168.0.230/Image/"+ boardcards[i]);
        $("#cboard"+i).attr("onclick","buyCard(this);");
        $("#gameCards"+i).show();
        
    }
    var statics = $(".static");
    statics.each(function(){
        $(this).attr("onclick","buyCard(this);");
        
    });

    cardCounts();
    
}

function startGame(){
    $("#startGame").hide();
    
    var response = null;
    $.ajax({
        url:"http://192.168.0.230/StartGame",
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });
    board = boardCards();
    console.log(board);

    playerHand();
}

function buyCard(cardimage){
    var url = $(cardimage).attr("src");
    var urlparts = url.split('/');
    var card = urlparts.pop();

    var name = $("#playerNameInput").val();
    $.ajax({
        url:"http://192.168.0.230/BuyCard/"+name + "/"+ card,
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });
    playerHand();

}

function handAction(cardimage){
    var url = $(cardimage).attr("src");
    var urlparts = url.split('/');
    var card = urlparts.pop();

    var name = $("#playerNameInput").val();
    $.ajax({
        url:"http://192.168.0.230/UseCard/"+name + "/"+ card,
        method:"POST",
        async: false,
        success:function(data){
            response = data;
            console.log(data);
        }
    });
    playerHand();
}

function cardCounts(){
        var counts = null;
    $.ajax({
        url: "http://192.168.0.230/GetCardsWithCounts",
        method: "GET",
        async: false,
        success:function(data){
            info = data;
            
            console.log(info);
        }
    });

    var info = JSON.parse(info['data']);
    var finites = $(".finite");
    for(var i=0; i<finites.length; i++){
        for(var j=0; j<info.cards.length; j++){
            if($($(finites[i]).children("img")[0]).attr("src").search(info.cards[j])!=-1){
                
                var spanEle = $(finites[i]).find("span")[0];
                spanEle.innerHTML = info.counts[j];
                
            }
        }
    }
    $(".overlay").show();

    

}