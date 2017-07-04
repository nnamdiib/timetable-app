$(document).ready(function()
{
	// The API endpoint
	var END_POINT = "/dayend/";

	// Array for each id of the table columns.
	TABLE_COLUMN_IDS = ["course-name", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"];

	$("#submit").click(function(e){
		e.preventDefault();

		// Get all the input from the text fields,		
		var lastID = $("form input:last").attr("id");
		var currentID = parseInt(lastID.slice(lastID.lastIndexOf('e') + 1 ));
		var params = "";

		$("tbody").empty();
		// Manually constructing the query Param string
		for(var i = 1; i < currentID+1; i++) {
			if($("#course"+i).val() != ""){
				if(i > 1) {
					params += '&';
				}
				var course_code = $("#course"+i).val().toLowerCase().trim();
				params += 'code='+ course_code;
			}
		}

		var d = "http://"+ window.location.host + END_POINT + "?" + params;

		$.ajax({
			url: d,
			type: 'GET',
			dataType: "json",
			success: function(json){
				//parse_json_from_class_end(json);
				parse_json_from_day_end(json);
			}
		});

	});

});

$(document).ready(function()
{
	$("#add").click(function(e){
		// add a new form field to enter the courses.
		e.preventDefault();

		var lastID = $("form input:last").attr("id");
		var currentID = lastID.charAt(lastID.length - 1);
		var nextID = parseInt(currentID) + 1;

		var fieldDiv = $("<div></div>").addClass("form-group");
		
		// the inner div
		var innerDiv = $("<div></div>").addClass("col-sm-10");
						
		// Input
		var input = $("<input>").addClass("form-control");
		$(input).attr("type", "text");
		var newID = "course" + nextID;
		$(input).attr("id", newID);

		$("#submit").before(fieldDiv);
		$(fieldDiv).append(innerDiv);
		$(innerDiv).append(input);
		$(".form-group:last").after(fieldDiv);

	});
});


function parse_json_from_class_end(json)
{
	// the json response received from the 'class end point' is
	// already a list containing each queried class object as elements
	// so we just pass the json straight to be formatted into the table.
	input_timetable_elements(json);
}

function parse_json_from_day_end(json)
{
	// the json response received from the 'day end point'
	// has to be further processed into a list containing
	// each queried class object as elements.
	// we do such processing then pass it to be formatted into the table.
	all_classes = new Array();
	var i;

	for(i = 1; i < 6; i++) {
		var courses_in_day = json[TABLE_COLUMN_IDS[i]];
		all_classes = all_classes.concat(courses_in_day);		
	}
	input_timetable_elements(all_classes);
}

function input_timetable_elements(classes)
{
	// Creates the timetable by adding the table elements
	// on the html page.
	unique_courses = new Array();
	var i;
	var j;
	for(i = 0; i < classes.length; i++) {
		var obj = classes[i];

		if(unique_courses.includes(obj.course)){
			var row = $("#"+obj.course);
			for(j = 1; j < 6; j++) {
				if(obj.day == TABLE_COLUMN_IDS[j]) {
					var ch = $(row).children("td#"+obj.day)
					$(ch).text(obj.time);
				}
			}

		} 
		else {
			unique_courses.push(obj.course);						
			// make the row
			var row = $("<tr></tr>").attr("id", obj.course);
			$("tbody").append(row);

			// make the cell for course name.
			var coursename = $("<td></td>").text(obj.course);
			$(row).append(coursename)

			//loop and make the other cells for time. <td></td>
			for(j = 1; j < 6; j++) {
				var td = $("<td></td>").attr("id", TABLE_COLUMN_IDS[j]);
				if(obj.day == TABLE_COLUMN_IDS[j]) {
					$(td).text(obj.time);
				}
				$(row).append(td);
			}

		}
	}
}