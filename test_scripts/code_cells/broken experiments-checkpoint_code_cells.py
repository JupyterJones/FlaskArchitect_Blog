import vsketch

#JES4-3 #KyraMoran #created 9/20/19

#this program makes shapes based on the x and y coordinate range in the picture

from random import *

#makeBackground
lightBlue = makeColor (100,150,200)
pic = makeEmptyPicture(600,600,lightBlue)


pink1 = makeColor (230, 160, 160) #just wanted to practice making a color
  
for i in range (200):
  xCord = randint(0,600) #starting x coordinate
  yCord = randint(0,600) #starting y coordinate
  circle = randint(10,60) #height and width of circles
  square = randint(10,100) #height and width of squares
  ovalWidth = randint (10,50) #width of ovals
  ovalHeight = randint (10,80) #height of ovals
  
  if xCord < 200: #left third
    addOval(pic,xCord,yCord, circle, circle, green)
    
  elif 200 < xCord < 400: #middle third
    if yCord < 200:
      addRect(pic, xCord, yCord, square, square, pink1) #top third
    elif 200 <= yCord <= 400:
      addRect(pic, xCord, yCord, square, square, blue) #middle third   
    else:
      addRect(pic, xCord, yCord, square, square, yellow) #bottom third
    
  else: #right third
    addOval(pic, xCord, yCord, ovalWidth, ovalHeight, lightGray)

show(pic)

https://spin.atomicobject.com/2022/04/26/generative-art-recursion/

function getCircleX(radians, radius) {
  return Math.cos(radians) * radius;
}

console.log(getCircleX(1, 10));
// expected output: 5.403023058681398

console.log(getCircleX(2, 10));
// expected output: -4.161468365471424

console.log(getCircleX(Math.PI, 10));
// expected output: -10


//helper
/**
 * converts degree to radians
 * @param degree
 * @returns {number}
 */
var toRadians = function (degree) {
    return degree * (Math.PI / 180);
};

/**
 * Converts radian to degree
 * @param radians
 * @returns {number}
 */
var toDegree = function (radians) {
    return radians * (180 / Math.PI);
}

/**
 * Rounds a number mathematical correct to the number of decimals
 * @param number
 * @param decimals (optional, default: 5)
 * @returns {number}
 */
var roundNumber = function(number, decimals) {
    decimals = decimals || 5;
    return Math.round(number * Math.pow(10, decimals)) / Math.pow(10, decimals);
}
//the object
var MathD = {
    sin: function(number){
        return roundNumber(Math.sin(toRadians(number)));
    },
    cos: function(number){
        return roundNumber(Math.cos(toRadians(number)));
    },
    tan: function(number){
        return roundNumber(Math.tan(toRadians(number)));
    },
    asin: function(number){
        return roundNumber(toDegree(Math.asin(number)));
    },
    acos: function(number){
       return roundNumber(toDegree(Math.acos(number)));
   },
   atan: function(number){
       return roundNumber(toDegree(Math.atan(number)));
   }
};


Math.sin(35)

MathD{cos(3)}

toRadians(45)

var data = [
    { 
        "name": "ananta",
        "age": "15",
        "country": "Atlanta"
    }
];

data.push({"name": "Tony Montana", "age": "99"});

data.push({"country": "IN"});

data

var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
x1 = 30;
y1 = 40;
r =  50;
theta = 0.5;
ctx.moveTo(x1, y1);
ctx.lineTo(x1 + r * Math.cos(theta), y1 + r * Math.sin(theta));
ctx.stroke();

//where you must make sure that theta is in radians and that ctx is defined to be whatever canvas context you //want it to be (in the above code, this means you want something like

<canvas id="myCanvas" width="200" height="100"
style="border:1px solid #000000;">
</canvas>

function drawTree(x, y, angle, length) {
  const [x1, y1] = [x, y];
  const x2 = x1 + Math.cos(angle) * length;
  const y2 = y1 - Math.sin(angle) * length;
  
  var line = (x1, y1, x2, y2);
  var minLength = 5
  var angleChange = 6
  var lengthRatio = .6
  if (length >= minLength) {
    drawTree(x2, y2, angle + angleChange, length * lengthRatio);
    drawTree(x2, y2, angle - angleChange, length * lengthRatio);
  } else {
    drawLeaves(x2, y2);
  }
}

function drawLeaves(x, y) {
  drawTree.push(x,y);
  
  fill(leafColor);
  noStroke();
  
  for (let i = 0; i < leafDensity; i++) {
    circle(
      randomGaussian(x, 10),
      randomGaussian(y, 10),
      random(2, 5)
    );
  }
  
  pop();
}

drawTree(3, 4, 37, 30)

function drawTree(x, y, angle, length) {
  const [x1, y1] = [x, y];
  const x2 = x1 + cos(angle) * length;
  const y2 = y1 - sin(angle) * length;
  
  line(x1, y1, x2, y2);

  if (length >= minLength) {
    drawTree(x2, y2, angle + angleChange, length * lengthRatio);
    drawTree(x2, y2, angle - angleChange, length * lengthRatio);
  } else {
    drawLeaves(x2, y2);
  }
}

function drawLeaves(x, y) {
  push();
  
  fill(leafColor);
  noStroke();
  
  for (let i = 0; i < leafDensity; i++) {
    circle(
      randomGaussian(x, 10),
      randomGaussian(y, 10),
      random(2, 5)
    );
  }
  
  pop();
}

drawTree(3, 4, 37, 30)

!npm install math

%%javascript
// We make sure the `counter` module is defined
// only once.
require.undef('counter');

// We define the `counter` module depending on the
// Jupyter widgets framework.
define('counter', ["@jupyter-widgets/base"],
       function(widgets) {

    // We create the CounterView frontend class,
    // deriving from DOMWidgetView.
    var CounterView = widgets.DOMWidgetView.extend({

        // This method creates the HTML widget.
        render: function() {
            // The value_changed() method should be
            // called when the model's value changes
            // on the kernel side.
            this.value_changed();
            this.model.on('change:value',
                          this.value_changed, this);

            var model = this.model;
            var that = this;

            // We create the plus and minus buttons.
            this.bm = $('<button/>')
            .text('-')
            .click(function() {
                // When the button is clicked,
                // the model's value is updated.
                var x = model.get('value');
                model.set('value', x - 1);
                that.touch();
            });

            this.bp = $('<button/>')
            .text('+')
            .click(function() {
                var x = model.get('value');
                model.set('value', x + 1);
                that.touch();
            });

            // This element displays the current
            // value of the counter.
            this.span = $('<span />')
            .text('0')
            .css({marginLeft: '10px',
                  marginRight: '10px'});

            // this.el represents the widget's DOM
            // element. We add the minus button,
            // the span element, and the plus button.
            $(this.el)
            .append(this.bm)
            .append(this.span)
            .append(this.bp);
        },

        value_changed: function() {
            // Update the displayed number when the
            // counter's value changes.
            var x = this.model.get('value');
            $($(this.el).children()[1]).text(x);
        },
    });

    return {
        CounterView : CounterView
    };
});


CounterView()



