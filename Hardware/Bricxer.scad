use <threads.scad>;

RING_RAD = 36.8 / 2;
RING_GAP = 2.2;
RING_GRID = [2, 3];
MAX_LEDS = 12;
LED_SIZE = 5.25;
LED_THICKNESS = 1.6;
LED_OUTER_RAD = 35.58 / 2;
LED_INNER_RAD = 23.30 / 2;

POTENTIOMETER_SHAFT_RAD = 7.25/2;
POTENTIOMETER_KNOB_OFFSET = 4;

potentiometerSupportRad = POTENTIOMETER_SHAFT_RAD + 4;
ledRad = (LED_OUTER_RAD - LED_INNER_RAD)/2 + LED_INNER_RAD;

magnetRad = 2.5/2;
magnetDepth = 0.5;
maxDistance = 50;
magnetOffset = 2;

capThickness = .8;

wallThickness = 1.5;
wallDepth = 20;

// Determine if rings will be snaked or not
function isSnake(row) = ( row == len(RING_GRID) - 1 ? true : RING_GRID[row] % 2 != RING_GRID[row+1] % 2 && isSnake(row+1));

// Functions to compute height based on layout of rings
boxHeight = function (x) RING_GAP * (x + 1) + RING_RAD * (x * 2 + 1);
snakeHeight = function (x) x * (2 * RING_RAD + RING_GAP) * sin(60) + RING_GAP + RING_RAD;
rowHeightFunc = isSnake(0) ? snakeHeight : boxHeight;

length = (RING_GAP + RING_RAD * 2) * max(RING_GRID) + RING_GAP;
height = rowHeightFunc(len(RING_GRID) - 1) + RING_GAP + RING_RAD;

function generateArray(array, index, movingIndex) = index == movingIndex ? array[index]/2 : array[index];
function arrayShift(array, index, movingIndex, shiftValue) = index == movingIndex ? array[index] + shiftValue : array[index];

module CutMagnetHoles(translationArray, movingIndex, oppositeDistance, fixedIndex, offset = 0) {
  if (movingIndex < len(translationArray)) {
    if (translationArray[movingIndex] > maxDistance) {
      movementArray = [for (ind = [0:len(translationArray)-1])arrayShift(translationArray, ind, movingIndex, offset)];
      oppositeArray = [for (ind = [0:len(movementArray)-1])arrayShift(movementArray, ind, fixedIndex, oppositeDistance)];
      translate(movementArray) {
        cylinder(magnetDepth, magnetRad, magnetRad);
      }
      translate(oppositeArray) {
        cylinder(magnetDepth, magnetRad, magnetRad);
      }
      newArray = [for (ind = [0:len(movementArray)-1])generateArray(translationArray, ind, movingIndex)];
      CutMagnetHoles(newArray, movingIndex, oppositeDistance, fixedIndex, offset);
      CutMagnetHoles(newArray, movingIndex, oppositeDistance, fixedIndex, offset + translationArray[movingIndex]);
    }
  }
}

module CreateRingStructure() {
  for (row = [0: len(RING_GRID) - 1]) {    
    rowHeight = rowHeightFunc(row);
    translate([0, rowHeight, 0]){
      for (col = [0: RING_GRID[row] - 1]) {
        colWidth = RING_GAP * (col + 1) + RING_RAD * (col * 2 + 1);
        colOffset = (max(RING_GRID) - RING_GRID[row]) * (RING_GAP + RING_RAD * 2);
        translate([colWidth + colOffset/2, 0, 0]) {
          for(i=[0:1:$children-1]) {
            children(i);
          }
        }
      }
    }
  }
}

module CreateRingOfLeds() {
  for (ledNum = [0:MAX_LEDS-1]) {
    translate([(ledRad)*cos(ledNum*(360/MAX_LEDS)),(ledRad)*sin(ledNum*(360/MAX_LEDS)),0]) {
      rotate((360/MAX_LEDS) * ledNum) {
        cube(LED_SIZE, true);
      }
    }
  }
}

module CreateRingWireHoles() {
  for (ledNum = [0:MAX_LEDS-1]) {
    translate([(ledRad)*cos(ledNum*(360/MAX_LEDS)),(ledRad)*sin(ledNum*(360/MAX_LEDS)),0]) {
      rotate((360/MAX_LEDS) * ledNum) {
        i = 0;
        if (ledNum == i || ledNum == i + 2 || ledNum == i + 6 || ledNum == i + 8) {
          translate([1.5, 4.5, 0]) {
            cylinder(LED_THICKNESS, 1, 1);
          }
        }
      }
    }
  }
}

module CreateWalls() {
  difference() {
    color("red") {
      translate([0, -wallThickness, 0]) {
        cube([length, wallThickness, wallDepth]);
      }
      translate([0, height, 0]) {
        cube([length, wallThickness, wallDepth]);
      }
      translate([-wallThickness, -wallThickness, 0]) {
        cube([wallThickness, height + (2 * wallThickness), wallDepth]);
      }
      translate([length, -wallThickness, 0]) {
        cube([wallThickness, height + (2 * wallThickness), (wallDepth - LED_THICKNESS)]);
      }
    }
    translate([0, 0, wallDepth-LED_THICKNESS]) {
      CreateBacker();
    }
  }
}

module CreateBacker() {
  color("green") {
    // cube([length, height, LED_THICKNESS]);
    // linear_extrude(LED_THICKNESS, scale=1.025) {
    //   translate()
    //   square([length, height]);
    // }
    intersection() {
      hull() {
        translate([0, 0, 0]) {
          cylinder(d1=wallThickness,d2=.25, h=LED_THICKNESS, center=true);
        }
        translate([0, height, 0]) {
          cylinder(d1=wallThickness,d2=.25, h=LED_THICKNESS, center=true);
        }
        translate([length, 0, 0]) {
          cylinder(d1=wallThickness,d2=.25, h=LED_THICKNESS, center=true);
        } 
        translate([length, height, 0]){
          cylinder(d1=wallThickness,d2=.25, h=LED_THICKNESS, center=true);
        }
      }
      translate([0, -wallThickness/2, 0]) {
        cube([length, (height + wallThickness), LED_THICKNESS]);
      }
    }
  }
}

// Front panel
union() {
  difference() {
    cube([length, height, LED_THICKNESS]);
    // Magnet Hole Cutouts
    CutMagnetHoles([magnetOffset, height/2, 0], 1, length - (2 * magnetOffset), 0);
    CutMagnetHoles([length/2, magnetOffset, 0], 0, height - (2 * magnetOffset), 1);
    translate([magnetOffset, magnetOffset, 0]) {
      cylinder(magnetDepth, magnetRad, magnetRad);
    }
    translate([length - magnetOffset, height - magnetOffset, 0]) {
      cylinder(magnetDepth, magnetRad, magnetRad);
    }
    translate([length - magnetOffset, magnetOffset, 0]) {
      cylinder(magnetDepth, magnetRad, magnetRad);
    }
    translate([magnetOffset, height - magnetOffset, 0]) {
      cylinder(magnetDepth, magnetRad, magnetRad);
    }

    // LED Ring Cutouts
    CreateRingStructure() {
      cylinder(LED_THICKNESS, POTENTIOMETER_SHAFT_RAD, POTENTIOMETER_SHAFT_RAD);
      CreateRingOfLeds();
    }
  }
  
  // Potentiometer support
  CreateRingStructure() {
    difference() {
      metric_thread (diameter=potentiometerSupportRad * 2 - .25, pitch=1, length=POTENTIOMETER_KNOB_OFFSET, internal=false, square=true);
      cylinder(POTENTIOMETER_KNOB_OFFSET, POTENTIOMETER_SHAFT_RAD, POTENTIOMETER_SHAFT_RAD);
      translate([potentiometerSupportRad - 1.5, 0, POTENTIOMETER_KNOB_OFFSET]) {
        cube([1, 2.5, 1.5], true);
      }
    }
  }
}
CreateWalls();
// LED Rings
//translate([0,0,LED_THICKNESS]) {
//  color("blue"){
//    difference() {
//      CreateRingStructure() {
//        difference() {
          //cylinder(LED_THICKNESS, RING_RAD, RING_RAD);
          //cylinder(LED_THICKNESS, LED_INNER_RAD, LED_INNER_RAD);
//        }
 //     }

//      CreateRingStructure() {
        //CreateRingOfLeds();
        //CreateRingWireHoles();
//      }
//    }
//  }
//}

// LED cap to hold LED in place
rotate([0,180,0]){
  translate ([0,0,-LED_THICKNESS -capThickness]) {
    color("orange") {
      CreateRingStructure() {
        difference() {
          union() {
            cylinder(LED_THICKNESS, LED_INNER_RAD, LED_INNER_RAD);
            
            translate([0, 0, LED_THICKNESS]) {
              cylinder(capThickness, ledRad, ledRad);
            }
          }
          metric_thread (diameter=potentiometerSupportRad * 2 + .25, pitch=1, length=POTENTIOMETER_KNOB_OFFSET, internal=true, square=true);
        }
      }
    }
  }
}

//Backer to hide all of our messy wiring
translate([0, -(height + height/2), 0]) {
  CreateBacker();
}