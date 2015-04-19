function User(){

   // Add object properties
   this.firstname = " ";
   this.lastname = " ";
   this.email = " ";
   this.ssn = " ";
   this.phone = " ";
   this.url = " ";
   this.password = " ";
   this.passwordStrngth = " ";
   this.dob = " ";
   this.dobWithTime = " ";
   this.creditcardnumber = " ";

   this.toJSONString = function(){
   		return JSON.stringify(this);
   };

    this.readFromJSONString = function(u){

	var userJson = JSON.parse(u);
	this.firstname = userJson.firstname;
   this.lastname = userJson.lastname;
   this.email = userJson.email;
   this.ssn = userJson.ssn;
   this.phone = userJson.phone;
   this.url = userJson.url;
   this.password = userJson.password;
   this.passwordStrngth = userJson.passwordStrngth;
   this.dob = userJson.dob;
   this.dobWithTime = userJson.dobWithTime;
   this.creditcardnumber = userJson.creditcardnumber;
	};

	this.isPhoneNumberFormatValid = function()
	{
	 
	 console.log("inside pppppppphhhhhhh");
	 // var phoneNumberPattern = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;  
	 var phoneNumberPattern = /^\(?(\d{3})\)?[-](\d{3})[-](\d{4})$/;  
	  console.log("inside valid phone number "+ phoneNumberPattern.test(this.phone));  
	  return phoneNumberPattern.test(this.phone);
	
	};

	this.isValidEmail = function() 
	{
		var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	    return re.test(this.email);
	} ;

	}


function saveToLocalStorage(str){

	if (Modernizr.localstorage) 
	{
			//alert("You are offline: Data is being stored in localStorage");
			//console.log('Offline mode:local storage is enabled')		
			localStorage.setItem("userObject", str);
			//console.log('saved to localstorage')

	}
}

function saveToSessionStorage(str){

	if(Modernizr.sessionstorage) 
	{
			//alert("You are online: Data is being stored in sessionStorage");
			//console.log('session storage enabled');
			
			sessionStorage.setItem("userObject", str);
	}

}

function readFromLocalStorage() 
{
	if (Modernizr.localstorage) 
		{
				//alert("You are offline: Data is being retrieved from localStorage");
				//console.log('Offline mode:local storage is enabled')		
				var userString = localStorage.getItem("userObject");

				//console.log('saved to localstorage')
				return userString;
		}
		
	return null;
}

function readFromSessionStorage()
{
if(Modernizr.sessionstorage) 
	{
			//alert("You are online: Data is being read from sessionStorage");
			//console.log('session storage enabled');
			
			var userString = sessionStorage.getItem("userObject");
			return userString;
	}
	return null;

}
//Define Even Handler for the Class - Net Offline or Online