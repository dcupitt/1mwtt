// =================== WEEK 1 HOMEWORK ====================
$(document).ready(function(){
  // ===================  DAY 1 ====================

  // Hours in a year. How many hours are in a year?
  var hrInYr = 24 * 365;
  var hrInYrString = "Hours in a Year: " + hrInYr;
  console.log(hrInYrString);


  // Minutes in a decade. How many minutes are in a decade?
  var minInDec = hrInYr * 60 * 10 + (2 * 24);
  var minInDecString = "Minutes in a Decade: " + minInDec;
  console.log(minInDecString);


  // Your age in seconds. How many seconds old are you? (I'm not going to check your answer, so be as accurate—or not—as you want.)
  var secInDay = 24 * 60 * 60;
  var myAgeDays = (27 * 365) + 35 + Math.round(27 / 4);
  var myAgeSecs = myAgeDays * secInDay;
  var myAgeSecsString = "My Age in Seconds: " + myAgeSecs;
  console.log(myAgeSecsString);


  // Cristina Tarantino: 32 yesterday! How many milliseconds old is she hahaha? Calculate @Cristina Tarantino's age in milliseconds.
  var millisecInDay = secInDay * 1000;
  var CristinaTarantinoAgeMillisecs = (32 * (365 + (32/4))) * millisecInDay;
  CristinaTarantinoAgeMillisecsString = "Cristina Tarantino's Age in Milliseconds: " + CristinaTarantinoAgeMillisecs;
  console.log(CristinaTarantinoAgeMillisecsString);


  // Print homework day 1 to page

  var $day1 = $( "#day1" )
  var htmlHw =
          '<div>' + '<h1>' + hrInYrString +'</h1></div>' +
          '<div>' + '<h1>' + minInDecString +'</h1></div>' +
          '<div>' + '<h1>' + myAgeSecsString +'</h1></div>' +
          '<div>' + '<h1>' + CristinaTarantinoAgeMillisecsString +'</h1></div>';
  $day1.append(htmlHw);

  // ============================================================================
  // ===================  DAY 2 ====================

  // Music note A 440 Hz 1 octave is double the frequency tempered piano A' 880 Hz Calculate and console.log the frequency each of the 12 notes between A and A' Hint: the notes are NOT in a linear scale, but in a geometric scale
  // Expected results:
  // var A = 440
  // A# = 466.16
  // B = 493.88
  // C = 523.25
  // C# = 554.37
  // D = 587.33
  // D# = 622.25
  // E = 659.26
  // F = 698.46
  // F# = 739.99
  // G = 783.99
  // G# = 830.61
  // A = 880;
  var musicScale = [440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.26, 698.46, 739.99, 783.99, 830.61, 880];

  var scaleDif = function (array) {
    var difArray = [];
    for (i = 0; i < musicScale.length - 1; i++) {
      var dif = array[i + 1] - array[i];
      difArray.push(dif);
    };
    console.log(difArray)
  }

  scaleDif(musicScale);

  // A * (2 ^ i/12)

  var musicScaleNotes = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A"];

  var scaleHz = function(array) {
    var newArray = [];
    for (var i = 0; i < array.length - 1; i++) {
      newArray.push(array[i] + " : " + (440 * (2 ** ((i)/12))).toFixed(2));
    };
    console.log(newArray);
    return newArray;
  }

  scaleHz(musicScaleNotes);

  var scaleHzObject = function(array) {
    var newArray = [];
    for (var i = 0; i < array.length - 1; i++) {
      var element = array[i];
      newArray.push({[element]: (440 * (2 ** ((i)/12))).toFixed(2)});
    };
    console.log(newArray);
    return newArray;
  }

  scaleHzObject(musicScaleNotes);


  // Planets
  // Calculate and console log how many 'minutes' the Moon travels in a day. Hint: first calculate how many degrees the Moons travels in the sky when the Earth returns to the same position during its daily rotation.




  // The moon orbits quite fast: it moves about 0.5 degrees per hour in the sky. In 24 hours it moves 13 degrees. The moon's observed motion eastward results from its physical motion of the moon along its orbit around the Earth.


// Earth rotation in 24 hours: 360 degrees

// Moon orbit in 24 hours: 13 degrees
// 60 minutes in 1 degree


});