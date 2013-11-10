var nextDealID = undefined;
var nextOldDealID = undefined;
var insertedDeals = new Array();;

$(document).ready(function() {
	loadInsertDeals("dealsBox",undefined,undefined);
	
	$("#dealSearch").change(function(){
		filterDeals();
	});
});



function loadInsertDeals(destinationBox,idStart, direction){
	var queryURL;

	queryURL = "../get_deals.json";
	var testoHeading="";
	
	if (nextDealID != undefined) {
		queryURL+="startingDeal="+idStart+"&";
	}

	if (direction=='past') {
		queryURL += "direction="+direction+"&";
		// load old deals, otherwise defaults to get new ones
	}
	
	$.getJSON(queryURL, function(data) {
			if ($('#intestazioneLista').children().length == 0) {
				$("#intestazioneLista").append("<h3>"+testoHeading+"</h3>");
			}
			
			if (data.deals.length>0) {
				
				if (direction=='past') {
					for (var i = 0; i < data.deals.length; i++) { // newer on the top
						var currentDeal = data.deals[i];
						insertDeal(destinationBox,currentDeal,'bottom');
					}
				}else {
					for (var i = data.deals.length-1; i >= 0; i--) { // newer on the top
						var currentDeal = data.deals[i];
						insertDeal(destinationBox,currentDeal,undefined);
					}
				}
				
				var firstDealID = parseInt(data.deals[0].id);
				var lastDealID = parseInt(data.deals[data.deals.length-1].id);
				
				if (nextDealID==undefined||((firstDealID+1)>nextDealID)) {
					nextDealID=firstDealID+1;
				}
				
				if (nextOldDealID==undefined||((lastDealID-1)<nextOldDealID)) {
					nextOldDealID=lastDealID-1;
				}
				
				if ($('#fondoLista').children().length==0) {
					$('#fondoLista').append("<a href='javascript:loadPastDeals();'>Carica i deal più vecchi</a>");
				}
			}
	}).complete(function() {
		if (direction!='past') {
			setTimeout(function() {
				loadInsertDeals(destinationBox,nextDealID, direction);
			}, 10000*10000);
		}
	});

}






function insertDeal(destinationBox,deal,position) {
	var nextFavTrigger = true;
	var nextFavText = 'Favorite';
	if (deal.favorite!=undefined) {
		if (deal.favorite==true) {
			nextFavTrigger = false;
			nextFavText = 'Unfavorite';
		}
	}
	
	with(DOMBuilder.dom) {
		var elementToAdd = 
			DIV({'class':'item' + (deal.new?' newItem':'')},
				IMG({'src': deal.image}),
				DIV({'class':'descriptionBox'}, deal.description),
				DIV(
					DIV({'class':'shareBox', 'id': 'deal'+deal.id}, 'Share'),
					DIV({'class':'imageBox'}, A({'id':'favoriteDeal'+deal.id,'href':"javascript:flagFavorite("+deal.id+",'"+nextFavTrigger+"');"},IMG({'src':deal.favorite?'../static/images/heart_red.png':'../static/images/heart_gray.png'}))),
					DIV({'class':'clear'})
				)
			);
	}
	
					  	
	//insertedDeals[insertedDeals.length] = deal;
	//elementToAdd.style.display="none";
	
	if (position=='bottom') {
		$("#"+destinationBox).append(elementToAdd);
		$('#dealsBox').masonry( 'appended', elementToAdd );
		alert("should get the PENULTIMATE CHILD, the last one is the clear!");
	}else {
		$("#"+destinationBox).prepend(elementToAdd);
		$('#dealsBox').masonry( 'appended', elementToAdd );
		
	}
	
	$('#deal'+deal.id).popover({
	'html':true,
	'trigger':'hover',
	'content': function(){
		var formattedBody = "Moose is my favorite tool to organize shopping deals from my email inbox.\n I discovered " + escape(deal.description) + " thanks to it!";
		var mailToLink = "mailto:?subject=I%20would%20like%20to%20invite%20you%20to%20join%20Moose.com&body=" + formattedBody;
	
	
	
		return "<a target='_blank' href='http://www.facebook.com/sharer/sharer.php?s=100&p[url]=www.moose.com&p[title]=Great%20deal%20found%20thanks%20to%20Moose.com&p[summary]="+ escape(deal.description) +"'><img class='smallImage' src='../static/images/facebook.png'></a><br /><a target='_blank' href='http://twitter.com/home?status=Moose%20is%20my%20favorite%20tool%20to%20organize%20my%20inbox%20shopping%20deals: "+ escape(deal.description) +"'><img class='smallImage' src='../static/images/twitter.png'></a><br /><a href='"+mailToLink+"'><img class='smallImage' src='../static/images/envelope.png'></a>";
	}
});

	
	//$('#deal'+deal.id+" .rowContent .rowText").html(dealContent);
	
	//$("#deal"+deal.id).fadeIn('slow');
}


function loadPastTweets() {
	loadInsertTweets("dealsBox",nextOldDealID,'past');
}

function filterDeals(){
	var string = $("#dealSearch").val();
	insertedDeals.forEach(function(item, index){
		if((item.description.indexOf(string) == -1) && (item.store.indexOf(string) == -1)){
			var toRemove = new Array();
			toRemove.push($("#deal"+item.id));
			$("#dealsBox").masonry( 'hide', toRemove);	
		} else{
			console.log("ok");
		}
	}) 
}








function flagFavorite(dealid,toStatus){
	$("#favoriteDeal"+dealid).removeAttr('href');

	queryURL = "../setasfavorite/"+dealid+"/"+toStatus;

	$.getJSON(queryURL, function(data) {
		if (data.status==true) {
			if (toStatus==true) {
				$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'false');");
				$("#favoriteDeal"+dealid).text("Unfavorite");
			}else {
				$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'true');");
				$("#favoriteDeal"+dealid).text("Favorite");
			}
			
			// metti l'href nuovo
			// cambia testo in Unfavorite
		}else {
			if (toStatus==true) {
				$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'true');");
			}else {
				$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'false');");
			}
			
			// rimetti l'href vecchio
		}
	}).error(function(xhr, ajaxOptions, thrownError) {
		console.log(xhr.responseText);
		if (toStatus=='Y') {
			$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'true');");
		}else {
			$("#favoriteDeal"+dealid).attr("href","javascript:flagFavorite("+dealid+",'false');");
		}
		// rimetti l'href vecchio
	}).complete(function() {
		
	});
}