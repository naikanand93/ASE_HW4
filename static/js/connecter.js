$(document).ready(function(){

	console.log("Executing Javascript.")

	users_list = ""

	$.ajax({
		url: '/get',
		type: 'GET',
		success: function(response) {
			console.log('In the AJAX Call for Getting all Users')
			users_list = response;
			console.log(users_list);

			for(var i = 0; i < users_list.length; i++) {
				document.getElementById('display').innerHTML = users_list + "<br>"

			}
		},
		error: function(error) {
			console.log(JSON.stringify(error));
			$('#testing').text(JSON.stringify(error));
		}

	})

})