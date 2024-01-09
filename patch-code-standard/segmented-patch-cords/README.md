# Segmented patch cords

Reasons **not** to use segmented patch cords for most connections:
1. Segmented patch cords create an extra barrier to refactor/re-layout a patch: you have to re-layout the patch cords every time you move an object
2. With perpendicular intersections, it is harder to see which segments belong to which cord
3. With regular patch cords, it is more apparent when a patch needs a better layout, simplification or encapsulation
4. When you only use segmented patch cords when lines go back up to "earlier" objects in the patch, this makes it easier to distinguish feedback-ish connections.

We do use a segmented patch cord when feeding back to an earlier point in the patch or occasionally if a connection needs to go from one far end of a patch to another, if there is no way to avoid that.