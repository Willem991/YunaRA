import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote
import posixpath


def extract_epub_cover(epub_path: str | Path, output_path: str | Path):
    epub_path = Path(epub_path)
    output_path = Path(output_path)

    with zipfile.ZipFile(epub_path, "r") as epub:

        # -----------------------------------------
        # Find the OPF file
        # -----------------------------------------

        container_xml = epub.read("META-INF/container.xml")
        container_root = ET.fromstring(container_xml)

        rootfile = None

        for element in container_root.iter():
            if element.tag.endswith("rootfile"):
                rootfile = element.get("full-path")
                break

        if not rootfile:
            raise ValueError("Could not find EPUB OPF file")

        # -----------------------------------------
        # Read OPF
        # -----------------------------------------

        opf_xml = epub.read(rootfile)
        opf_root = ET.fromstring(opf_xml)

        opf_directory = posixpath.dirname(rootfile)

        # -----------------------------------------
        # Build manifest
        # -----------------------------------------

        manifest = {}

        for element in opf_root.iter():
            if element.tag.endswith("item"):
                item_id = element.get("id")
                href = element.get("href")
                media_type = element.get("media-type")
                properties = element.get("properties", "")

                if item_id and href:
                    manifest[item_id] = {
                        "href": href,
                        "media_type": media_type,
                        "properties": properties
                    }

        # -----------------------------------------
        # Find cover
        # -----------------------------------------

        cover_item = None

        # EPUB 3:
        # <item properties="cover-image" ...>
        for item in manifest.values():
            if "cover-image" in item["properties"].split():
                cover_item = item
                break

        # EPUB 2:
        # <meta name="cover" content="cover-image-id"/>
        if cover_item is None:

            for element in opf_root.iter():
                if not element.tag.endswith("meta"):
                    continue

                if element.get("name") == "cover":
                    cover_id = element.get("content")

                    if cover_id in manifest:
                        cover_item = manifest[cover_id]

                    break

        if cover_item is None:
            raise ValueError("Could not find cover image")

        # -----------------------------------------
        # Resolve image path
        # -----------------------------------------

        cover_href = unquote(cover_item["href"])

        cover_path = posixpath.normpath(
            posixpath.join(opf_directory, cover_href)
        )

        # -----------------------------------------
        # Extract image
        # -----------------------------------------

        try:
            image_data = epub.read(cover_path)
        except KeyError:
            raise ValueError(
                f"Cover image not found in EPUB: {cover_path}"
            )

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        output_path.write_bytes(image_data)

        return output_path