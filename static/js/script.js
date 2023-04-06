function getsource(id){
    $.ajax({
        url:"https://api.spoonacular.com/recipes/"+id+"/information?apiKey=1948934612124d9e920b0dcbfe7078f0",
        success: function(res){
            document.getElementById('sourceLink').innerHTML=res.sourceUrl
            document.getElementById('sourceLink').href=res.sourceUrl
        }
    });
}

function getrecipe(q){
    $.ajax({
        url:"/search?q="+q,
        success: function(res){
            var result = res.results[0];
            var output = "<h1>"+result.title+"</h1><br><img src='"+result.image+"' width='400'/><br>ready in "+result.readyInMinutes+" minutes";
            document.getElementById('output').innerHTML = output;
            getsource(result.id);
        }
    });
}