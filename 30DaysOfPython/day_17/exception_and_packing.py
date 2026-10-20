
print("-" * 30, "Exercise", "-" * 30)

names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

try:
    *nordic_countries, es, ru = names

except Exception as e:
    print(f"Failed to unpack the countries: {e}")

else:
    print("Countries unpacked successfully.")

finally:
    print(f"\t Nordic countries: {nordic_countries}")
    print(f"\t Estonia: {es}")
    print(f"\t Russia: {ru}")
