#!/usr/bin/env python3
"""
Build madeira_data.json from markdown guides + GeoJSON.
Run: python3 build_data.py
Output: data/madeira_data.json
"""
import json
import re
import os

def slug(name):
    s = name.lower()
    s = re.sub(r'[àáâãäå]', 'a', s)
    s = re.sub(r'[èéêë]', 'e', s)
    s = re.sub(r'[ìíîï]', 'i', s)
    s = re.sub(r'[òóôõö]', 'o', s)
    s = re.sub(r'[ùúûü]', 'u', s)
    s = re.sub(r'[ç]', 'c', s)
    s = re.sub(r'[ñ]', 'n', s)
    s = re.sub(r'[^a-z0-9\s-]', '', s)
    s = re.sub(r'[\s]+', '-', s).strip('-')
    s = re.sub(r'-+', '-', s)
    return s

def maps_url(lat, lng):
    return f"https://www.google.com/maps/search/?api=1&query={lat},{lng}"

def item(name, lat, lng, kind, region, tip, **kwargs):
    d = {
        "id": slug(name),
        "name": name,
        "lat": lat,
        "lng": lng,
        "kind": kind,
        "region": region,
        "tip": tip,
        "google_maps_url": maps_url(lat, lng),
        "image_url": None,
        "image_credit": None,
    }
    d.update(kwargs)
    return d

items = []

# ============================================================
# TRAILS
# ============================================================

items.append(item(
    "PR1 - Vereda do Areeiro", 32.7403, -16.9287, "trail", "Central Mountains",
    "Madeira's #1 hike: Pico do Arieiro to Pico Ruivo. Currently closed (reopening Apr 2026). First 1.2km to Stairway to Heaven still accessible.",
    code="PR1", difficulty="Hard", distance_km=7.0, elevation_m=790,
    time_hours="3.5-5.5", rating=4.7, review_count=4000, rating_source="AllTrails",
    fee_eur=10.50, tunnels=5, headlamp=True, status="closed", trail_type="vereda"
))

items.append(item(
    "PR1.2 - Vereda do Pico Ruivo", 32.7653, -16.9209, "trail", "Central Mountains",
    "Only way to summit Pico Ruivo (1862m) while PR1 is closed. Well-maintained stone path. Arrive early, parking fills by 9:30am.",
    code="PR1.2", difficulty="Moderate", distance_km=5.6, elevation_m=370,
    time_hours="1.5-3", rating=4.6, review_count=4077, rating_source="AllTrails",
    fee_eur=4.50, tunnels=0, headlamp=False, status="open", trail_type="vereda"
))

items.append(item(
    "PR6 - Levada das 25 Fontes", 32.762, -17.068, "trail", "West & Southwest",
    "Iconic levada to 25-spring waterfall pool. 800m pitch-black tunnel. Shuttle from ER105 car park (EUR 3 down, EUR 2 up). Combine with PR6.1.",
    code="PR6", difficulty="Moderate", distance_km=9.0, elevation_m=300,
    time_hours="3-4", rating=4.5, review_count=3225, rating_source="AllTrails",
    fee_eur=4.50, tunnels=1, headlamp=True, status="open", trail_type="levada"
))

items.append(item(
    "PR6.1 - Levada do Risco", 32.762, -17.068, "trail", "West & Southwest",
    "Easiest trail: flat walk to Madeira's tallest waterfall (100m). Perfect add-on to PR6 from same Rabacal trailhead.",
    code="PR6.1", difficulty="Easy", distance_km=3.0, elevation_m=50,
    time_hours="1-2", rating=4.4, review_count=543, rating_source="AllTrails",
    fee_eur=4.50, tunnels=0, headlamp=False, status="open", trail_type="levada"
))

items.append(item(
    "PR8 - Vereda da Ponta de Sao Lourenco", 32.7493, -16.7066, "trail", "East",
    "Highest-rated trail on AllTrails. Volcanic lunar landscape, no shade. Very windy. Bring 2L+ water. Cafe at Casa do Sardinha mid-trail.",
    code="PR8", difficulty="Moderate", distance_km=7.4, elevation_m=412,
    time_hours="2.5-4", rating=4.7, review_count=6999, rating_source="AllTrails",
    fee_eur=4.50, tunnels=0, headlamp=False, status="open", trail_type="vereda"
))

items.append(item(
    "PR9 - Levada do Caldeirao Verde", 32.7828, -16.9116, "trail", "East",
    "17.4km round trip to Green Cauldron waterfall. 4 tunnels with ankle-deep water. Full-day commitment. Spare socks essential.",
    code="PR9", difficulty="Moderate", distance_km=17.4, elevation_m=100,
    time_hours="5-7", rating=4.6, review_count=4214, rating_source="AllTrails",
    fee_eur=4.50, tunnels=4, headlamp=True, status="open", trail_type="levada"
))

items.append(item(
    "PR10 - Levada do Furado", 32.7396, -16.8869, "trail", "East",
    "11km forest levada from Ribeiro Frio to Portela. Currently closed due to landslide. One of few trails accessible by public bus (Bus 56).",
    code="PR10", difficulty="Easy", distance_km=11.0, elevation_m=200,
    time_hours="4-6", rating=4.3, review_count=676, rating_source="AllTrails",
    fee_eur=4.50, tunnels=3, headlamp=False, status="closed", trail_type="levada"
))

items.append(item(
    "PR11 - Vereda dos Balcoes", 32.7355, -16.8864, "trail", "East",
    "Shortest trail: flat 1.5km walk to iconic mountain viewpoint. Endemic Madeiran chaffinches feed from hands. Best effort-to-reward ratio.",
    code="PR11", difficulty="Easy", distance_km=3.0, elevation_m=60,
    time_hours="1-1.5", rating=4.3, review_count=2506, rating_source="AllTrails",
    fee_eur=4.50, tunnels=0, headlamp=False, status="open", trail_type="vereda"
))

items.append(item(
    "PR13 - Vereda do Fanal", 32.815, -17.152, "trail", "West & Southwest",
    "Remote trail to 600-year-old twisted trees. Best in FOG. Most visitors drive directly to Fanal instead of full 10.8km hike.",
    code="PR13", difficulty="Hard", distance_km=10.8, elevation_m=500,
    time_hours="4-5", rating=4.4, review_count=1502, rating_source="AllTrails",
    fee_eur=4.50, tunnels=0, headlamp=False, status="open", trail_type="vereda"
))

items.append(item(
    "PR17 - Caminho do Pinaculo e Folhadal", 32.754, -17.019, "trail", "Central Mountains",
    "Adventure hiker's trail. Two mega tunnels (500m + 1km) with ankle-deep water. Hardest tunnels on any Madeira trail. Partially open.",
    code="PR17", difficulty="Hard", distance_km=15.0, elevation_m=520,
    time_hours="6-7", rating=4.5, review_count=218, rating_source="AllTrails",
    fee_eur=4.50, tunnels=5, headlamp=True, status="partial", trail_type="levada"
))

items.append(item(
    "PR18 - Levada do Rei", 32.804, -16.870, "trail", "East",
    "Peaceful, easy levada to pristine Ribeiro Bonito stream. Low crowds. Hidden gem among experienced hikers. Combine with Santana visit.",
    code="PR18", difficulty="Easy", distance_km=10.2, elevation_m=150,
    time_hours="3-4", rating=4.4, review_count=1361, rating_source="AllTrails",
    fee_eur=4.50, tunnels=1, headlamp=False, status="open", trail_type="levada"
))

# ============================================================
# VIEWPOINTS (33 total)
# ============================================================

# Tier 1 (1-10)
items.append(item(
    "Cabo Girao Skywalk", 32.656658, -17.004539, "viewpoint", "Funchal & South",
    "580m glass-bottom platform over Europe's highest sea cliff. Go early morning or after 4pm to avoid tour bus crowds.",
    worth_it=10, best_time="Early morning (08:30-10:00) or late afternoon", altitude_m=580, entry_fee="EUR 2-5"
))

items.append(item(
    "Eira do Serrado", 32.710430, -16.965680, "viewpoint", "Funchal & South",
    "Iconic crater-like view over Valley of the Nuns. 25 min from Funchal. Check visibility first -- fog can ruin it.",
    worth_it=9, best_time="Morning for clarity", altitude_m=1095, entry_fee="Free"
))

items.append(item(
    "Pico do Arieiro", 32.740251, -16.942484, "viewpoint", "Central Mountains",
    "1818m, 3rd highest peak. SUNRISE above clouds is legendary. Near-freezing at dawn. Drive right up. PR1 start.",
    worth_it=10, best_time="Sunrise", altitude_m=1818, entry_fee="Free (parking EUR 2-4/h)"
))

items.append(item(
    "Miradouro dos Balcoes", 32.741590, -16.890350, "viewpoint", "East",
    "Best effort-to-reward viewpoint on the island. Easy 30min walk from Ribeiro Frio. Central peaks panorama. Endemic firecrests.",
    worth_it=9, best_time="Morning for clear skies", altitude_m=870, entry_fee="EUR 3 (IFCN)"
))

items.append(item(
    "Miradouro da Portela", 32.782, -16.833, "viewpoint", "East",
    "Dramatic view of Penha d'Aguia rock and Porto da Cruz. Mystical when clouds pass through. Only 4 parking spaces.",
    worth_it=8, best_time="Morning or late afternoon", altitude_m=670, entry_fee="Free"
))

items.append(item(
    "Miradouro do Veu da Noiva", 32.816096, -17.095091, "viewpoint", "North Coast",
    "Iconic Bridal Veil waterfall cascading from cliff into the sea. Quick photo stop en route to Porto Moniz. Best after rain.",
    worth_it=8, best_time="After rain", altitude_m=90, entry_fee="Free"
))

items.append(item(
    "Miradouro das Cabanas", 32.815, -16.870, "viewpoint", "North Coast",
    "One of the best sunset viewpoints on the island. Northwest coast panorama over Arco de Sao Jorge.",
    worth_it=8, best_time="Sunset", altitude_m=500, entry_fee="Free"
))

items.append(item(
    "Miradouro do Guindaste", 32.793912, -16.848435, "viewpoint", "East",
    "Sea-level glass walkways 26m over the ocean. Unique low-angle perspective with Penha d'Aguia rock. Free.",
    worth_it=8, best_time="Sunrise", altitude_m=20, entry_fee="Free"
))

items.append(item(
    "Miradouro da Ribeira da Janela", 32.844799, -17.150571, "viewpoint", "North Coast",
    "Views over rock formations with 'window' hole rising from the ocean. Facilities, parking, playground. Combine with sea-level visit.",
    worth_it=7, best_time="Any time", altitude_m=390, entry_fee="Free"
))

items.append(item(
    "Ponta do Rosto", 32.749275, -16.706601, "viewpoint", "East",
    "Volcanic dragon tail peninsula. Both north and south coasts visible. Colorful volcanic cliffs. Feels like another planet. PR8 start.",
    worth_it=9, best_time="Morning light", altitude_m=130, entry_fee="Free"
))

# Tier 2 (11-20)
items.append(item(
    "Miradouro da Encumeada", 32.754, -17.019, "viewpoint", "Central Mountains",
    "Two-sided views: north to Sao Vicente, south to Serra de Agua. Rare cloud waterfall phenomenon. Often fogged by midday.",
    worth_it=7, best_time="Early morning", altitude_m=1007, entry_fee="Free"
))

items.append(item(
    "Miradouro do Paredao", 32.716081, -16.955487, "viewpoint", "Funchal & South",
    "Higher angle on Nun's Valley than Eira do Serrado. Less known, fewer crowds.",
    worth_it=7, best_time="Morning", altitude_m=1430, entry_fee="Free"
))

items.append(item(
    "Miradouro do Cortado", 32.800, -16.855, "viewpoint", "East",
    "Dramatic cliff angles of Penha d'Aguia (590m), Faial promontory, and Ponta de Sao Lourenco in distance.",
    worth_it=7, best_time="Any time", altitude_m=400, entry_fee="Free"
))

items.append(item(
    "Miradouro da Torre", 32.650, -16.975, "viewpoint", "Funchal & South",
    "Charming view of Camara de Lobos fishing village with colorful boats. Churchill painted this view.",
    worth_it=7, best_time="Golden hour (sunset)", altitude_m=30, entry_fee="Free"
))

items.append(item(
    "Miradouro de Sao Cristovao Boaventura", 32.830, -16.930, "viewpoint", "North Coast",
    "Impressive cliff formation meeting the sea from unusually low vantage point. Unique perspective.",
    worth_it=7, best_time="Any time", altitude_m=50, entry_fee="Free"
))

items.append(item(
    "Miradouro Francisco Alvares Nobrega", 32.720, -16.765, "viewpoint", "East",
    "Best town views on Madeira: Machico valley, golden sand beach, marina, peninsula.",
    worth_it=7, best_time="Any time", altitude_m=100, entry_fee="Free"
))

items.append(item(
    "Miradouro da Faja da Ovelha", 32.770, -17.237, "viewpoint", "West & Southwest",
    "Remote west coast feel. Paul do Mar village far below with plantations, cliffs, green terraces.",
    worth_it=7, best_time="Any time", altitude_m=400, entry_fee="Free"
))

items.append(item(
    "Rocha do Navio", 32.825, -16.865, "viewpoint", "East",
    "Cliffs, green farms, waterfalls plunging into ocean. Cable car currently closed. Spectacular even without descending.",
    worth_it=7, best_time="Any time", altitude_m=200, entry_fee="Free"
))

items.append(item(
    "Pico Ruivo do Paul", 32.777009, -17.079965, "viewpoint", "Central Mountains",
    "1640m peak. Paul da Serra plateau and Sao Vicente valley panorama. Quieter than Pico do Arieiro.",
    worth_it=7, best_time="Morning", altitude_m=1640, entry_fee="Free"
))

items.append(item(
    "Bica da Cana", 32.762, -17.068, "viewpoint", "Central Mountains",
    "1560m. Alternative sunrise spot on Paul da Serra. Panoramic views to Arieiro and Ruivo. Empty parking.",
    worth_it=7, best_time="Sunrise", altitude_m=1560, entry_fee="Free"
))

# Tier 3 (21-33)
items.append(item(
    "Miradouro de Terra Grande", 32.690, -17.035, "viewpoint", "Funchal & South",
    "180-degree view of valleys and terraced plantations on south coast near Ribeira Brava. Easy roadside stop.",
    worth_it=6, best_time="Any time", altitude_m=720, entry_fee="Free"
))

items.append(item(
    "Miradouro do Fio", 32.780, -17.240, "viewpoint", "West & Southwest",
    "Southwest tip cliffs, pebble beaches, sea. Tea house nearby.",
    worth_it=6, best_time="Any time", altitude_m=300, entry_fee="Free"
))

items.append(item(
    "Miradouro da Santinha", 32.870, -17.180, "viewpoint", "North Coast",
    "Porto Moniz from above, vineyards, island panorama. Mountain road above town.",
    worth_it=6, best_time="Any time", altitude_m=200, entry_fee="Free"
))

items.append(item(
    "Miradouro do Cabouco", 32.760, -16.890, "viewpoint", "Central Mountains",
    "Valley views with summits on road to Pico do Arieiro. Off beaten path.",
    worth_it=6, best_time="Any time", altitude_m=600, entry_fee="Free"
))

items.append(item(
    "Paul do Mar Viewpoint", 32.754092, -17.226941, "viewpoint", "West & Southwest",
    "Isolated village at cliff base, sea and waves. Quiet, away from crowds.",
    worth_it=6, best_time="Any time", altitude_m=10, entry_fee="Free"
))

items.append(item(
    "Raposeira", 32.759183, -17.223215, "viewpoint", "West & Southwest",
    "Paul do Mar from above. 10-min dirt trail from parking.",
    worth_it=6, best_time="Any time", altitude_m=510, entry_fee="Free"
))

items.append(item(
    "Miradouro Ponta da Ladeira", 32.859433, -17.203731, "viewpoint", "West & Southwest",
    "Coast view and Faja da Quebrada Nova. Near Achadas da Cruz cable car.",
    worth_it=6, best_time="Any time", altitude_m=360, entry_fee="Free"
))

items.append(item(
    "Lombo do Mouro", 32.747435, -17.041146, "viewpoint", "Central Mountains",
    "Sao Vicente valley and Pico Arieiro views along ER 110 mountain road.",
    worth_it=6, best_time="Any time", altitude_m=1290, entry_fee="Free"
))

items.append(item(
    "Miradouro de Boa Morte", 32.795, -17.250, "viewpoint", "West & Southwest",
    "Near Ponta do Pargo lighthouse. 180-degree ocean sunsets. 5-min descent walk.",
    worth_it=6, best_time="Sunset", altitude_m=400, entry_fee="Free"
))

items.append(item(
    "Ponta do Tristao", 32.870, -17.195, "viewpoint", "North Coast",
    "Northernmost point of Madeira. Off-beaten-path sunset. 5-min dirt path.",
    worth_it=6, best_time="Sunset", altitude_m=50, entry_fee="Free"
))

items.append(item(
    "Pinaculo", 32.665, -16.910, "viewpoint", "Funchal & South",
    "Best vantage point of Funchal city. Sunset location. Accessible by public bus.",
    worth_it=6, best_time="Sunset", altitude_m=500, entry_fee="Free"
))

items.append(item(
    "Ponta do Sol Harbor Viewpoint", 32.680, -17.100, "viewpoint", "West & Southwest",
    "Harbor and sunset views with beach restaurants. Warm microclimate.",
    worth_it=6, best_time="Sunset", altitude_m=10, entry_fee="Free"
))

items.append(item(
    "Fanal", 32.815211, -17.152339, "viewpoint", "West & Southwest",
    "Ancient Laurissilva forest with 600-year-old twisted trees. Atmospheric in fog, not a panoramic viewpoint.",
    worth_it=7, best_time="Early morning or fog", altitude_m=1160, entry_fee="Free"
))

# Extra viewpoints from GeoJSON not in viewpoints MD
items.append(item(
    "Cristo Rei Garajau", 32.6386, -16.8507, "viewpoint", "Funchal & South",
    "Christ statue viewpoint with ocean panorama.",
    worth_it=6, best_time="Any time", altitude_m=200, entry_fee="Free"
))

items.append(item(
    "Ponta do Pargo Lighthouse", 32.8139, -17.2631, "viewpoint", "West & Southwest",
    "Westernmost point of Madeira. Sweeping 180-degree sunset views. Garganta Funda waterfall nearby.",
    worth_it=7, best_time="Sunset", altitude_m=300, entry_fee="Free"
))

# ============================================================
# SWIMMING SPOTS (13 total)
# ============================================================

items.append(item(
    "Porto Moniz Natural Pools (Paid)", 32.866601, -17.175722, "swim", "North Coast",
    "Classic Madeira swim. EUR 3. Lifeguards, changing rooms, children's pool. 3800m2 volcanic lava pools. Can close in storms.",
    swim_type="natural-pool", entry_fee="EUR 3"
))

items.append(item(
    "Porto Moniz Cachalote Pools (Free)", 32.867, -17.174, "swim", "North Coast",
    "Free rugged volcanic pools near the Aquarium. No lifeguard, no changing rooms. More authentic, confident swimmers only.",
    swim_type="natural-pool", entry_fee="Free"
))

items.append(item(
    "Seixal Natural Pools", 32.815, -17.100, "swim", "North Coast",
    "FREE volcanic pools with stunning lava arch. Arguably more beautiful than Porto Moniz. No lifeguards. Steep 33% access road.",
    swim_type="natural-pool", entry_fee="Free"
))

items.append(item(
    "Doca do Cavacas", 32.635, -16.945, "swim", "Funchal & South",
    "EUR 6 managed volcanic pools between Lido and Praia Formosa. Snorkeling, restaurant, south coast = calmer. Crystal clear.",
    swim_type="natural-pool", entry_fee="EUR 6"
))

items.append(item(
    "Calheta Golden Sand Beach", 32.720, -17.170, "beach", "West & Southwest",
    "Best traditional beach on Madeira. Imported golden sand from Morocco. Calm sheltered water, family-friendly. Free. Warm microclimate.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Machico Golden Sand Beach", 32.720, -16.765, "beach", "East",
    "Imported golden sand in sheltered bay. Full facilities, water sports. Good for arrival/departure day near airport. Free.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Seixal Black Sand Beach", 32.815, -17.103, "beach", "North Coast",
    "Natural black volcanic sand against green cliffs. 'Jamaica Beach' on Instagram. Photography 10/10, swimming risky in March.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Praia Formosa", 32.638, -16.940, "beach", "Funchal & South",
    "Largest public beach (2km). Pebble/dark sand. Blue Flag. Promenade to Camara de Lobos. 10 min from Funchal centre. Free.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Prainha", 32.738, -16.710, "beach", "East",
    "Madeira's ONLY natural sandy beach. Volcanic black sand in sheltered cove. Calm, clear water. Unique arid landscape. Free.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Porto da Cruz Beach", 32.785, -16.835, "beach", "East",
    "Black pebble beach with best surf on Madeira. Penha d'Aguia backdrop. Not ideal for calm swimming. Wetsuits essential.",
    swim_type="beach", entry_fee="Free"
))

items.append(item(
    "Faja dos Padres", 32.658, -17.037, "swim", "Funchal & South",
    "Secluded pebble beach below 300m cliff. Cable car EUR 10-12 or boat from Camara de Lobos. Pristine turquoise water, restaurant.",
    swim_type="beach", entry_fee="EUR 10-12 (cable car)"
))

items.append(item(
    "Poco dos Chefes", 32.721, -16.966, "swim", "Funchal & South",
    "Natural freshwater swimming hole in Valley of the Nuns. Free. Too cold for March. Popular with locals in summer.",
    swim_type="natural-pool", entry_fee="Free"
))

items.append(item(
    "Praia dos Anjos", 32.640, -16.935, "beach", "Funchal & South",
    "Small pebble beach used by locals. Quiet, authentic, no tourists. Minimal facilities.",
    swim_type="beach", entry_fee="Free"
))

# ============================================================
# GARDENS (6 total)
# ============================================================

items.append(item(
    "Monte Palace Tropical Garden", 32.6742, -16.9029, "garden", "Funchal & South",
    "Madeira's #1 garden. EUR 15. Koi ponds, azulejo tiles, museum, wine tasting included. Cable car closed until Apr 2026 -- use taxi/bus.",
    entry_fee="EUR 15", hours="09:00-18:00 (winter) / 09:00-19:00 (summer)"
))

items.append(item(
    "Jardim Botanico da Madeira", 32.6620, -16.8955, "garden", "Funchal & South",
    "EUR 6. 2000+ exotic plants, bird park with parrots and macaws, Funchal views. Complementary to Monte Palace.",
    entry_fee="EUR 6", hours="09:00-17:00 (Oct-Apr) / 09:00-19:00 (May-Sep)"
))

items.append(item(
    "Palheiro Gardens", 32.6598, -16.8673, "garden", "Funchal & South",
    "EUR 11. CAMELLIAS IN PEAK BLOOM IN MARCH. English estate feel blended with subtropical plants. Best garden for March visit.",
    entry_fee="EUR 11", hours="09:00-17:00 daily"
))

items.append(item(
    "Jardim do Mar", 32.740, -17.215, "garden", "West & Southwest",
    "Not a formal garden -- car-free village nicknamed 'Garden of the Sea.' Subtropical flowers, narrow streets, surf spot. Free.",
    entry_fee="Free", hours="Always open (village)"
))

items.append(item(
    "Quinta da Boa Vista", 32.650, -16.910, "garden", "Funchal & South",
    "Best orchid collection on the island. EUR 5. Weekdays only (closed weekends). Small but exquisite. 1 hour visit.",
    entry_fee="EUR 5", hours="Mon-Fri 09:00-18:00"
))

items.append(item(
    "Santa Catarina Park", 32.647, -16.918, "garden", "Funchal & South",
    "Free public park. 36,000m2. Flower beds, Funchal and marina views, playground, cafe. Pleasant stroll, not destination-worthy alone.",
    entry_fee="Free", hours="Always open"
))

# ============================================================
# FUNCHAL RESTAURANTS
# ============================================================

# Fine Dining
items.append(item(
    "Il Gallo d'Oro", 32.637, -16.940, "restaurant", "Funchal & South",
    "Only 2 Michelin stars on Madeira. EUR 245-295 tasting menus. Reserve well in advance. Dress code enforced.",
    cuisine="Fine Dining / French-Portuguese", price_range="€€€", must_order="Terroir Experience tasting menu"
))

items.append(item(
    "Desarma", 32.645, -16.912, "restaurant", "Funchal & South",
    "1 Michelin star. 11th-floor panoramic views over Funchal. Creative concept dining with tasting menus EUR 175-275.",
    cuisine="Modern Madeiran", price_range="€€€", must_order="The Chef's Battle tasting menu"
))

items.append(item(
    "William Restaurant", 32.638, -16.938, "restaurant", "Funchal & South",
    "1 Michelin star at Reid's Palace. EUR 105-160. Pair with afternoon tea at Reid's (EUR 30pp). Romantic Atlantic views.",
    cuisine="Refined Portuguese", price_range="€€€", must_order="Discovery tasting menu"
))

items.append(item(
    "Joy Restaurant", 32.639, -16.935, "restaurant", "Funchal & South",
    "Newest fine dining entrant, next to Savoy Palace. Contemporary tasting menus. Stylish modern design. Opened late 2024.",
    cuisine="Contemporary Fine Dining", price_range="€€€", must_order="Seasonal tasting menu"
))

# Mid-Range / Bistronomic
items.append(item(
    "Avista", 32.637, -16.940, "restaurant", "Funchal & South",
    "Bib Gourmand. Same chef as Il Gallo d'Oro at fraction of price. EUR 25-70. Ocean terrace. Children's menu available.",
    cuisine="Mediterranean", price_range="€€", must_order="Algarve red shrimp shared plates"
))

items.append(item(
    "Casal da Penha", 32.644, -16.916, "restaurant", "Funchal & South",
    "Bib Gourmand. Cobbled lanes. Black scabbardfish filet, lamb chops. Wine cellar upstairs. EUR 20-60.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Black scabbardfish filet"
))

items.append(item(
    "Armazem do Sal", 32.648, -16.906, "restaurant", "Funchal & South",
    "Former medieval salt warehouse. Stone walls, wooden beams. Michelin-recommended. Shrimp risotto, soft-shell crab. EUR 25-80.",
    cuisine="Modern Madeiran", price_range="€€", must_order="Shrimp risotto, poncha cocktail"
))

items.append(item(
    "Tipografia", 32.650, -16.909, "restaurant", "Funchal & South",
    "Castanheiro Boutique Hotel. Revisited espada com banana with banana puree. Portuguese-Italian fusion. EUR 20-60.",
    cuisine="Portuguese-Mediterranean-Italian", price_range="€€", must_order="Revisited espada com banana"
))

items.append(item(
    "5 Sentidos", 32.648, -16.910, "restaurant", "Funchal & South",
    "Open kitchen. Small fresh menu that changes frequently. EUR 10 weekday lunch menu. Save for your last night.",
    cuisine="Creative Portuguese", price_range="€€", must_order="Parrotfish, chocolate tart with salted caramel"
))

items.append(item(
    "Kampo", 32.649, -16.908, "restaurant", "Funchal & South",
    "Open kitchen by Chef Julio Pereira. Contemporary seasonal menu. Perfect for special occasions. Inventive without pretension.",
    cuisine="Contemporary", price_range="€€€", must_order="White chocolate, olive, and passion fruit dessert"
))

items.append(item(
    "AKUA", 32.648, -16.906, "restaurant", "Funchal & South",
    "Fresh fish and shellfish from display window. Black shrimp, prawns, mussels, lobsters. Old Town alley. EUR 30-50.",
    cuisine="Seafood", price_range="€€", must_order="Day's catch from display window"
))

items.append(item(
    "La ao Fundo", 32.647, -16.905, "restaurant", "Funchal & South",
    "Madeiran staples with African and Indian twists. High-quality tuna and swordfish. Rustic stone walls, cosy atmosphere.",
    cuisine="Madeiran Fusion", price_range="€€", must_order="Tuna or swordfish"
))

items.append(item(
    "Goya", 32.637, -16.935, "restaurant", "Funchal & South",
    "Classical fine dining in hotel area/Lido. Exceptional passion fruit souffle. Prime choice for dates and celebrations.",
    cuisine="Fine Dining", price_range="€€€", must_order="Passion fruit souffle"
))

items.append(item(
    "Santa Maria Restaurant", 32.648, -16.905, "restaurant", "Funchal & South",
    "Old Town street-side terrace. Black pork cheek with truffle puree. Portuguese + sushi fusion. EUR 10-40.",
    cuisine="Portuguese-Japanese Fusion", price_range="€€", must_order="Black pork cheek with truffle puree"
))

items.append(item(
    "Taberna Madeira", 32.644, -16.908, "restaurant", "Funchal & South",
    "Zona Velha. Grilled limpets, milho frito, sweet potato bread couvert. Tapas-style. Reliable first-night dinner.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Grilled limpets (lapas), milho frito"
))

items.append(item(
    "Peixaria no Mercado", 32.649, -16.905, "restaurant", "Funchal & South",
    "Outdoor terrace overlooking market street. Cod croquettes with homemade tartar. Daily catch from market. EUR 20-40.",
    cuisine="Seafood", price_range="€€", must_order="Cod croquettes with homemade tartar sauce"
))

# Casual / Local Favorites
items.append(item(
    "Zarcos", 32.645, -16.920, "restaurant", "Funchal & South",
    "Always packed with locals. Enormous portions. Steaks, fish, milho frito, passion fruit mousse. Arrive hungry.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Steaks with milho frito"
))

items.append(item(
    "Rustikus", 32.648, -16.912, "restaurant", "Funchal & South",
    "EUR 6.90 daily lunch specials. Locals queue out the door. Menu changes daily. No-frills quality. Arrive early.",
    cuisine="Traditional Portuguese", price_range="€", must_order="Prato do dia (daily special)"
))

items.append(item(
    "A Tendinha", 32.647, -16.907, "restaurant", "Funchal & South",
    "Cash only. Daily whiteboard menu. Fresh, no-frills, truly Madeiran. Unbeatable value.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Daily whiteboard fish or meat"
))

items.append(item(
    "Snack Bar Bela 5", 32.647, -16.904, "restaurant", "Funchal & South",
    "Family-run Funchal institution. Quality homemade food. End-of-day discounts on unused food. Rock-bottom prices.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Daily specials"
))

items.append(item(
    "O Londres", 32.648, -16.911, "restaurant", "Funchal & South",
    "Canteen-like buzz with regulars. Tuna steaks, bacalhau a Bras, espetada. Daily pratos do dia. Skip the salmon.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Tuna steak with fried corn"
))

items.append(item(
    "Restaurante Dos Combatentes", 32.649, -16.910, "restaurant", "Funchal & South",
    "One of Funchal's oldest restaurants. Consistently good homemade food. Central location. Vegetarian options.",
    cuisine="Traditional Portuguese", price_range="€€", must_order="Fish dishes, stuffed vegetables"
))

items.append(item(
    "Ja Fui Jaquet", 32.647, -16.904, "restaurant", "Funchal & South",
    "On touristy Rua de Santa Maria but genuinely good value. EUR 12 four-course lunch. Fish pasta sharing pot at dinner.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Four-course lunch special"
))

items.append(item(
    "O Americano", 32.648, -16.905, "restaurant", "Funchal & South",
    "Tapas format for sampling multiple Madeiran dishes. House tuna with sweet potatoes and onions. EUR 10-30.",
    cuisine="Madeiran Tapas", price_range="€", must_order="House tuna with sweet potatoes"
))

items.append(item(
    "Barra Azul", 32.638, -16.940, "restaurant", "Funchal & South",
    "Right on Praia Formosa beach. Limpets, beef picados, octopus, espada with banana. Outdoor wooden seating.",
    cuisine="Seafood / Traditional", price_range="€€", must_order="Limpets, beef picados"
))

items.append(item(
    "A Bica", 32.647, -16.908, "restaurant", "Funchal & South",
    "Simple, traditional. The go-to for espada com banana and tuna steaks. Quality and freshness above all.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Espada com banana"
))

items.append(item(
    "Doca do Cavacas Restaurant", 32.635, -16.945, "restaurant", "Funchal & South",
    "By volcanic rock pools with Cabo Girao views. Red snapper highly recommended. Hidden gem location. EUR mid-range.",
    cuisine="Seafood", price_range="€€", must_order="Red snapper, espada com banana"
))

items.append(item(
    "Informal", 32.649, -16.908, "restaurant", "Funchal & South",
    "Modern Portuguese with East Asian influence. Ramen, yakisoba, tempura. Two daily vegetarian/vegan options.",
    cuisine="Portuguese-Asian Fusion", price_range="€€", must_order="Ramen, tempura vegetables"
))

items.append(item(
    "Sete Mares", 32.645, -16.910, "restaurant", "Funchal & South",
    "Two locations (Funchal port + Camara de Lobos). Nautical theme, harbor views. Tomato onion soup with poached egg.",
    cuisine="Seafood / Traditional", price_range="€€", must_order="Tomato onion soup with poached egg, prego no bolo do caco"
))

# ============================================================
# REGIONAL RESTAURANTS
# ============================================================

# Camara de Lobos / Estreito
items.append(item(
    "Restaurante Santo Antonio", 32.6555, -16.9555, "restaurant", "Funchal & South",
    "THE most famous espetada restaurant since 1966. Beef on bay laurel sticks. Family-run. Drive up through mountains is part of experience.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Espetada on laurel skewers, grilled chicken with milho frito"
))

items.append(item(
    "As Vides", 32.6560, -16.9580, "restaurant", "Funchal & South",
    "The FIRST restaurant to commercialize espetada (~1950). Traditional recipe with fried corn and potatoes. Budget-friendly.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Traditional espetada with fried corn"
))

items.append(item(
    "O Polar", 32.650, -16.975, "restaurant", "Funchal & South",
    "Beloved local institution in Camara de Lobos. Espetada, grilled chicken, homemade passion fruit pudding. Reservations recommended.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Espetada a Madeirense, passion fruit pudding"
))

items.append(item(
    "Vila da Carne", 32.650, -16.975, "restaurant", "Funchal & South",
    "Modern-yet-traditional in Camara de Lobos. Superior meat quality espetada. Traditional Madeiran recipe.",
    cuisine="Meat / Traditional", price_range="€€", must_order="Espetada, premium meats"
))

items.append(item(
    "O Lagar", 32.650, -16.975, "restaurant", "Funchal & South",
    "Former wine cellar in Camara de Lobos, family-run since 1995. Miniature Santana house at entrance. Fresh local produce.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Traditional Madeiran cuisine, espetada"
))

items.append(item(
    "Vila do Peixe", 32.650, -16.975, "restaurant", "Funchal & South",
    "Pick-your-fish concept in Camara de Lobos. Floor-to-ceiling bay views. Select from live counter. Reserve ahead on weekends.",
    cuisine="Seafood", price_range="€€", must_order="Day's catch -- tuna, sea bream, scabbardfish, grilled with salt"
))

items.append(item(
    "O Viola", 32.650, -16.977, "restaurant", "Funchal & South",
    "Warm and sophisticated near Camara de Lobos. Premium dry-aged meats. Ideal for special occasions.",
    cuisine="Meat / Premium", price_range="€€€", must_order="Dry-aged beef steaks (bifes)"
))

# Porto Moniz
items.append(item(
    "Restaurante Orca", 32.867, -17.175, "restaurant", "North Coast",
    "Terrace with ocean views next to natural pools. Tuna steak, spicy prawns, grilled limpets, prego no bolo do caco.",
    cuisine="Seafood / Traditional", price_range="€€", must_order="Bife de atum, gambas a diablo"
))

items.append(item(
    "Restaurante Polo Norte", 32.867, -17.177, "restaurant", "North Coast",
    "Inland Porto Moniz. Home-style cooking. Beef espetada, Portuguese wines. Friendly team. Ocean view terrace upstairs.",
    cuisine="Traditional Portuguese", price_range="€€", must_order="Beef espetada"
))

items.append(item(
    "Sea View Restaurante", 32.867, -17.176, "restaurant", "North Coast",
    "Hidden gem near natural pools. Fish soup, grilled tuna with unique vegetable sides.",
    cuisine="Seafood", price_range="€€", must_order="Fish soup, grilled tuna"
))

items.append(item(
    "Conchinha Bar", 32.867, -17.176, "restaurant", "North Coast",
    "Quieter lunchtime alternative in Porto Moniz center. Sandwiches, salads, soups, maracuja cheesecake.",
    cuisine="Cafe / Light Meals", price_range="€", must_order="Maracuja cheesecake"
))

# Santana
items.append(item(
    "Restaurante Quinta do Furao", 32.800, -16.880, "restaurant", "East",
    "Cliff-edge hotel restaurant. Oxtail tureen, slow-cooked beef cheek, mushroom risotto. Sea view. Summer terrace + winter fireplace.",
    cuisine="Modern Madeiran", price_range="€€", must_order="Oxtail tureen, slow-cooked beef cheek"
))

items.append(item(
    "Cantinho da Serra", 32.805, -16.882, "restaurant", "East",
    "Large fireplace, ideal for cooler days. Madeiran stew, carne de vinha d'alhos. Exclusively local products.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Madeiran stew, carne de vinha d'alhos"
))

items.append(item(
    "Marcel's Bistro", 32.805, -16.881, "restaurant", "East",
    "Relaxing vibe in Santana. Prawns, bacalhau, cocktails. Avoid O Colmo, Estrela do Norte at lunch (coach tour crowds).",
    cuisine="Bistro", price_range="€€", must_order="Prawns, bacalhau"
))

# Sao Vicente
items.append(item(
    "Quebramar", 32.802, -17.047, "restaurant", "North Coast",
    "Rotating upper floor with sea views in Sao Vicente. Non-rotating tables downstairs. Traditional pilgrimage soup.",
    cuisine="Traditional Portuguese", price_range="€€", must_order="Caldo da Romaria (pilgrimage soup)"
))

items.append(item(
    "Taberna de Sao Vicente", 32.802, -17.047, "restaurant", "North Coast",
    "Traditional Portuguese taberna atmosphere in Sao Vicente center. Bacalhau, bife espetada, milho fritas.",
    cuisine="Traditional Portuguese", price_range="€", must_order="Bacalhau, bife espetada"
))

items.append(item(
    "Restaurante Lavrador", 32.802, -17.048, "restaurant", "North Coast",
    "Cook-your-own beef/tuna on hot stone. Homemade bolo de mel. Family-run, mountain views. Book ahead for terrace.",
    cuisine="Interactive / Traditional", price_range="€€", must_order="Hot stone beef/tuna, bolo de mel"
))

items.append(item(
    "Brasa Viva", 32.802, -17.047, "restaurant", "North Coast",
    "Family-friendly in Sao Vicente. Tender, juicy, traditionally prepared espetada. Near Venda Nova poncha tavern.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Espetada"
))

# Calheta
items.append(item(
    "Fontes do Horacio", 32.722, -17.178, "restaurant", "West & Southwest",
    "Hidden gem in Estreito da Calheta. Among the best espetada on the island. Feels like someone's home. Features Bella the robot server.",
    cuisine="Traditional Madeiran", price_range="€€", must_order="Espetada, bife da casa"
))

items.append(item(
    "Restaurante Beira Mar", 32.720, -17.175, "restaurant", "West & Southwest",
    "Restaurant of choice for locals at Calheta marina. Polvo, grilled limpets, fish stew, homemade sangria. Relaxed vibe.",
    cuisine="Seafood / Traditional", price_range="€€", must_order="Polvo (octopus), grilled limpets"
))

items.append(item(
    "Leme Marisqueira", 32.720, -17.174, "restaurant", "West & Southwest",
    "Right on Calheta marina with ocean views. Varied seafood menu, Portuguese and Mediterranean dishes. Good wine selection.",
    cuisine="Seafood / Mediterranean", price_range="€€", must_order="Seafood platter"
))

items.append(item(
    "Restaurante O Farolim", 32.720, -17.173, "restaurant", "West & Southwest",
    "Stunning Atlantic views in Calheta. Specializes in grilled seafood. Limpets, tuna steaks, scabbardfish with banana.",
    cuisine="Grilled Seafood", price_range="€€", must_order="Grilled limpets, tuna steaks"
))

# Machico
items.append(item(
    "O Forno", 32.722, -16.765, "restaurant", "East",
    "Garlic prawns, beef espetada. Massive portions, tiny prices. Packed with locals weekends. Free ginja cherry liqueur.",
    cuisine="Traditional Madeiran", price_range="€", must_order="Garlic prawns, beef espetada"
))

items.append(item(
    "Restaurante Mercado Velho", 32.720, -16.766, "restaurant", "East",
    "Charming traditional Portuguese in Machico. Mussels, shrimp and sauce, cod. Beloved by locals and tourists alike.",
    cuisine="Traditional Portuguese", price_range="€€", must_order="Mussels, shrimp, cod"
))

# Porto da Cruz
items.append(item(
    "A Pipa", 32.773, -16.828, "restaurant", "East",
    "Porto da Cruz culinary gem. Best poncha on north coast. Tuna, limpets, sardines. Arrive noon. Closed Sun/Mon. No reservations.",
    cuisine="Seafood / Traditional", price_range="€", must_order="Tuna steaks, homemade poncha, limpets"
))

items.append(item(
    "Restaurante Praca do Engenho", 32.773, -16.829, "restaurant", "East",
    "Beautiful sea and mountain views in Porto da Cruz. Salads, fish dishes. Great for day trips.",
    cuisine="Light Meals / Seafood", price_range="€", must_order="Fish dishes"
))

# Curral das Freiras
items.append(item(
    "Sabores do Curral", 32.721, -16.966, "restaurant", "Funchal & South",
    "Chestnut specialty dishes in Valley of the Nuns. Roof terrace with incredible valley views. Vegetarian options.",
    cuisine="Madeiran / Chestnut", price_range="€€", must_order="Chestnut soup, pork loin with chestnuts"
))

# Camacha
items.append(item(
    "Abrigo do Pastor", 32.680, -16.840, "restaurant", "East",
    "Former shepherd shelter. Wild boar, stewed goat, roasted suckling pig, T-bone. Rustic decor preserves original charm.",
    cuisine="Game / Mountain Meats", price_range="€€", must_order="Wild boar, espetada de vaca com osso"
))

# Seixal
items.append(item(
    "Las Carabaibas", 32.815, -17.100, "restaurant", "North Coast",
    "Limited menu focused on quality execution in Seixal. Bacalhau Verde, gambas soup served in a bread loaf.",
    cuisine="Seafood / Traditional", price_range="€€", must_order="Bacalhau Verde, gambas soup in bread loaf"
))

# DIY Espetada
items.append(item(
    "Talho do Canico", 32.650, -16.850, "restaurant", "Funchal & South",
    "Butcher shop + communal grill. Choose meat, season it, grill over open flames. Standing only. Thu-Sat ONLY. Locals-only vibe.",
    cuisine="DIY Grill / Butcher", price_range="€", must_order="DIY espetada -- choose your cut"
))

# ============================================================
# MARKET
# ============================================================

items.append(item(
    "Mercado dos Lavradores", 32.6487, -16.9035, "market", "Funchal & South",
    "Go to upper floor for local prices. Avoid ground-floor fruit hustlers. Fish market best early AM. Art Deco architecture (1940).",
))

items.append(item(
    "Santo da Serra Sunday Market", 32.720, -16.820, "market", "East",
    "Local produce vendors, street food stalls with local cider and wine. Barraca d'Avo bar serves excellent poncha.",
))

# ============================================================
# PONCHA BARS
# ============================================================

# Funchal
items.append(item(
    "Rei da Poncha", 32.6475, -16.9060, "poncha", "Funchal & South",
    "'The King of Poncha.' Try a meter of ponchas -- multiple mini glasses to sample all flavors. Popular with locals and visitors.",
))

items.append(item(
    "Venda Velha", 32.6468, -16.9065, "poncha", "Funchal & South",
    "Probably the best poncha in Funchal. Weekend DJs, vintage decor. Lively party atmosphere.",
))

items.append(item(
    "A Mercadora", 32.647, -16.907, "poncha", "Funchal & South",
    "Traditional poncha experience in central Funchal. Easy to find.",
))

items.append(item(
    "Pharmacia do Bento", 32.647, -16.909, "poncha", "Funchal & South",
    "Central downtown Funchal location. Easy access for poncha stop.",
))

items.append(item(
    "Os Castrinhos", 32.642, -16.920, "poncha", "Funchal & South",
    "Funchal outskirts. More local atmosphere away from tourist center. Also serves carne de vinha d'alhos.",
))

items.append(item(
    "Madeira Rum House", 32.6455, -16.9070, "poncha", "Funchal & South",
    "Massive rum collection. All poncha flavors. Not a tourist trap -- locals drink here. Lemon = connoisseur's choice.",
))

# Outside Funchal
items.append(item(
    "Taberna da Poncha", 32.730, -16.990, "poncha", "Central Mountains",
    "THE island institution. Serra d'Agua. EUR 3/glass. Peanut shells on floor, business cards on walls. Pilgrimage-worthy.",
))

items.append(item(
    "Bar Filhos D'Anjos", 32.650, -16.975, "poncha", "Funchal & South",
    "Birthplace of poncha in Camara de Lobos. Rustic interiors, CR7 photos. Authentic experience.",
))

items.append(item(
    "Bar Number Two", 32.649, -16.975, "poncha", "Funchal & South",
    "Terrace with views of Camara de Lobos bay. Laid-back, friendly. Great for chatting with locals.",
))

items.append(item(
    "Engenhos do Norte", 32.773, -16.828, "poncha", "East",
    "At the Porto da Cruz rum distillery. Northern coast poncha tradition. Tour distillery and taste rums.",
))

items.append(item(
    "A Venda do Andre", 32.660, -17.010, "poncha", "Funchal & South",
    "Quinta Grande, hills above Cabo Girao. Open since 1950s. Was half poncha bar, half grocery. Feels like a museum.",
))

# Post-hike poncha stops
items.append(item(
    "Bar do Luis", 32.790, -16.845, "poncha", "East",
    "Faial location. Perfect post-hike poncha stop after Eagle's Rock hike.",
))

items.append(item(
    "Cabo Aereo Cafe", 32.810, -16.900, "poncha", "North Coast",
    "Sao Jorge north coast. Good poncha stop after north coast trail hikes.",
))

items.append(item(
    "Sr. Joao", 32.681, -17.100, "poncha", "West & Southwest",
    "Ponta do Sol. Near Levada Nova trail. Post-hike poncha in warm microclimate.",
))

items.append(item(
    "Snack Bar Boca da Encumeada", 32.754, -17.019, "poncha", "Central Mountains",
    "Mountain location at Encumeada pass. Post-hike refreshment at altitude.",
))

# ============================================================
# BAKERIES & CAFES
# ============================================================

items.append(item(
    "Fabrica Santo Antonio", 32.647, -16.912, "bakery", "Funchal & South",
    "Oldest confectionery in Madeira (1893). 5th generation. Bolo de mel, sugar cane biscuits, fennel candy. A living museum.",
))

items.append(item(
    "Padaria Pastelaria Mariazinha", 32.648, -16.910, "bakery", "Funchal & South",
    "Where locals start mornings. Excellent pasteis de nata, bolo de mel. 2 nata + 1 croissant + 1 spinach pocket = EUR 5.",
))

items.append(item(
    "Petit Fours Patisserie", 32.647, -16.912, "bakery", "Funchal & South",
    "THE best pasteis de nata on the island according to TripAdvisor. Freshly baked breads, light lunch options.",
))

items.append(item(
    "Opan Bakery", 32.645, -16.910, "bakery", "Funchal & South",
    "Ubiquitous chain, always excellent. Pastel de nata, salami cake (chocolate), pizza slices. Budget lunch offers. Avenida Arriaga branch recommended.",
))

items.append(item(
    "A Confeitaria", 32.648, -16.911, "bakery", "Funchal & South",
    "Rated #1 bakery in Funchal on TripAdvisor. Always busy with locals. Sandwiches, wraps, cakes. Rua dos Aranhas branch best.",
))

items.append(item(
    "Rodripan Bakery", 32.840, -17.170, "bakery", "North Coast",
    "Near Porto Moniz. Pasteis de nata, bolo de arroz, pineapple pastries. Perfect fuel stop on north coast drives. Visit early.",
))

items.append(item(
    "UauCacau", 32.648, -16.907, "bakery", "Funchal & South",
    "Artisan chocolates: maracuja, poncha, Madeira wine, salted caramel flavors. Exceptional quality. Hot chocolate.",
))

items.append(item(
    "Mya Petit Cafe", 32.648, -16.910, "bakery", "Funchal & South",
    "Instagram-friendly pink interior. Avocado toast, Buddha bowls, pancakes. Excellent brunch spot.",
))

items.append(item(
    "Cafe Fortaleza", 32.647, -16.904, "bakery", "Funchal & South",
    "Behind Sao Joao do Pico Fortress. Artisan lollies (passion fruit especially), local craft beer. Great atmosphere.",
))

items.append(item(
    "O Giro", 32.648, -16.910, "bakery", "Funchal & South",
    "Freshly made churros with ice cream (Kinder Bueno flavor). EUR 3.50 generous portion. Thin, crispy, piping hot.",
))

items.append(item(
    "Loja do Cha", 32.647, -16.908, "bakery", "Funchal & South",
    "Proper English tea behind the cathedral. Extensive tea menu, cakes, crepes. The square is a sun trap year-round.",
))

# ============================================================
# WINE LODGES
# ============================================================

items.append(item(
    "Blandy's Wine Lodge", 32.648, -16.910, "wine", "Funchal & South",
    "7 generations. Tours from premium (2 wines) to private (5 wines). Vineyard tour at Quinta de Santa Luzia is excellent.",
))

items.append(item(
    "Pereira d'Oliveira", 32.649, -16.909, "wine", "Funchal & South",
    "FREE tastings with traditional cakes! 1.5M litres of old vintage stock. Connoisseur's choice. No booking needed. Since 1850.",
))

items.append(item(
    "H.M. Borges", 32.648, -16.910, "wine", "Funchal & South",
    "Founded 1877. Silver Experience: 40-min cellar tour + 2 wine tasting. Artwork by Max Romer. Mon-Fri 9am-1pm, 2:30-5:30pm.",
))

items.append(item(
    "Vinhos Barbeito", 32.650, -16.975, "wine", "Funchal & South",
    "'The Lafite of Madeira.' Family-run since 1946. Farm setting in Camara de Lobos. Platinum tour: 90min, 8 tastings, EUR 24.",
))

items.append(item(
    "Quinta do Barbusano", 32.802, -17.048, "wine", "North Coast",
    "Sao Vicente. 6 wines, floor-to-ceiling valley views. Vineyard tour with petiscos (snacks). Combines wine with north coast excursion.",
))

items.append(item(
    "Terras do Avo", 32.800, -17.050, "wine", "North Coast",
    "Near Sao Vicente. Lovely tasting rooms with amazing views. Edges out Quinta do Barbusano on wine quality per reviewers.",
))

items.append(item(
    "Engenhos do Norte Distillery", 32.773, -16.828, "wine", "East",
    "Porto da Cruz rum distillery. Tour and taste sugarcane rum (aguardente de cana) -- the base of poncha. Gift shop sells bolo de mel.",
))

# ============================================================
# TOWNS (from GeoJSON)
# ============================================================

items.append(item(
    "Camara de Lobos", 32.6485, -16.9752, "town", "Funchal & South",
    "Churchill's fishing village. Colorful boats, great poncha bars. Start point for espetada restaurants in Estreito.",
))

items.append(item(
    "Curral das Freiras", 32.7208, -16.9657, "town", "Funchal & South",
    "Valley of the Nuns. Try chestnut dishes at Sabores do Curral. Poco dos Chefes swimming hole nearby.",
))

items.append(item(
    "Machico", 32.7229, -16.7659, "town", "East",
    "Pleasant town with imported golden sand beach. O Forno restaurant (garlic prawns, free ginja). Near airport.",
))

items.append(item(
    "Santana", 32.8049, -16.8813, "town", "East",
    "Traditional A-frame thatched houses. Quick photo stop. Base for PR9 Queimadas hikes.",
))

items.append(item(
    "Porto da Cruz", 32.7725, -16.8286, "town", "East",
    "Hidden gem. Seawater pool, Engenho do Norte rum distillery, best surf. A Pipa = best poncha (closed Sun/Mon).",
))

items.append(item(
    "Sao Vicente", 32.8023, -17.0472, "town", "North Coast",
    "Quiet town with great promenade. Quebramar restaurant (rotating floor). Caves nearby.",
))

items.append(item(
    "Calheta", 32.7219, -17.1783, "town", "West & Southwest",
    "Golden sand beach (imported from Morocco). Warmest microclimate. Saccharum hotel sunset rooftop.",
))

items.append(item(
    "Ponta do Sol", 32.6812, -17.1041, "town", "West & Southwest",
    "Warm microclimate. Digital nomad hub. Harbor viewpoint for sunset. Sr. Joao poncha bar nearby.",
))

items.append(item(
    "Jardim do Mar Village", 32.7376, -17.2111, "town", "West & Southwest",
    "Car-free 'Garden of the Sea' village. Subtropical flowers, narrow streets, surf spot. Not a formal garden.",
))

items.append(item(
    "Paul do Mar", 32.7548, -17.2272, "town", "West & Southwest",
    "Isolated fishing village at cliff base. Precipicio viewpoint above for sunset.",
))

# ============================================================
# HIDDEN GEMS (from GeoJSON)
# ============================================================

items.append(item(
    "Fanal Forest", 32.815211, -17.152339, "hidden-gem", "West & Southwest",
    "UNESCO laurel forest. Ancient 600-year-old twisted trees in fog. Tim Burton vibes. Best early AM or post-rain.",
))

items.append(item(
    "Calhau da Lapa", 32.663, -17.035, "hidden-gem", "Funchal & South",
    "Fishermen's caves in volcanic cliffs. 700 steep stairs or boat. Waterfall, clear water. You must climb back up!",
))

items.append(item(
    "Achadas da Cruz Cable Car", 32.859433, -17.203731, "hidden-gem", "West & Southwest",
    "Europe's steepest cable car (98% slope). EUR 3 return, CASH ONLY. 8am-7pm. Most tourists skip this. Incredible views.",
))

# Peaks from GeoJSON
items.append(item(
    "Pico Ruivo", 32.7604, -16.9438, "peak", "Central Mountains",
    "1862m -- highest point in Madeira. Reach via PR1.2 from Achada do Teixeira (2.5-3h round trip). 360-degree views.",
))

# Trailheads from GeoJSON
items.append(item(
    "Ribeiro Frio", 32.7396, -16.8869, "town", "East",
    "PR11 Balcoes + PR10 start. Free trout farm. Victor's Snack Bar for poncha. Bus 56 from Funchal.",
))

items.append(item(
    "Parque Florestal das Queimadas", 32.7828, -16.9116, "town", "East",
    "PR9 Caldeirao Verde start. Limited parking -- arrive before 8:30am. Picnic area, restrooms, thatched-roof building.",
))

# Nightlife from GeoJSON
items.append(item(
    "Zona Velha", 32.646, -16.905, "nightlife", "Funchal & South",
    "Heart of nightlife. Painted doors on Rua de Santa Maria. Bar-hop between Rei da Poncha, Venda Velha, Trap Music Bar.",
))

# ============================================================
# BUILD OUTPUT
# ============================================================

output = {
    "meta": {
        "version": "1.0",
        "last_updated": "2026-02-27",
        "total_items": len(items)
    },
    "items": items
}

# Deduplicate IDs by appending -2, -3 etc for collisions
seen_ids = {}
for it in items:
    base_id = it["id"]
    if base_id in seen_ids:
        seen_ids[base_id] += 1
        it["id"] = f"{base_id}-{seen_ids[base_id]}"
    else:
        seen_ids[base_id] = 1

os.makedirs("data", exist_ok=True)
with open("data/madeira_data.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print(f"Wrote {len(items)} items to data/madeira_data.json")

# Print summary by kind
from collections import Counter
kinds = Counter(it["kind"] for it in items)
for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
    print(f"  {k}: {v}")
