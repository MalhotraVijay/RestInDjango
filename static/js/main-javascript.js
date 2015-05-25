/*(function(){
    window.alert("This loads on the page call in the browser");
}
)();
var SuccessAlignment = function(){
    //The main constructor function that makes the objects on which the APIs are exposed
    
    var constants = {} ; //Object to hold the system wide constants constants.
    
    //make AJAX call
    this.makeAjaxCall(url,data,success,failure){
        alert( url + data + success + failure);
    }
}
*/

var SuccessAlignment = function () {
    //The main constructor function that makes the objects on which the APIs are exposed
   
    //Object to hold the system wide constants constants.
     var constants = {
    };
    
    function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    
    //alert(csrftoken);
    //make AJAX call post settings
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    $.ajaxSetup({
    crossDomain: false, // obviates need for sameOrigin test
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
    });
};   


SuccessAlignment.prototype.makeAjaxCall = function (ajaxObj) {
        $.ajax({
            url : ajaxObj.url,
            data : ajaxObj.data,
            type : ajaxObj.type,
            success : function(data){
                ajaxObj.success(data);
            },
            failure : function(data){
                ajaxObj.failure(data);
            }
        });
}

SuccessAlignment.prototype.addDataToDOM = function(){
    
    //Think of the implemetation of this method !!
}

/*
ssc = new SuccessAlignment();
ssc.makeAjaxCall('abc.com');

ssc1= new SuccessAlignment();
ssc1.makeAjaxCall('xyzm');

*/