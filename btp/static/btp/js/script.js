$(document).ready(function(){
    var hideit = ['#faculty-view', '#projects-view', '#students-view','#submit-view','#submissions-view', '#deadlines-view', '#home-view'];
    for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }	
    $('#home-view').show();	
    
    $('#faculty-link').click(function(){
    for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }
    $('#faculty-view').show();	
    });
    $('#students-link').click(function(){
    for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }
    $('#students-view').show();
    });
    $('#projects-link').click(function(){
    for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }
    $('#projects-view').show();
    });
    $('#submissions-link').click(function(){
    
    for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }
    $('#submissions-view').show();
    });  
    $('#submit-link').click(function(){
     for(var i=0; i<hideit.length; i++){
	$(hideit[i]).hide();	
    }
    $('#submit-view').show();	
    });      
    	    
    
});
