# Madeira trip assets (map + PR trails)

## Quick start
- Open `index.html` for a simple landing page (map + itinerary + downloads).
- Open `madeira_map.html` in your browser for the full-screen interactive map (PR trailheads + trail ends + key POIs + straight “start→end” lines).
- Import `data/madeira_map_full.kml` into Google My Maps if you want it on your phone in Google Maps (PR + POIs).
- Import `data/madeira_pr_trails.kml` if you only want the PR trail pins/lines.
- Import `data/madeira_pr_trails.geojson` into apps that accept GeoJSON (OsmAnd/Organic Maps/etc).
- `data/madeira_pois.geojson` contains additional “hub/viewpoint/garden/town” pins used by the map.

## Notes / limitations
- The PR trail coordinates are extracted from official IFCN “painéis informativos” images via OCR. They’re good enough for trip planning, but always verify trailhead parking/signage on arrival.
- Some PR panels cover multiple sub-routes; the map pins are best treated as *trailhead/endpoint anchors*, not the exact full path.
- The “route line” is just a straight line from start→end (not the actual trail geometry).

## Official reference maps
- `data/ifcn_maps/ifcn_pr_map.jpg` is the official overview map of classified walking routes.
- `data/ifcn_maps/ifcn_rabacal_map.jpg` is the official Rabaçal/Risco/25 Fontes area map.
