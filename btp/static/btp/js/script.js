$(document).ready(function(){
    
    $('#faculty-view').hide();$('#projects-view').hide();$('#students-view').hide();$('#home-view').show();
    $('#faculty-link').click(function(){
    $('#faculty-view').show();$('#projects-view').hide();$('#students-view').hide();$('#home-view').hide();
    });
    $('#students-link').click(function(){
    $('#faculty-view').hide();$('#projects-view').hide();$('#students-view').show();$('#home-view').hide();
    });
    $('#projects-link').click(function(){
    $('#faculty-view').hide();$('#projects-view').show();$('#students-view').hide();$('#home-view').hide();
    });
    $('#home-link').click(function(){
    $('#faculty-view').hide();$('#projects-view').hide();$('#students-view').hide();$('#home-view').show();
    });      
    
});