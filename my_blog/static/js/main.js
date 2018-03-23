window.fbAsyncInit = function() {
  FB.init({
    appId      : '{216836045536768}',
    cookie     : true,
    xfbml      : true,
    version    : '{latest-api-version}'
  });

  FB.AppEvents.logPageView();

};

(function(d, s, id){
   var js, fjs = d.getElementsByTagName(s)[0];
   if (d.getElementById(id)) {return;}
   js = d.createElement(s); js.id = id;
   js.src = "https://connect.facebook.net/en_US/sdk.js";
   fjs.parentNode.insertBefore(js, fjs);
 }(document, 'script', 'facebook-jssdk'));

 function fbAuthUser() {FB.login(function(response) {
  if (response.authResponse) {
   console.log('Welcome!  Fetching your information.... ');
   FB.api('/me', function(response) {
     console.log('Good to see you, ' + response.name + '.');
   });
  } else {
   console.log('User cancelled login or did not fully authorize.');
  }
})};
function fbLogoutUser() {FB.logout(function(response) {
console.log("Logout")
})};

document.getElementById("fb-login").onClick = "fbAuthUser()";
document.getElementById("fb-logout").onClick = "fbLogoutUser()";
