  // Your web app's Firebase configuration
  var firebaseConfig = {
    apiKey: "AIzaSyAqnO34l13pTkWWJYPOuscGd1qaqABhLbU",
    authDomain: "movies-by-the-sea-279218.firebaseapp.com",
    databaseURL: "https://movies-by-the-sea-279218.firebaseio.com",
    projectId: "movies-by-the-sea-279218",
    storageBucket: "movies-by-the-sea-279218.appspot.com",
    messagingSenderId: "11881734156",
    appId: "1:11881734156:web:9ef020bd4be1ae5aaece29"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);


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