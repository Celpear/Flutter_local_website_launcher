import os
import yaml

# Path to the pubspec.yaml file
pubspec_path = 'pubspec.yaml'
# Path to the webexport directory
startverzeichnis = 'assets/webexport'

assetcount = 0
# Read the YAML file
with open(pubspec_path, 'r') as file:
    data = yaml.safe_load(file)

# Access the "assets" section
if 'flutter' in data and 'assets' in data['flutter']:
    #clear assets
    data['flutter']['assets'].clear()
    for ordnerpfad, _, _ in os.walk(startverzeichnis):
        data['flutter']['assets'].append(f"{ordnerpfad}/")
    assetcount = len(data['flutter']['assets'])
    # Create new yaml file
    yaml_output = yaml.dump(data, default_flow_style=False)
    # Write new yaml file
    with open('pubspec.yaml', 'w') as file:
        file.write(yaml_output)
    print(f"The file {pubspec_path} was successful updated with {assetcount} paths. Now Ready for 'flutter pub get'")
    
else:
    print("Keine Assets gefunden.")


