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
			
		// Input
		var input = $("<input>").addClass("form-control");
		$(input).attr("type", "text");
		var newID = "course" + nextID;
		$(input).attr("id", newID);

		$("#submit").parent().parent().before(fieldDiv);
		$(".form-group:last").append(input);

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
					
          obj.time = TrimData(obj.time);

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

          obj.time = TrimData(obj.time);

          $(td).text(obj.time);
				}

				$(row).append(td);
			}

		}
	}
}


/**
 * Trims time data ensure time is in 12 hours system
 * @param  {string} time_data [time string]
 * @return {string}           [time in 12 hours system]
 */
function trim_data(time_data) {
  var final_time = "";
  var time_object = time_data.split('-');

  count = 0;
  time_object.forEach(function(item) {

      if(item[0].substring(0, 1) === "0") {
        temp = item.substring(1);
        item = temp;
      }

      if(~item.indexOf("pm")) {
        //first section contains pm
        final_time += ( ( parseInt(item.replace("pm","")) - 12 ) + "pm");
      }
      else {
        final_time += item;
      }

      if(count == 0) {
        final_time += " - ";
        count++;
      };
  });

  return final_time;
}


/**
 * Enables string formatting using placeholders
 * Source : https://www.codeproject.com/Tips/201899/String-Format-in-JavaScript
 * @param  {array} args [values to replace]
 * @return {string}      [replaced string]
 */
String.prototype.format = function (args) {
      var str = this;

      return str.replace(String.prototype.format.regex, function(item) {

        var intVal = parseInt(item.substring(1, item.length - 1));
        
        var replace;
        
        if (intVal >= 0) {
          replace = args[intVal];
        } else if (intVal === -1) {
          replace = "{";
        } else if (intVal === -2) {
          replace = "}";
        } else {
          replace = "";
        }
        return replace;
      });
    };

String.prototype.format.regex = new RegExp("{-?[0-9]+}", "g");



/**
 * Prints only a particular portion of your screen
 * @param  {string} selector [id of section to print]
 * @param  {string} header_text [Header of document to print. <can be null>]
 */
function print_section(selector, header_text) {
  $(selector).printThis({
    header: header_text 
  });
}


/**
 * Print the timetable of user
 */
function print_table() {
  header_text = "<h4 class=\"text-left\">{0}</h4>";
  
  date_time_stamp = "Current date: {0}<br><br>Time: {1}<br><br>".format(
                      [
                        new Date().toLocaleDateString(),
                        new Date().toLocaleTimeString()
                      ]);

  header_text = header_text.format([date_time_stamp]);
  
  print_section('.time-table', header_text);
}