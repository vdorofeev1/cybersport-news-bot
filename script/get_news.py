from script.cybersport_requests.materials_request import materials_request
from script.cybersport_requests.slug_request import slug_request, clean_text


def get_news():
    response = []

    materials_response = materials_request()
    materials = materials_response["data"]

    for material in materials:
        slug = material["attributes"]["slug"]
        title = material["attributes"]["title"]

        message = ""
        message += "\n" + title + "\n\n"

        slug_response = slug_request(slug)
        blocks = slug_response["data"]["attributes"]["content"]["blocks"]

        for block in blocks:
            data = block["data"]
            if "text" in data:
                text = block["data"]["text"]

                message += clean_text(text) + "\n"
        response.append(message)

    return response


