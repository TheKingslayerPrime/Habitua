var timerlimit = 1500;
	  var timepassed = 0;
    var stopped = false;
	  var timeleft = timerlimit;
	  let timerinterval = null;
      document
        .getElementById("startbtn")
        .onclick = startTimer;
	  document.getElementById("stopbtn").onclick = stopTimer;
	  
    function stopTimer(){
		  location.reload();
	  }
	  
	  function startTimer() {
  timerinterval = setInterval(() => {
    timepassed = timepassed += 1;
	decrementProgress();
    if (timeleft === 0 & stopped == false) {
      onTimesUp();
    }
  }, 1000);
}
	  function onTimesUp() {
		  alert("Time up!");
  clearInterval(timerinterval);
}
      function decrementProgress() {
        if (timeleft != 0) {
          timeleft = timeleft - 1;
          setProgress();
        }
      }
function fmtMSS(s){
	return(s-(s%=60))/60+(9<s?':':':0')+s
}
      function setProgress() {
        document.getElementById("progress-spinner").style.background = `conic-gradient(rgb(3, 133, 255) ${timeleft*360/timerlimit}deg ,rgb(242, 242, 242) ${timeleft*360/timerlimit}deg )`;
        document.getElementById("middle-circle").innerHTML =
          fmtMSS(timeleft).toString();
      }

      window.onload = function () {
        setProgress();
      };