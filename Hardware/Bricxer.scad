RING_RAD = 36.8 / 2;
RING_GAP = 2.2;
RING_GRID = [3,2];
MAX_LEDS = 12;
LED_SIZE = 5;
LED_THICKNESS = 1.6;
LED_OUTER_RAD = 34.33 / 2;
LED_INNER_RAD = 24.55 / 2;

ledRad = (LED_OUTER_RAD - LED_INNER_RAD)/2 + LED_INNER_RAD;

// Determine if rings will be snaked or not
function isSnake(row) = ( row == len(RING_GRID) - 1 ? true : RING_GRID[row] % 2 != RING_GRID[row+1] % 2 && isSnake(row+1));

// Functions to compute height based on layout of rings
boxHeight = function (x) RING_GAP * (x + 1) + RING_RAD * (x * 2 + 1);
snakeHeight = function (x) x * (2 * RING_RAD + RING_GAP) * sin(60) + RING_GAP + RING_RAD;
rowHeightFunc = isSnake(0) ? snakeHeight : boxHeight;

length = (RING_GAP + RING_RAD * 2) * max(RING_GRID) + RING_GAP;
height = rowHeightFunc(len(RING_GRID) - 1) + RING_GAP + RING_RAD;

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

// Front panel
union() {
  difference() {
    cube([length, height, LED_THICKNESS]);
    
    // LED Ring Cutouts
    CreateRingStructure() {
      for (ledNum = [0:MAX_LEDS-1]) {
        translate([(ledRad)*cos(ledNum*(360/MAX_LEDS)),(ledRad)*sin(ledNum*(360/MAX_LEDS)),0]) {
          rotate((360/MAX_LEDS) * ledNum){
            cube(LED_SIZE, true);
          }
        }
      }
    }
  }
}
