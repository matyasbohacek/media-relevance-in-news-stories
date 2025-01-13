
import os
import json
import PIL
import subprocess
import exifread


def extract_c2pa_metadata(file_path: str) -> dict:
    """
    TODO MB

    :param file_path:
    :return:
    """

    os.environ["PATH"] = "/Users/matyasbohacek/.cargo/bin" + os.pathsep + os.environ["PATH"]

    c2pa_metadata = subprocess.run("c2patool \"" + file_path + "\"", stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE, shell=True)
    c2pa_metadata = json.loads(c2pa_metadata.stdout.decode("utf-8"))

    return c2pa_metadata["manifests"][c2pa_metadata["active_manifest"]]


def extract_conventional_metadata(file_path: str) -> (dict, dict):
    """
    TODO MB

    :param file_path:
    :return:
    """

    img = PIL.Image.open(file_path)
    spec_exif_data = {PIL.ExifTags.TAGS[k]: v for k, v in img.getexif().items() if k in PIL.ExifTags.TAGS}

    #
    gen_exif_data = {}
    with open(file_path, "rb") as f:
        gen_exif_data = exifread.process_file(f)

    return spec_exif_data, gen_exif_data


def parse_content_credentials(item):
    entry = []
    if 'title' in item:
        entry.append(f"Title: {item['title']}")

    if 'format' in item:
        entry.append(f"Format: {item['format']}")

    if 'signature_info' in item and 'time' in item['signature_info']:
        entry.append(f"Time of Capture: {item['signature_info']['time']}")

    if 'assertions' in item:
        for assertion in item['assertions']:
            if 'label' in assertion and assertion['label'] == 'c2pa.actions':
                actions = assertion.get('data', {}).get('actions', [])
                for action in actions:
                    action_core = action['action'].split('.')[-1]
                    action_str = f"Action: {action_core.replace('c2pa', '').replace('_', ' ').capitalize()}"
                    if 'softwareAgent' in action:
                        softwareAgent = action['softwareAgent']
                        if 'Adobe Firefly' in softwareAgent:
                            action_str += " by Adobe Firefly AI model"
                        else:
                            action_str += f" by {softwareAgent.split()[0]}"
                    entry.append(action_str)

            if 'label' in assertion and assertion['label'] == 'c2pa.metadata':
                metadata = assertion.get('data', {})
                if 'Iptc4xmpExt:LocationCreated' in metadata:
                    location = metadata['Iptc4xmpExt:LocationCreated']
                    if 'Iptc4xmpExt:Latitude' in location and 'Iptc4xmpExt:Longitude' in location:
                        entry.append(f"Verified Location: Latitude {location['Iptc4xmpExt:Latitude']}, Longitude {location['Iptc4xmpExt:Longitude']}")
                #if 'dc:description' in metadata:
                #    entry.append(f"Description: {metadata['dc:description']}")
                if 'photoshop:DateCreated' in metadata:
                    entry.append(f"Date Created: {metadata['photoshop:DateCreated']}")
                if 'photoshop:Source' in metadata:
                    entry.append(f"Source: {metadata['photoshop:Source']}")

    return "\n".join(entry)


def extract_and_preprocess_c2pa(item):
    md_c2pa = extract_c2pa_metadata(item)
    return parse_content_credentials(md_c2pa)
    # md_exif_spec, md_exif_gen = extract_conventional_metadata(item)
