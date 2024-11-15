"use strict";

/*
  Outputs a bang when it becomes visible. Only passes on incoming bangs when visible.

  Note that to be visible for a device in presentation mode, this object must be included in presentation.
*/

mgraphics.init()

function paint() {
  outlet(0, "bang")
}

function bang() {
  mgraphics.redraw()
}
