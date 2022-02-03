  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyA6C1MNPPYJmfKWWgsM7fe3a_VhN_VDsvI",
    authDomain: "movies-by-the-sea-3450e.firebaseapp.com",
    databaseURL: "https://movies-by-the-sea-3450e.firebaseio.com",
    projectId: "movies-by-the-sea-3450e",
    storageBucket: "movies-by-the-sea-3450e.appspot.com",
    messagingSenderId: "218385950220",
    appId: "1:218385950220:web:349fb2bd19c640b0543029"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  var messageRef = firebase.database().ref('Message');
function getIDValue(id)
{
    return document.getElementById(id).value;
}
function submit(e)
{
    e.preventDefault();
    console.log(123);

    var name = getIDValue('name');
    var email = getIDValue('email');
    var subject = getIDValue('subject');
    var message = getIDValue('message');

    console.log(name);

    saveMessage(name,email,subject,message);

    document.querySelector('#sendmessage').style.display = 'block';

    setTimeout(function()
        {
            document.querySelector('#sendmessage').style.display = 'none';
        },3000);
}
function saveMessage(name,email,subject,message)
{
    var NewMessageRef = messageRef.push();
    NewMessageRef.set({
        name: name,
        email: email,
        subject: subject,
        message: message
    });
}
filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("journal-info");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}
function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}
function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}