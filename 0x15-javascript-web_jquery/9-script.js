// Get a value of a given key from a link to json.

$(document).ready(function () {
	const url = "https://fourtonfish.com/hellosalut/?lang=fr";
	$.getJSON(url, function(data) {
		const hello = data.hello;
		$("#hello").text(hello);
	});
});
