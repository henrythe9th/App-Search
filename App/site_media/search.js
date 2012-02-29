function search_submit() {
	var query = $("#id_query").val();
	$("#search_results").load(/search/?ajax&query="+ encodeURIComponent(query));
	$("#search_results").hide();
	$("#search_results").fadeIn();
	return false;
}

$(document).ready(
	function () {
		$("#search-form).submit(search_submit);
		$("#id_query").result(search_submit);
	}
});
