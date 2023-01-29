days = int(input())
cargo_ship_event = 0
warship_event = 0
daily_plunder = int(input())
plunder_value = 0
expected_plunder = float(input())

for daily_attack in range(days):
    cargo_ship_event += 1
    warship_event += 1
    if cargo_ship_event == 3:
        plunder_value += daily_plunder + (daily_plunder / 2)
        cargo_ship_event = 0
        continue
    if warship_event == 5:
        plunder_value += daily_plunder
        plunder_value -= plunder_value * 0.3
        warship_event = 0
        continue
    plunder_value += daily_plunder
if plunder_value >= expected_plunder:
    print(f"Ahoy! {plunder_value:.2f} plunder gained.")
elif plunder_value < expected_plunder:
    percentage_from_expected = (plunder_value / expected_plunder) * 100
    print(f"Collected only {percentage_from_expected:.2f}% of the plunder.")